#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор документації PDP: TMDL -> JSON (catalog) -> Markdown (docs).

Повний обсяг: усі міри з _Measures.tmdl та всі таблиці моделі.
Бізнес-суть НЕ вигадується: береться цитатами з wiki «Таблиць джерел даних»
(колонки «Поле», «Назва реквізиту», «Коментар»). Без відповідності — порожньо,
факт у docs/validation.md. Поле manualNotes зберігається між регенераціями.
"""
import os, re, json, argparse, datetime, subprocess

# ---------------------------------------------------------------- slug
CYR = {
 'а':'a','б':'b','в':'v','г':'h','ґ':'g','д':'d','е':'e','є':'ie','ж':'zh','з':'z',
 'и':'y','і':'i','ї':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p',
 'р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh','ц':'ts','ч':'ch','ш':'sh','щ':'shch',
 'ь':'','ю':'iu','я':'ia',"'":'','’':''
}
def slugify(s):
    out=[]
    for ch in s.strip().lower():
        if ch in CYR: out.append(CYR[ch])
        elif ch.isascii() and ch.isalnum(): out.append(ch)
        else: out.append('-')
    return re.sub(r'-+','-',''.join(out)).strip('-') or 'x'

def uniq(slug, used):
    s=slug; i=2
    while s in used: s=f"{slug}-{i}"; i+=1
    used.add(s); return s

def anchor(h):
    h=re.sub(r'[`"\'\\*]','',h.strip().lower())
    h=re.sub(r'[^\w\s-]','',h, flags=re.U)
    return re.sub(r'\s+','-',h).strip('-')

# ---------------------------------------------------------------- TMDL helpers
def indent(line):
    n=0
    for ch in line:
        if ch=='\t': n+=1
        else: break
    return n

def dedent(lines):
    nz=[l for l in lines if l.strip()]
    if not nz: return ""
    m=min(indent(l) for l in nz)
    return "\n".join(l[m:] if len(l)>=m else l for l in lines).strip("\n")

PROP=('displayFolder:','lineageTag:','formatString:','dataType:','isHidden',
      'annotation ','changedProperty','/// ','formatStringDefinition')

def parse_measures(path):
    raw=open(path,encoding="utf-8").read().split("\n")
    starts=[i for i,l in enumerate(raw) if indent(l)==1 and l.lstrip('\t').startswith("measure ")]
    starts.append(len(raw))
    res=[]
    for a,b in zip(starts,starts[1:]):
        blk=raw[a:b]; core=blk[0].lstrip('\t')
        m=re.match(r"measure (?:'([^']+)'|\"([^\"]+)\"|([^=]+?)) ?=(.*)$",core)
        if not m: continue
        name=(m.group(1) or m.group(2) or (m.group(3) or "").strip())
        rest=m.group(4); body=blk[1:]; r=rest.strip(); dax=""
        if r.startswith('```'):
            buf=[]
            for l in body:
                if l.strip()=='```': break
                buf.append(l)
            dax=dedent(buf)
        elif r=="":
            buf=[]
            for l in body:
                if indent(l)<=2 and l.lstrip('\t').startswith(PROP): break
                buf.append(l)
            dax=dedent(buf)
        else: dax=r
        props={}
        for l in body:
            if indent(l)<2: continue
            ls=l.lstrip('\t')
            for k in ('displayFolder','lineageTag','formatString','dataType'):
                if ls.startswith(k+':'): props[k]=ls.split(':',1)[1].strip()
            if ls.startswith('isHidden'): props['isHidden']=True
        res.append({"name":name,"dax":dax,
            "displayFolder":props.get("displayFolder",""),
            "formatString":props.get("formatString",""),
            "dataType":props.get("dataType",""),
            "isHidden":bool(props.get("isHidden",False))})
    return res

def list_tables(tdir):
    mp={}
    for fn in os.listdir(tdir):
        if not fn.endswith(".tmdl"): continue
        p=os.path.join(tdir,fn)
        first=open(p,encoding="utf-8").readline().strip()
        mm=re.match(r"table\s+(?:'([^']+)'|(.+))$",first)
        if mm: mp[(mm.group(1) or mm.group(2)).strip()]=p
    return mp

def parse_table(path):
    raw=open(path,encoding="utf-8").read().split("\n")
    name=""; mm=re.match(r"table\s+(?:'([^']+)'|(.+))$",raw[0].strip())
    if mm: name=(mm.group(1) or mm.group(2)).strip()
    cols=[]; i=0
    while i<len(raw):
        l=raw[i]
        if indent(l)==1 and l.lstrip('\t').startswith("column "):
            core=l.lstrip('\t')
            cm=re.match(r"column (?:'([^']+)'|([^=]+?))(?: =(.*))?$",core)
            cname=(cm.group(1) or (cm.group(2) or '').strip()) if cm else core
            calc=cm.group(3) is not None if cm else False
            dt=""; src=""; j=i+1
            while j<len(raw) and indent(raw[j])>=2:
                ls=raw[j].lstrip('\t')
                if ls.startswith("dataType:"): dt=ls.split(':',1)[1].strip()
                if ls.startswith("sourceColumn:"): src=ls.split(':',1)[1].strip()
                j+=1
            cols.append({"name":cname,"dataType":dt,"source":src,"isCalculated":bool(calc)})
        i+=1
    text=open(path,encoding="utf-8").read()
    pq=""; pm=re.search(r"partition\s+(\S+)\s*=",text)
    if pm: pq=pm.group(1)
    server=db=""; sm=re.search(r'Sql\.Database\(\s*"([^"]+)"\s*,\s*"([^"]+)"',text)
    if sm: server,db=sm.group(1),sm.group(2)
    src=set()
    for q in re.findall(r'Query="(.*?)"',text,re.S):
        for s,t in re.findall(r'\[(\w+)\]\.\[(\w+)\]',q): src.add(f"{s}.{t}")
        for s,t in re.findall(r'FROM\s+(\w+)\.(\w+)',q): src.add(f"{s}.{t}")
    for s,it in re.findall(r'Schema="(\w+)",\s*Item="([^"]+)"',text): src.add(f"{s}.{it}")
    return {"name":name,"columns":cols,"powerQuery":pq,"server":server,"db":db,
            "sourceTables":sorted(src)}

def parse_relationships(path):
    if not os.path.exists(path): return []
    raw=open(path,encoding="utf-8").read().split("\n"); rels=[]; cur=None
    for l in raw:
        if l.startswith("relationship "):
            if cur: rels.append(cur)
            cur={"from":None,"to":None,"cross":"single"}
        elif cur is not None:
            ls=l.strip()
            if ls.startswith("fromColumn:"): cur["from"]=ls.split(':',1)[1].strip()
            elif ls.startswith("toColumn:"): cur["to"]=ls.split(':',1)[1].strip()
    if cur: rels.append(cur)
    out=[]
    for r in rels:
        if not r["from"] or not r["to"]: continue
        ft,fc=r["from"].rsplit('.',1); tt,tc=r["to"].rsplit('.',1)
        out.append({"fromTable":ft,"fromColumn":fc,"toTable":tt,"toColumn":tc})
    return out

def deps(dax, mnames, tnames):
    cols=set(); ut=set(); um=set()
    for t,c in re.findall(r"'([^']+)'\[([^\]]+)\]",dax):
        cols.add(f"{t}[{c}]");  ut.add(t) if t in tnames else None
    for t,c in re.findall(r"(?<![\w'.\]])([A-Za-z_]\w*)\[([^\]]+)\]",dax):
        if t in tnames: cols.add(f"{t}[{c}]"); ut.add(t)
    for nm in re.findall(r"\[([^\]]+)\]",dax):
        if nm in mnames: um.add(nm)
    return sorted(cols), sorted(ut), sorted(um)

# ---------------------------------------------------------------- wiki index
def split_md_tables(text):
    """Повертає список таблиць: (headers[], rows[][]) з markdown."""
    out=[]; lines=text.split("\n"); i=0
    while i<len(lines):
        if lines[i].lstrip().startswith("|") and i+1<len(lines) and re.match(r"^\s*\|?[\s:|-]+\|?\s*$",lines[i+1]):
            head=[c.strip() for c in lines[i].strip().strip('|').split('|')]
            rows=[]; j=i+2
            while j<len(lines) and lines[j].lstrip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip('|').split('|')]); j+=1
            out.append((head,rows)); i=j
        else: i+=1
    return out

def build_wiki_index(root):
    """field_lower -> [{requisite, comment, factTable, page, anchor}].  Також metric_name_lower."""
    by_field={}; by_metric={}
    if not root or not os.path.isdir(root): return by_field, by_metric
    for dp,_,files in os.walk(root):
        if ".attachments" in dp: continue
        for fn in files:
            if not fn.endswith(".md"): continue
            p=os.path.join(dp,fn)
            rel=os.path.relpath(p,root)[:-3].replace("\\","/")
            try: text=open(p,encoding="utf-8").read()
            except Exception: continue
            # карта позиція->останній заголовок (для anchor)
            heads=[(m.start(),m.group(2)) for m in re.finditer(r"^(#{1,6})\s+(.*)$",text,re.M)]
            def anchor_at(pos):
                a="";
                for s,h in heads:
                    if s<=pos: a=h
                    else: break
                return anchor(a) if a else ""
            for head,rows in split_md_tables(text):
                low=[h.lower() for h in head]
                def col(*keys):
                    for k in keys:
                        for idx,h in enumerate(low):
                            if k in h: return idx
                    return -1
                fi=col("поле"); ri=col("назва реквізиту","реквізит","назва метрик","назва"); ci=col("коментар","опис"); ti=col("таблиця джерело","фактова таблиця","таблиця")
                if fi<0 and ri<0: continue
                # позиція таблиці у тексті для anchor (беремо позицію заголовка перед нею — наближено за першим рядком)
                tpos=text.find("|".join(head[:2])) if head else 0
                anc=anchor_at(tpos if tpos>=0 else 0)
                for r in rows:
                    if len(r)<=max(fi,ri): continue
                    field=(r[fi].strip() if 0<=fi<len(r) else "")
                    field=re.sub(r"<br>.*","",field).strip().strip("[]")
                    req=(r[ri].strip() if 0<=ri<len(r) else "")
                    com=(r[ci].strip() if 0<=ci<len(r) else "")
                    fact=(r[ti].strip() if 0<=ti<len(r) else "")
                    rec={"requisite":req,"comment":com,"factTable":fact,"page":rel,"anchor":anc}
                    if field and field not in ("Х","х","-"):
                        by_field.setdefault(field.lower(),[]).append(rec)
                    if req and len(req)>2:
                        by_metric.setdefault(req.lower(),[]).append(rec)
    return by_field, by_metric

def business_for(cols, name, by_field, by_metric):
    """Повертає (definition, purpose, requirementRefs) з цитат wiki; без збігу — порожньо."""
    fields=[c.split('[',1)[1][:-1] for c in cols if '[' in c]
    def _skip(f):
        u=f.upper()
        return u.endswith(("_ID","_KEY")) or u in {"ID","DATE","EXEC_DATE","PLAN_DATE","ORDER","USER_ACCESS_ID","EMPLOYEE_ID"}
    fields=[f for f in fields if not _skip(f)]
    defs=[]; purpose=[]; refs=set(); seen=set()
    for f in fields:
        for rec in by_field.get(f.lower(),[]):
            key=(f.lower(),rec["requisite"],rec["page"])
            if key in seen: continue
            seen.add(key)
            if rec["requisite"]: defs.append(f"{f} → {rec['requisite']}")
            if rec["comment"]: purpose.append(rec["comment"])
            if rec["page"]:
                refs.add(rec["page"]+("#"+rec["anchor"] if rec["anchor"] else ""))
    # якщо не знайшли за полями — спроба за назвою (останній сегмент після крапки)
    if not defs:
        tail=name.split('.')[-1].strip().lower()
        for rec in by_metric.get(tail,[]):
            if rec["requisite"]: defs.append(rec["requisite"])
            if rec["comment"]: purpose.append(rec["comment"])
            if rec["page"]: refs.add(rec["page"]+("#"+rec["anchor"] if rec["anchor"] else ""))
    definition="; ".join(dict.fromkeys(defs))
    purpose_txt=" ".join(dict.fromkeys(purpose))[:600]
    return definition, purpose_txt, sorted(refs)

# ---------------------------------------------------------------- main
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pbip",default="/sessions/modest-charming-shannon/mnt/GIT_local")
    ap.add_argument("--sm",default="PDP.SemanticModel")
    ap.add_argument("--wiki",default="/sessions/modest-charming-shannon/mnt/azure-wiki/PDP.wiki/Функціональні-вимоги/Вимоги-до-звіту-People-Digital-Profile")
    ap.add_argument("--out",default="/tmp/pdp-docs")
    ap.add_argument("--folder",default="")  # порожньо = усі displayFolder
    args=ap.parse_args()

    defn=os.path.join(args.pbip,args.sm,"definition"); tdir=os.path.join(defn,"tables")
    mfile=os.path.join(tdir,"_Measures.tmdl")
    try: commit=subprocess.check_output(["git","-C",args.pbip,"rev-parse","HEAD"],text=True).strip()
    except Exception: commit=""
    # extractedAt прив'язуємо до дати коміту джерела (а не wall-clock), щоб повторна
    # генерація без змін у джерелі давала байт-ідентичний вихід — ідемпотентність
    # щоденного автооновлення (Task C): commit || "no changes" спрацьовує коректно.
    try: now=subprocess.check_output(["git","-C",args.pbip,"show","-s","--format=%cI","HEAD"],text=True).strip()
    except Exception: now=datetime.datetime.now().astimezone().isoformat(timespec="seconds")

    measures=parse_measures(mfile)
    if args.folder: measures=[m for m in measures if m["displayFolder"]==args.folder]
    mnames={m["name"] for m in measures}
    tmap=list_tables(tdir); tnames=set(tmap)
    by_field,by_metric=build_wiki_index(args.wiki)

    # усі таблиці моделі як сутності
    entities={tn:parse_table(p) for tn,p in tmap.items()}
    rels=parse_relationships(os.path.join(defn,"relationships.tmdl"))
    rels_for=lambda tn:[r for r in rels if r["fromTable"]==tn or r["toTable"]==tn]

    OUT=args.out
    cat_m=os.path.join(OUT,"catalog","measures"); cat_e=os.path.join(OUT,"catalog","entities")
    doc_m=os.path.join(OUT,"docs","measures");    doc_e=os.path.join(OUT,"docs","entities")
    for d in (cat_m,cat_e,doc_m,doc_e): os.makedirs(d,exist_ok=True)
    def manual(path):
        if os.path.exists(path):
            try: return json.load(open(path,encoding="utf-8")).get("manualNotes","")
            except Exception: return ""
        return ""

    used=set(); index=[]; V={"no_business":[],"broken_dep":[],"orphan_cols":[],"no_wiki":[]}
    rel_meas={tn:[] for tn in entities}

    # ---- міри ----
    slug_m={}
    for m in measures: slug_m[m["name"]]=uniq(slugify(m["name"]),used)
    for m in measures:
        c,t,um=deps(m["dax"],mnames,tnames)
        for tn in t:
            if tn in rel_meas: rel_meas[tn].append(m["name"])
        for dep in um:
            if dep not in mnames: V["broken_dep"].append(f"{m['name']} → {dep}")
        st=set()
        for tn in t:
            e=entities.get(tn)
            if e: st|=set(e["sourceTables"])
        define,purpose,refs=business_for(c,m["name"],by_field,by_metric)
        slug=slug_m[m["name"]]; jpath=os.path.join(cat_m,slug+".json")
        seg=[s for s in m["displayFolder"].split("\\") if s]
        obj={"id":slug,"type":"measure","name":m["name"],"homeTable":"_Measures",
          "displayFolder":m["displayFolder"],"formatString":m["formatString"],
          "dataType":m["dataType"],"isHidden":m["isHidden"],"description":"",
          "dax":m["dax"],
          "dependencies":{"measures":um,"columns":c,"tables":t},
          "lineage":{"sourceTables":sorted(st),
                     "sourceColumns":sorted({x.split('[',1)[1][:-1] for x in c}),
                     "powerQuery":(entities[t[0]]["powerQuery"] if t else "")},
          "business":{"definition":define,"purpose":purpose,"requirementRefs":refs},
          "tags":sorted(set([slugify(s) for s in seg]+["pdp"])),
          "source":{"repo":"PDP","file":f"{args.sm}/definition/tables/_Measures.tmdl",
                    "commit":commit,"extractedAt":now},
          "manualNotes":manual(jpath)}
        json.dump(obj,open(jpath,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
        index.append({"id":slug,"type":"measure","name":m["name"],
                      "displayFolder":m["displayFolder"],"file":f"measures/{slug}.md"})
        if not define: V["no_business"].append(m["name"]);
        if not refs: V["no_wiki"].append(m["name"])
        write_measure_md(os.path.join(doc_m,slug+".md"),obj,slug_m)

    # ---- сутності ----
    slug_e={tn:uniq(slugify(tn),used) for tn in entities}
    for tn,e in entities.items():
        er=rels_for(tn)
        for col in e["columns"]:
            if not col["source"] and not col["isCalculated"]:
                V["orphan_cols"].append(f"{tn}[{col['name']}]")
        # бізнес сутності — за фактовою таблицею (DM.*) у wiki
        ent_def=""; ent_refs=set()
        for st in e["sourceTables"]:
            base=st.split('.')[-1].lower()
            for recs in by_field.values():
                for rec in recs:
                    if base and base in rec["factTable"].lower():
                        ent_refs.add(rec["page"]+("#"+rec["anchor"] if rec["anchor"] else ""))
        slug=slug_e[tn]; jpath=os.path.join(cat_e,slug+".json")
        obj={"id":slug,"type":"entity","name":tn,"definition":ent_def,
          "server":e["server"],"db":e["db"],"powerQuery":e["powerQuery"],
          "sourceTables":e["sourceTables"],"columns":e["columns"],
          "relationships":[{"toTable":(r["toTable"] if r["fromTable"]==tn else r["fromTable"]),
                            "fromColumn":r["fromColumn"],"toColumn":r["toColumn"],
                            "role":("from" if r["fromTable"]==tn else "to")} for r in er],
          "relatedMeasures":sorted(set(rel_meas.get(tn,[]))),
          "requirementRefs":sorted(ent_refs),
          "source":{"repo":"PDP","file":f"{args.sm}/definition/tables/{tn}.tmdl",
                    "commit":commit,"extractedAt":now},
          "manualNotes":manual(jpath)}
        json.dump(obj,open(jpath,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
        index.append({"id":slug,"type":"entity","name":tn,"displayFolder":"","file":f"entities/{slug}.md"})
        write_entity_md(os.path.join(doc_e,slug+".md"),obj,slug_m)

    json.dump(index,open(os.path.join(OUT,"catalog","_index.json"),"w",encoding="utf-8"),
              ensure_ascii=False,indent=2)
    write_measures_index(os.path.join(doc_m,"index.md"),measures,slug_m)
    write_entities_index(os.path.join(doc_e,"index.md"),entities,slug_e)
    write_model(os.path.join(OUT,"docs","model.md"),entities,rels)
    write_glossary(os.path.join(OUT,"docs","glossary.md"))
    write_index(os.path.join(OUT,"docs","index.md"),measures,entities)
    write_validation(os.path.join(OUT,"docs","validation.md"),V,len(measures))
    append_changelog(os.path.join(OUT,"docs","changelog.md"),now,len(measures),len(entities),commit)
    state={"pbip":{"commit":commit,"extractedAt":now,"measures":len(measures),"entities":len(entities),
                   "wiki_fields_indexed":len(by_field)}}
    json.dump(state,open(os.path.join(OUT,".cowork","state.json"),"w",encoding="utf-8"),
              ensure_ascii=False,indent=2)
    cov=len(measures)-len(V["no_business"])
    print(f"OK: {len(measures)} measures, {len(entities)} entities, business={cov}/{len(measures)}, wiki_fields={len(by_field)}, commit={commit[:8]}")

# ---------------------------------------------------------------- MD writers
def ptable(rows):
    return "\n".join(["| Властивість | Значення |","|---|---|"]+[f"| {k} | {v} |" for k,v in rows])

def write_measure_md(path,o,sm):
    L=[f"# {o['name']}",""]
    L.append(ptable([("Тип","міра"),("Home table",o["homeTable"]),
        ("displayFolder",f"`{o['displayFolder']}`"),
        ("formatString",f"`{o['formatString']}`" if o['formatString'] else "—"),
        ("dataType",o["dataType"] or "—"),("Прихована","так" if o["isHidden"] else "ні")]))
    L+=["","## DAX","","```dax",o["dax"] or "—","```",""]
    lin=o["lineage"]; L+=["## Джерела",""]
    if lin["sourceTables"]: L.append("Вихідні таблиці: "+", ".join(f"`{t}`" for t in lin["sourceTables"]))
    if lin["sourceColumns"]: L+=["", "Колонки: "+", ".join(f"`{c}`" for c in lin["sourceColumns"])]
    if lin["powerQuery"]: L+=["", f"Power Query: `{lin['powerQuery']}`"]
    if not (lin["sourceTables"] or lin["sourceColumns"]): L.append("—")
    b=o["business"]; L+=["","## Бізнес-суть",""]
    if b["definition"]:
        L.append(b["definition"])
        if b["purpose"]: L+=["", b["purpose"]]
        if b["requirementRefs"]:
            L+=["","**Вимоги:** "+", ".join(f"`{r}`" for r in b["requirementRefs"])]
    else:
        L+=['!!! warning "Без бізнес-визначення"',
            "    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`."]
    L+=["","## Залежності",""]
    dm=o["dependencies"]["measures"]; dt=o["dependencies"]["tables"]
    if dm: L+=["Міри: "+", ".join(f"[{n}](../measures/{sm[n]}.md)" if n in sm else f"`{n}`" for n in dm),""]
    if dt: L+=["Таблиці: "+", ".join(f"`{t}`" for t in dt),""]
    if o["dependencies"]["columns"]: L.append("Колонки: "+", ".join(f"`{c}`" for c in o["dependencies"]["columns"]))
    if not (dm or dt): L.append("—")
    L+=["","## Схема","","```mermaid","graph LR",f'  M["{o["name"]}"]']
    for t in dt: L.append(f"  M --> {t}")
    L+=["```","","## Нотатки","",o["manualNotes"] if o["manualNotes"] else "_порожньо_"]
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_entity_md(path,o,sm):
    L=[f"# {o['name']}",""]
    L.append(ptable([("Тип","бізнес-сутність / таблиця"),
        ("Сервер",f"`{o['server']}`" if o['server'] else "—"),
        ("База",f"`{o['db']}`" if o['db'] else "—"),
        ("Power Query",f"`{o['powerQuery']}`" if o['powerQuery'] else "—"),
        ("Джерела",", ".join(f"`{t}`" for t in o["sourceTables"]) or "—")]))
    if o["requirementRefs"]:
        L+=["","**Вимоги:** "+", ".join(f"`{r}`" for r in o["requirementRefs"])]
    L+=["","## Колонки","","| Колонка | Тип | Джерело | Calc |","|---|---|---|---|"]
    for c in o["columns"]:
        L.append(f"| {c['name']} | {c['dataType'] or '—'} | {c['source'] or '—'} | {'так' if c['isCalculated'] else ''} |")
    L+=["","## Зв'язки",""]
    if o["relationships"]:
        L+=["| Напрям | Колонка | Пов'язана таблиця | Колонка |","|---|---|---|---|"]
        for r in o["relationships"]:
            L.append(f"| {r['role']} | {r['fromColumn']} | `{r['toTable']}` | {r['toColumn']} |")
    else: L.append("—")
    L+=["","## Пов'язані міри",""]
    if o["relatedMeasures"]:
        L.append(f"Усього: {len(o['relatedMeasures'])}.")
        L+=[ (f"- [{n}](../measures/{sm[n]}.md)" if n in sm else f"- `{n}`") for n in o["relatedMeasures"][:60]]
        if len(o["relatedMeasures"])>60: L.append(f"- … і ще {len(o['relatedMeasures'])-60}")
    else: L.append("—")
    L+=["","## Нотатки","",o["manualNotes"] if o["manualNotes"] else "_порожньо_"]
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_measures_index(path,measures,sm):
    groups={}
    for m in measures: groups.setdefault(m["displayFolder"] or "(без теки)",[]).append(m)
    L=["# Міри",f"","Усього: **{len(measures)}**.",""]
    for df in sorted(groups):
        L+=[f"## {df}","","| Міра | formatString |","|---|---|"]
        for m in sorted(groups[df],key=lambda x:x["name"]):
            L.append(f"| [{m['name']}](./{sm[m['name']]}.md) | `{m['formatString']}` |")
        L.append("")
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_entities_index(path,entities,se):
    L=["# Бізнес-сутності",f"","Усього: **{len(entities)}**.","","| Таблиця | Джерела |","|---|---|"]
    for tn,e in sorted(entities.items()):
        L.append(f"| [{tn}](./{se[tn]}.md) | {', '.join('`'+t+'`' for t in e['sourceTables']) or '—'} |")
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_model(path,entities,rels):
    # mermaid erDiagram: ідентифікатори вузлів мають бути [A-Za-z0-9_]; імена таблиць
    # із пробілом/крапкою (t_AC Burnout, p_AC.Loss_Productivity) інакше не рендеряться.
    nid=lambda s: re.sub(r"\W","_",s)
    L=["# Схема моделі","","Зв'язки таблиць (many → one).","","```mermaid","erDiagram"]
    names=set(entities)
    for r in rels:
        if r["fromTable"] in names and r["toTable"] in names:
            L.append(f'  {nid(r["toTable"])} ||--o{{ {nid(r["fromTable"])} : "{r["fromColumn"]}"')
    L+=["```"]
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_glossary(path):
    L=["# Глосарій","",
       "- **OKR** — Objectives and Key Results, цілі та ключові результати.",
       "- **KR** — Key Result, ключовий результат.",
       "- **PP** — Personal Profile, персональний профіль.",
       "- **GP** — Group Profile, груповий профіль.",
       "- **AC** — Analytical Cases, аналітичні кейси.",
       "- **TRS** — Target Remuneration Salary, цільовий річний дохід.",
       "- **lineage** — походження даних: таблиці/колонки джерела та запит Power Query.",
       "- **DAX / TMDL** — мова виразів / текстовий формат моделі Power BI."]
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_index(path,measures,entities):
    L=["# People Digital Profile — документація моделі","",
       "Пошуковий каталог мір і бізнес-сутностей семантичної моделі PDP.","",
       f"**Обсяг:** {len(measures)} мір, {len(entities)} сутностей.","",
       "## Розділи","",
       "- [Міри](measures/index.md)","- [Бізнес-сутності](entities/index.md)",
       "- [Схема моделі](model.md)","- [Глосарій](glossary.md)",
       "- [Валідація](validation.md)","- [Журнал змін](changelog.md)","",
       "Пошук — у верхньому рядку (вбудований, клієнтський)."]
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_validation(path,v,total):
    def block(title,items):
        out=[f'!!! warning "{title} — {len(items)}"']
        out+=[f"    - {it}" for it in items[:300]] if items else ["    немає"]
        if len(items)>300: out.append(f"    - … і ще {len(items)-300}")
        return out
    L=["# Валідація","",f"Усього мір: **{total}**. Із бізнес-визначенням: **{total-len(v['no_business'])}**.",""]
    L+=block("Міри без бізнес-визначення",v["no_business"])+[""]
    L+=block("Міри без посилання на вимоги",sorted(set(v["no_wiki"])))+[""]
    L+=block("Зламані залежності DAX",v["broken_dep"])+[""]
    L+=block("Колонки без lineage (orphan)",v["orphan_cols"])+[""]
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def append_changelog(path,now,nm,ne,commit):
    line=f"- {now} — регенерація: {nm} мір, {ne} сутностей (PBIP commit `{commit[:8]}`).\n"
    if os.path.exists(path):
        existing=open(path,encoding="utf-8").read()
        # ідемпотентність: не дублювати запис, якщо джерело не змінилося (той самий останній рядок)
        if existing.rstrip().endswith(line.rstrip()): return
        with open(path,"a",encoding="utf-8") as f: f.write(line)
    else:
        with open(path,"w",encoding="utf-8") as f: f.write("# Журнал змін\n\n"+line)

if __name__=="__main__":
    main()
