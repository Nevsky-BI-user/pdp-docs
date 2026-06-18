#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор документації PDP: TMDL -> JSON (catalog) -> Markdown (docs).

Повний обсяг: усі міри з _Measures.tmdl та всі таблиці моделі.
Бізнес-суть НЕ вигадується: береться цитатами з wiki «Таблиць джерел даних»
(колонки «Поле», «Назва реквізиту», «Коментар»). Без відповідності — порожньо,
факт у docs/validation.md. Поле manualNotes зберігається між регенераціями.
"""
import os, re, json, argparse, datetime, subprocess, urllib.parse

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
    """Структуроване бізнес-визначення з wiki:
       name  — точна бізнес-назва (міра == реквізит ТЗ);
       logic — опис/логіка з ТЗ (коментарі, дедуп);
       fieldMetrics — [(поле, [бізнес-метрики])] (допоміжна мапа);
       refs  — сторінки ТЗ. Без вигадок — лише цитати."""
    fields=[c.split('[',1)[1][:-1] for c in cols if '[' in c]
    def _skip(f):
        u=f.upper()
        return u.endswith(("_ID","_KEY")) or u in {"ID","DATE","EXEC_DATE","PLAN_DATE","ORDER","USER_ACCESS_ID","EMPLOYEE_ID"}
    fields=[f for f in fields if not _skip(f)]
    tail=name.split('.')[-1].strip()
    # 1) ТОЧНИЙ матч: назва міри == бізнес-реквізит → точна назва + ТЗ-логіка
    name_recs=by_metric.get(tail.lower(),[])
    bname=""; logic=[]; refs=set()
    for rec in name_recs:
        if not bname and rec["requisite"]: bname=rec["requisite"]
        if rec["comment"] and rec["comment"] not in logic: logic.append(rec["comment"])
        if rec["page"]: refs.add(rec["page"]+("#"+rec["anchor"] if rec["anchor"] else ""))
    # 2) поля-джерела → бізнес-метрики (мапа) + резервні коментарі/посилання (лише без точного матчу)
    field_metrics={}
    for f in fields:
        for rec in by_field.get(f.lower(),[]):
            if rec["requisite"]: field_metrics.setdefault(f,[]).append(rec["requisite"])
            if not name_recs and rec["comment"] and rec["comment"] not in logic: logic.append(rec["comment"])
            if rec["page"]: refs.add(rec["page"]+("#"+rec["anchor"] if rec["anchor"] else ""))
    field_metrics=sorted((f,list(dict.fromkeys(v))) for f,v in field_metrics.items())
    # 3) якщо точної назви немає — пробуємо метрику, що містить назву міри
    if not bname:
        for f,ms in field_metrics:
            hit=next((m for m in ms if tail.lower() in m.lower()),"")
            if hit: bname=hit; break
    return {"name":bname,"logic":logic[:5],"fieldMetrics":field_metrics,"refs":sorted(refs)}

# ---------------------------------------------------------------- report (PBIR report.json)
def _walk_measures(o, acc):
    """Рекурсивно збирає назви мір ("Measure":{...,"Property":"X"}) з конфігу візуала."""
    if isinstance(o, dict):
        mm=o.get("Measure")
        if isinstance(mm, dict) and "Property" in mm: acc.add(mm["Property"])
        for v in o.values(): _walk_measures(v, acc)
    elif isinstance(o, list):
        for v in o: _walk_measures(v, acc)

def page_kind(display):
    d=(display or "").strip(); du=d.upper(); dl=d.lower()
    if d in ("DEV","Test_new_features"): return "dev"
    if du.startswith(("TT:","ТТ:")) or dl.startswith(("підказка","підсказка")): return "tooltip"
    if "NAV" in du or "navigation" in dl or d=="Start Page": return "nav"
    if dl.startswith("деталізація"): return "drill"
    return "content"

def parse_report(path, mnames):
    """report.json -> впорядкований список сторінок [{display,kind,ordinal,visuals,measures[]}]."""
    if not os.path.exists(path): return []
    try: rep=json.load(open(path, encoding="utf-8"))
    except Exception: return []
    pages=[]
    for s in rep.get("sections", []):
        acc=set()
        for vc in s.get("visualContainers", []):
            for key in ("config","query","dataTransforms"):
                raw=vc.get(key)
                if not raw: continue
                try: _walk_measures(json.loads(raw), acc)
                except Exception: pass
        pages.append({"display":(s.get("displayName") or "").strip(),
                      "ordinal":s.get("ordinal"), "kind":page_kind(s.get("displayName")),
                      "visuals":len(s.get("visualContainers", [])),
                      "measures":sorted(m for m in acc if m in mnames)})
    pages.sort(key=lambda p:(p["ordinal"] if isinstance(p["ordinal"],int) else 999, p["display"]))
    return pages

# ---------------------------------------------------------------- mermaid / yaml helpers
def _mid(s):   return re.sub(r"\W","_",s) or "x"     # безпечний id вузла mermaid
def _mlabel(s):return (s or "").replace('"',"'")     # підпис вузла без лапок
def yq(s):     return '"'+(s or "").replace("\\","\\\\").replace('"','\\"')+'"'  # YAML double-quoted

# ---------------------------------------------------------------- text highlight / wiki links
def hl(text):
    """Підсвічує назви об'єктів (поля/таблиці/колонки) у тексті ТЗ як `code`."""
    text=(text or "").replace("<br>"," ").replace("|","/")
    text=re.sub(r"\[([^\]]+)\]", r"`\1`", text)                                  # [field] → code
    text=re.sub(r"(?<![`\w])([A-Za-z]+(?:_[A-Za-z0-9]+)+)(?![`\w])", r"`\1`", text)  # snake_case → code
    return text.strip()

AZ_ORG="MHPITDepProjects"; AZ_PROJECT="People Digital Profile (PDP)"; AZ_WIKI="PDP.wiki"
def ref_obj(ref, wiki_prefix):
    """Перетворює сирий шлях wiki на читабельний breadcrumb + клікабельне посилання Azure DevOps."""
    path=ref.split("#",1)[0]; anchor=ref.split("#",1)[1] if "#" in ref else ""
    label=" › ".join(s.replace("-"," ").strip() for s in path.split("/") if s)
    if anchor: label+=" › "+anchor.replace("-"," ")
    full="/".join(x for x in [wiki_prefix.strip("/"), path.strip("/")] if x)
    pagepath="/"+"/".join(s.replace("-"," ") for s in full.split("/") if s)
    url=(f"https://dev.azure.com/{AZ_ORG}/{urllib.parse.quote(AZ_PROJECT)}"
         f"/_wiki/wikis/{AZ_WIKI}?pagePath={urllib.parse.quote(pagepath)}")
    return {"label":label,"url":url,"path":path}

# ---------------------------------------------------------------- main
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pbip",default="/sessions/modest-charming-shannon/mnt/GIT_local")
    ap.add_argument("--sm",default="PDP.SemanticModel")
    ap.add_argument("--report",default="PDP.Report")
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
    # префікс шляху wiki (частина після 'PDP.wiki/') — щоб будувати посилання на ТЗ
    _wp=args.wiki.replace("\\","/"); _i=_wp.lower().find("pdp.wiki/")
    wiki_prefix=_wp[_i+len("pdp.wiki/"):].strip("/") if _i>=0 else ""

    # усі таблиці моделі як сутності
    entities={tn:parse_table(p) for tn,p in tmap.items()}
    rels=parse_relationships(os.path.join(defn,"relationships.tmdl"))
    rels_for=lambda tn:[r for r in rels if r["fromTable"]==tn or r["toTable"]==tn]

    # ---- звіт: сторінки та зіставлення міра -> сторінки ----
    report_pages=parse_report(os.path.join(args.pbip,args.report,"report.json"),mnames)
    rused=set(); doc_pages=[]
    for p in report_pages:
        if p["kind"] in ("content","tooltip") and p["measures"]:
            p["slug"]=uniq(slugify(p["display"]) or "page",rused); doc_pages.append(p)
    meas_pages={}  # name -> [(display, slug)]
    for p in doc_pages:
        for mn in p["measures"]:
            meas_pages.setdefault(mn,[]).append((p["display"],p["slug"]))

    OUT=args.out
    cat_m=os.path.join(OUT,"catalog","measures"); cat_e=os.path.join(OUT,"catalog","entities")
    doc_m=os.path.join(OUT,"docs","measures");    doc_e=os.path.join(OUT,"docs","entities")
    doc_r=os.path.join(OUT,"docs","report")
    for d in (cat_m,cat_e,doc_m,doc_e,doc_r): os.makedirs(d,exist_ok=True)
    def manual(path):
        if os.path.exists(path):
            try: return json.load(open(path,encoding="utf-8")).get("manualNotes","")
            except Exception: return ""
        return ""

    used=set(); index=[]; V={"no_business":[],"broken_dep":[],"orphan_cols":[],"no_wiki":[]}
    rel_meas={tn:[] for tn in entities}

    # ---- міри (двопрохідно: спершу залежності+зворотні зв'язки, далі запис) ----
    slug_m={}
    for m in measures: slug_m[m["name"]]=uniq(slugify(m["name"]),used)
    dep_cache={}            # name -> (columns, tables, used_measures)
    used_by={n:set() for n in mnames}   # name -> {міри, що її використовують}
    for m in measures:
        c,t,um=deps(m["dax"],mnames,tnames)
        dep_cache[m["name"]]=(c,t,um)
        for tn in t:
            if tn in rel_meas: rel_meas[tn].append(m["name"])
        for dep in um:
            if dep in used_by: used_by[dep].add(m["name"])
            else: V["broken_dep"].append(f"{m['name']} → {dep}")
    minfo={}               # name -> {slug, folder, fmt, bizdef} (для сторінок звіту)
    for m in measures:
        name=m["name"]; c,t,um=dep_cache[name]
        st=set()
        for tn in t:
            e=entities.get(tn)
            if e: st|=set(e["sourceTables"])
        biz=business_for(c,name,by_field,by_metric)
        req_refs=[ref_obj(r,wiki_prefix) for r in biz["refs"]]
        slug=slug_m[name]; jpath=os.path.join(cat_m,slug+".json")
        seg=[s for s in m["displayFolder"].split("\\") if s]
        rpages=meas_pages.get(name,[])
        obj={"id":slug,"type":"measure","name":name,"homeTable":"_Measures",
          "displayFolder":m["displayFolder"],"formatString":m["formatString"],
          "dataType":m["dataType"],"isHidden":m["isHidden"],"description":"",
          "dax":m["dax"],
          "reportPages":[{"display":d,"slug":s} for d,s in rpages],
          "dependencies":{"measures":um,"columns":c,"tables":t},
          "usedBy":sorted(used_by.get(name,[])),
          "lineage":{"sourceTables":sorted(st),
                     "sourceColumns":sorted({x.split('[',1)[1][:-1] for x in c}),
                     "powerQuery":(entities[t[0]]["powerQuery"] if t else "")},
          "business":{"name":biz["name"],"logic":biz["logic"],
                      "fieldMetrics":biz["fieldMetrics"],"requirementRefs":req_refs},
          "tags":sorted(set([slugify(s) for s in seg]+["pdp"])),
          "source":{"repo":"PDP","file":f"{args.sm}/definition/tables/_Measures.tmdl",
                    "commit":commit,"extractedAt":now},
          "manualNotes":manual(jpath)}
        json.dump(obj,open(jpath,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
        index.append({"id":slug,"type":"measure","name":name,
                      "displayFolder":m["displayFolder"],"file":f"measures/{slug}.md"})
        bizshort=biz["name"] or (biz["logic"][0] if biz["logic"] else "")
        minfo[name]={"slug":slug,"folder":m["displayFolder"],"fmt":m["formatString"],"bizdef":bizshort}
        if not (biz["name"] or biz["logic"] or biz["fieldMetrics"]): V["no_business"].append(name)
        if not biz["refs"]: V["no_wiki"].append(name)
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
    # ---- сторінки звіту (першочергово) ----
    write_report_index(os.path.join(doc_r,"index.md"),report_pages,doc_pages)
    for p in doc_pages:
        write_report_page(os.path.join(doc_r,p["slug"]+".md"),p,minfo)
    write_measures_index(os.path.join(doc_m,"index.md"),measures,slug_m,minfo)
    write_entities_index(os.path.join(doc_e,"index.md"),entities,slug_e)
    write_model(os.path.join(OUT,"docs","model.md"),entities,rels,slug_e)
    write_glossary(os.path.join(OUT,"docs","glossary.md"))
    write_index(os.path.join(OUT,"docs","index.md"),measures,entities,doc_pages)
    write_validation(os.path.join(OUT,"docs","validation.md"),V,len(measures))
    append_changelog(os.path.join(OUT,"docs","changelog.md"),now,len(measures),len(entities),commit)
    write_mkdocs_yml(os.path.join(OUT,"mkdocs.yml"),doc_pages,measures,slug_m,entities,slug_e)
    state={"pbip":{"commit":commit,"extractedAt":now,"measures":len(measures),"entities":len(entities),
                   "wiki_fields_indexed":len(by_field)}}
    json.dump(state,open(os.path.join(OUT,".cowork","state.json"),"w",encoding="utf-8"),
              ensure_ascii=False,indent=2)
    cov=len(measures)-len(V["no_business"])
    on_report=len(set().union(*[set(p["measures"]) for p in doc_pages])) if doc_pages else 0
    print(f"OK: {len(measures)} measures, {len(entities)} entities, business={cov}/{len(measures)}, "
          f"report_pages={len(doc_pages)} (measures_on_report={on_report}), wiki_fields={len(by_field)}, commit={commit[:8]}")

# ---------------------------------------------------------------- MD writers
def ptable(rows):
    return "\n".join(["| Властивість | Значення |","|---|---|"]+[f"| {k} | {v} |" for k,v in rows])

def write_measure_md(path,o,sm):
    b=o["business"]; dm=o["dependencies"]["measures"]; dt=o["dependencies"]["tables"]
    dc=o["dependencies"]["columns"]; ub=o.get("usedBy",[]); rp=o.get("reportPages",[]); lin=o["lineage"]
    def mlink(n): return f"[{n}](../measures/{sm[n]}.md)" if n in sm else f"`{n}`"
    L=[f"# {o['name']}",""]
    sub=[]
    if o["displayFolder"]: sub.append(f"тека `{o['displayFolder']}`")
    if o["formatString"]: sub.append(f"формат `{o['formatString']}`")
    if sub: L+=["*"+" · ".join(sub)+"*",""]
    # 1) технічний опис — першочергово (властивості → DAX → джерела даних → залежності → схема)
    L+=["## Технічний опис",""]
    L.append(ptable([("Тип","міра"),("Home table",o["homeTable"]),
        ("displayFolder",f"`{o['displayFolder']}`" if o['displayFolder'] else "—"),
        ("formatString",f"`{o['formatString']}`" if o['formatString'] else "—"),
        ("dataType",o["dataType"] or "—"),("Прихована","так" if o["isHidden"] else "ні")]))
    L+=["","### DAX","","```dax",o["dax"] or "—","```",""]
    L+=["### Джерела даних",""]
    if lin["sourceTables"]: L.append("Вихідні таблиці: "+", ".join(f"`{t}`" for t in lin["sourceTables"]))
    if lin["sourceColumns"]: L+=["", "Колонки: "+", ".join(f"`{c}`" for c in lin["sourceColumns"])]
    if lin["powerQuery"]: L+=["", f"Power Query: `{lin['powerQuery']}`"]
    if not (lin["sourceTables"] or lin["sourceColumns"]): L.append("—")
    L+=["","### Залежності (таблиці й колонки)",""]
    if dt: L+=["Таблиці: "+", ".join(f"`{t}`" for t in dt),""]
    if dc: L.append("Колонки: "+", ".join(f"`{c}`" for c in dc))
    if not dt and not dc: L.append("—")
    L+=["","### Схема","","```mermaid","graph LR",f'  M["{_mlabel(o["name"])}"]']
    for t in dt: L.append(f'  M --> {_mid(t)}["{_mlabel(t)}"]')
    L+=["```",""]
    # 2) бізнес-суть із ТЗ: назва → опис(логіка) → мапа полів → вимоги
    L+=["---","","## Бізнес-суть",""]
    has=bool(b.get("name") or b.get("logic") or b.get("fieldMetrics"))
    if b.get("name"): L+=[f"**Бізнес-назва:** {b['name']}",""]
    if b.get("logic"):
        L+=["### Опис із ТЗ",""]
        for cmt in b["logic"]: L+=[hl(cmt),""]
    if b.get("fieldMetrics"):
        total=sum(len(ms) for _,ms in b["fieldMetrics"])
        L+=[f'??? note "Поля-джерела та пов\'язані бізнес-метрики ({total})"',
            "    | Поле | Бізнес-метрики |","    |---|---|"]
        for f,ms in b["fieldMetrics"]:
            more=(f" … +{len(ms)-20}" if len(ms)>20 else "")
            cell=" · ".join(x.replace("|","/") for x in ms[:20])+more
            L.append(f"    | `{f}` | {cell} |")
        L+=[""]
    if b.get("requirementRefs"):
        L+=["**Вимоги (ТЗ):**",""]
        for r in b["requirementRefs"][:15]: L.append(f"- [{r['label']}]({r['url']})")
        if len(b["requirementRefs"])>15: L.append(f"- … ще {len(b['requirementRefs'])-15}")
        L+=[""]
    if not has and not b.get("requirementRefs"):
        L+=['!!! note "Бізнес-визначення відсутнє"',
            "    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.",""]
    # 3) де у звіті
    L+=["## На сторінках звіту",""]
    if rp:
        L.append(" · ".join(f"[{p['display']}](../report/{p['slug']}.md)" for p in rp))
    else:
        L.append("_Не використовується на основних сторінках звіту._")
    L+=[""]
    # 4) пов'язані міри — двосторонні переходи
    L+=["## Пов'язані міри",""]
    if dm: L+=["**Використовує:** "+", ".join(mlink(n) for n in dm),""]
    if ub:
        more=(f" … (+{len(ub)-40})" if len(ub)>40 else "")
        L+=["**Використовується в:** "+", ".join(mlink(n) for n in ub[:40])+more,""]
    if not dm and not ub: L+=["_Прямих зв'язків з іншими мірами немає._",""]
    # нотатки
    L+=["## Нотатки","",o["manualNotes"] if o["manualNotes"] else "_порожньо_"]
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

def write_measures_index(path,measures,sm,minfo=None):
    minfo=minfo or {}
    esc=lambda s:(s or "").replace("|","\\|").replace("\n"," ")
    groups={}
    for m in measures: groups.setdefault(m["displayFolder"] or "(без теки)",[]).append(m)
    L=["# Каталог мір","",f"Усього: **{len(measures)}** мір за {len(groups)} теками. "
       "Для перегляду за сторінками звіту див. [Звіт](../report/index.md).",""]
    for df in sorted(groups):
        L+=[f"## {df}","","| Міра | Формат | Бізнес-суть |","|---|---|---|"]
        for m in sorted(groups[df],key=lambda x:x["name"]):
            bd=esc((minfo.get(m["name"],{}) or {}).get("bizdef",""))
            if len(bd)>140: bd=bd[:137]+"…"
            fmt=f"`{m['formatString']}`" if m['formatString'] else "—"
            L.append(f"| [{esc(m['name'])}](./{sm[m['name']]}.md) | {fmt} | {bd or '—'} |")
        L.append("")
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_entities_index(path,entities,se):
    L=["# Бізнес-сутності",f"","Усього: **{len(entities)}**.","","| Таблиця | Джерела |","|---|---|"]
    for tn,e in sorted(entities.items()):
        L.append(f"| [{tn}](./{se[tn]}.md) | {', '.join('`'+t+'`' for t in e['sourceTables']) or '—'} |")
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_model(path,entities,rels,slug_e):
    # Замість однієї велетенської ER-схеми (≈145 зв'язків, нечитабельно) — по одній
    # зірковій схемі на кожну фактову таблицю + перелік конформованих вимірів.
    # mermaid id вузла: [A-Za-z0-9_]; імена з пробілом/крапкою інакше не рендеряться.
    nid=lambda s: re.sub(r"\W","_",s) or "x"
    names=set(entities)
    rels=[r for r in rels if r["fromTable"] in names and r["toTable"] in names]
    is_fact=lambda t: t.lower().startswith("fact")
    is_dim =lambda t: t.lower().startswith("dim")
    facts=sorted({t for t in names if is_fact(t)})
    elink=lambda t: f"[`{t}`](entities/{slug_e[t]}.md)" if t in slug_e else f"`{t}`"
    edge=lambda r: f'  {nid(r["toTable"])} ||--o{{ {nid(r["fromTable"])} : "{r["fromColumn"]}"'
    # зв'язки, що торкаються кожного факту; і ті, що між не-фактами
    by_fact={f:[] for f in facts}; other=[]
    for r in rels:
        hit=False
        if r["fromTable"] in by_fact: by_fact[r["fromTable"]].append(r); hit=True
        if r["toTable"] in by_fact and r["toTable"]!=r["fromTable"]: by_fact[r["toTable"]].append(r); hit=True
        if not hit: other.append(r)
    # конформовані виміри: у скількох фактах використовується кожен вимір
    dim_facts={}
    for r in rels:
        ft,tt=r["fromTable"],r["toTable"]
        if is_dim(tt) and is_fact(ft): dim_facts.setdefault(tt,set()).add(ft)
        if is_dim(ft) and is_fact(tt): dim_facts.setdefault(ft,set()).add(tt)
    L=["# Схема моделі","",
       f"Модель — це **схема-сузір'я**: **{len(facts)}** фактових таблиць, пов'язаних із вимірами "
       f"через **{len(rels)}** зв'язків (many → one). Щоб не зливати все в одну нечитабельну "
       "діаграму, нижче наведено окрему **зіркову схему на кожну фактову таблицю**.",""]
    conf=sorted(((len(fs),d) for d,fs in dim_facts.items()),key=lambda x:(-x[0],x[1]))
    if conf:
        L+=["## Конформовані виміри","",
            "Виміри, спільні для кількох фактів (число — у скількох фактах використовується). "
            "Натисніть на таблицю, щоб відкрити її опис.","",
            "| Вимір | Фактів |","|---|---|"]
        L+=[f"| {elink(d)} | {cnt} |" for cnt,d in conf]
        L+=[""]
    L+=["## Зіркові схеми за фактами","",
        "У кожній схемі фактова таблиця у центрі, навколо — її виміри; підпис на зв'язку — ключ з'єднання.",""]
    for f in facts:
        frs=sorted({(r["toTable"],r["fromTable"],r["fromColumn"]) for r in by_fact.get(f,[])})
        L+=[f"### {f}","",elink(f),""]
        if not frs:
            L+=["_Без зв'язків у моделі._",""]; continue
        L+=["```mermaid","erDiagram"]
        L+=[f'  {nid(tt)} ||--o{{ {nid(ft)} : "{col}"' for tt,ft,col in frs]
        L+=["```",""]
    if other:
        L+=["## Інші зв'язки (між вимірами)","","```mermaid","erDiagram"]
        L+=[edge(r) for r in other]
        L+=["```",""]
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

def write_index(path,measures,entities,doc_pages):
    npages=len(doc_pages)
    on_report=len(set().union(*[set(p["measures"]) for p in doc_pages])) if doc_pages else 0
    def card(icon,title,body,link,label):
        return [f"-   {icon}{{ .lg .middle }} **{title}**","","    ---","",f"    {body}","",
                f"    [:octicons-arrow-right-24: {label}]({link})",""]
    L=["# People Digital Profile","",
       "Документація семантичної моделі Power BI **People Digital Profile**, організована "
       "**навколо звіту**: метрики згруповано за сторінками звіту, з бізнес-суттю та переходами "
       "між пов'язаними мірами.","",
       '<div class="grid cards" markdown>',""]
    L+=card(":material-file-chart:","Звіт за сторінками",
            f"{npages} сторінок звіту · {on_report} мір з контекстом.","report/index.md","До звіту")
    L+=card(":material-table:","Каталог мір",
            f"Повний перелік усіх {len(measures)} мір за теками.","measures/index.md","Каталог мір")
    L+=card(":material-database:","Бізнес-сутності",
            f"{len(entities)} таблиць моделі: колонки, зв'язки, джерела.","entities/index.md","Сутності")
    L+=card(":material-sitemap:","Модель даних","Схема зв'язків таблиць (ER-діаграма).","model.md","Модель")
    L+=["</div>","",
        "## Як користуватися","",
        "- **Звіт** — почніть звідси: оберіть сторінку звіту й побачите її метрики з описом.",
        "- **Пошук** (угорі) — миттєвий пошук за назвою міри, таблиці чи бізнес-терміном.",
        "- На сторінці міри спершу **бізнес-суть** і **де у звіті**, далі **пов'язані міри**, "
        "потім технічний опис (DAX, джерела).","",
        "Додатково: [Глосарій](glossary.md) · [Якість і валідація](validation.md) · "
        "[Журнал змін](changelog.md)"]
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_report_index(path,pages,doc_pages):
    KL={"content":"основна","tooltip":"тултіп"}
    esc=lambda s:(s or "").replace("|","\\|")
    L=["# Звіт People Digital Profile","",
       "Документацію організовано **за сторінками звіту**. Оберіть сторінку, щоб побачити її "
       "метрики з бізнес-суттю та переходами до деталей кожної міри.",""]
    def section(title,kinds):
        rows=[p for p in doc_pages if p["kind"] in kinds]
        if not rows: return []
        out=[f"## {title}","","| Сторінка | Мір | Тип |","|---|---|---|"]
        for p in rows:
            out.append(f"| [{esc(p['display'])}]({p['slug']}.md) | {len(p['measures'])} | {KL.get(p['kind'],p['kind'])} |")
        return out+[""]
    L+=section("Основні сторінки",("content",))
    L+=section("Тултіпи та підказки",("tooltip",))
    others=[p for p in pages if "slug" not in p and p.get("display")]
    if others:
        L+=["## Службові сторінки","",
            "Навігаційні, деталізаційні та технічні сторінки — без окремої деталізації мір:","",
            ", ".join(f"{esc(p['display'])} ({len(p['measures'])})" for p in others),""]
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

def write_report_page(path,p,minfo):
    KL={"content":"Основна сторінка звіту","tooltip":"Тултіп / підказка"}
    esc=lambda s:(s or "").replace("|","\\|").replace("\n"," ")
    L=[f"# {p['display']}","",
       '!!! info "Сторінка звіту"',
       f"    Тип: **{KL.get(p['kind'],'сторінка')}** · мір на сторінці: **{len(p['measures'])}**","",
       "[:octicons-arrow-left-24: Усі сторінки звіту](index.md)",""]
    groups={}
    for mn in p["measures"]:
        info=minfo.get(mn)
        if not info: continue
        groups.setdefault(info["folder"] or "(без теки)",[]).append((mn,info))
    if not groups: L.append("_Немає задокументованих мір._")
    for folder in sorted(groups):
        L+=[f"## {folder}","","| Міра | Формат | Бізнес-суть |","|---|---|---|"]
        for mn,info in sorted(groups[folder],key=lambda x:x[0]):
            bd=esc(info["bizdef"]) if info["bizdef"] else "—"
            if len(bd)>160: bd=bd[:157]+"…"
            fmt=f"`{info['fmt']}`" if info["fmt"] else "—"
            L.append(f"| [{esc(mn)}](../measures/{info['slug']}.md) | {fmt} | {bd} |")
        L.append("")
    open(path,"w",encoding="utf-8").write("\n".join(L)+"\n")

MKDOCS_HEAD='''site_name: People Digital Profile — документація моделі
site_url: https://nevsky-bi-user.github.io/pdp-docs/
site_description: Документація семантичної моделі Power BI People Digital Profile — метрики за сторінками звіту, бізнес-суть, залежності.
repo_url: https://github.com/Nevsky-BI-user/pdp-docs
repo_name: Nevsky-BI-user/pdp-docs
theme:
  name: material
  language: uk
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: teal
      accent: teal
      toggle:
        icon: material/weather-night
        name: Темна тема
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: teal
      accent: teal
      toggle:
        icon: material/weather-sunny
        name: Світла тема
  font:
    text: Inter
    code: JetBrains Mono
  icon:
    repo: fontawesome/brands/github
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.indexes
    - navigation.top
    - navigation.tracking
    - navigation.instant
    - navigation.instant.progress
    - toc.follow
    - search.suggest
    - search.highlight
    - search.share
    - content.code.copy
    - content.tooltips
    - navigation.footer
plugins:
  - search
markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true
  - pymdownx.highlight
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
'''

def write_mkdocs_yml(path,doc_pages,measures,slug_m,entities,slug_e):
    content=[p for p in doc_pages if p["kind"]=="content"]
    tips=[p for p in doc_pages if p["kind"]=="tooltip"]
    nav=["nav:","  - Головна: index.md","  - Звіт:","      - Огляд звіту: report/index.md"]
    for p in content: nav.append(f"      - {yq(p['display'])}: report/{p['slug']}.md")
    if tips:
        nav.append("      - Тултіпи та підказки:")
        for p in tips: nav.append(f"          - {yq(p['display'])}: report/{p['slug']}.md")
    nav.append("  - Каталог мір: measures/index.md")
    nav.append("  - Бізнес-сутності:")
    nav.append("      - Усі сутності: entities/index.md")
    for tn in sorted(entities): nav.append(f"      - {yq(tn)}: entities/{slug_e[tn]}.md")
    nav+=["  - Модель даних: model.md","  - Глосарій: glossary.md",
          "  - Якість і валідація: validation.md","  - Журнал змін: changelog.md"]
    body=MKDOCS_HEAD+"\n".join(nav)+"\n\nnot_in_nav: |\n  measures/*.md\n"
    open(path,"w",encoding="utf-8").write(body)

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
