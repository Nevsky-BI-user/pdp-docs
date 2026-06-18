# HANDOFF для Claude Code — pdp-docs

Інструкція з продовження роботи над сайтом-документацією PDP. Виконувати на машині користувача (Windows, git + Python працюють локально).

## Контекст

`pdp-docs` — самооновлюваний сайт-документація семантичної моделі Power BI **People Digital Profile**. Три форми з єдиного джерела: `catalog/*.json` (істина) → `docs/*.md` → сайт MkDocs Material.

Джерела (read-only):
- PBIP-модель: `C:\PROJECTS\MHP\PDP\GIT_local` (`PDP.SemanticModel`, TMDL).
- Wiki вимог: `C:\github\azure-wiki\PDP.wiki\Функціональні-вимоги\Вимоги-до-звіту-People-Digital-Profile`.

## Поточний стан (зроблено)

- Згенеровано **729 мір** і **59 сутностей**: `catalog/measures`, `catalog/entities`, `docs/measures`, `docs/entities`, індекси, `model.md`, `glossary.md`, `validation.md`, `changelog.md`.
- Генератор `.cowork/generate.py` — парсинг TMDL (DAX, залежності, lineage) + індекс wiki «Таблиць джерел даних» (480 полів). Бізнес-суть — **цитати з wiki**, не вигадки.
- Бізнес-визначення: **528/729** мір (решта — SVG/навігація/технічні/складені без прямого метрика-поля; зафіксовано у `docs/validation.md`).
- `mkdocs build --strict` — чистий. Верифікація: DAX звірено з TMDL, крос-посилання без обірваних.
- Допоміжне: `mkdocs.yml`, `requirements.txt` (mkdocs-material==9.7.6), `.cowork/sources.json`, `.cowork/state.json`, `.cowork/publish.sh`, `.cowork/update.sh`, `README.md`.

**Важливо:** повноцінний git-репозиторій було зібрано в ізольованій пісочниці (її mount забороняє unlink/rename, тож git там неможливий). У `C:\github\pdp-docs` лежить **дзеркало файлів** і **бита `.git`** від невдалої спроби. На вашій машині git працює нормально.

## Завдання A — розгортання (пріоритет)

1. Прибрати биту `.git` і переініціалізувати:
   ```powershell
   Remove-Item -Recurse -Force C:\github\pdp-docs\.git
   ```
   ```bash
   cd /c/github/pdp-docs
   git init -b main
   git add -A
   git -c user.email=you@local -c user.name=you commit -m "feat: pdp-docs — 729 мір, 59 сутностей"
   ```
2. Залежності + контроль збірки:
   ```bash
   pip install -r requirements.txt
   mkdocs build --strict
   ```
3. Створити приватний GitHub-репо і запушити (через `gh` або вручну):
   ```bash
   gh repo create <owner>/pdp-docs --private --source . --remote origin --push
   ```
   або готовим скриптом (створить репо через REST API, push, gh-deploy):
   ```bash
   GH_USER=<owner> GH_TOKEN=<pat> bash .cowork/publish.sh
   ```
4. Опублікувати сайт і ввімкнути Pages:
   ```bash
   mkdocs gh-deploy --force
   ```
   GitHub → Settings → Pages → Deploy from a branch → `gh-pages` / `(root)`. Перевірити, що сайт відкривається і працює пошук.

## Завдання B — відтворюваність генерації на машині

`generate.py` має дефолтні шляхи з пісочниці (`/sessions/...`). На машині запускати з явними аргументами:
```bash
python .cowork/generate.py \
  --pbip "C:/PROJECTS/MHP/PDP/GIT_local" \
  --wiki "C:/github/azure-wiki/PDP.wiki/Функціональні-вимоги/Вимоги-до-звіту-People-Digital-Profile" \
  --out  "C:/github/pdp-docs"
```
Очікувано: `OK: 729 measures, 59 entities, business=528/729 …`. Рекомендація: винести ці шляхи у `sources.json` і читати їх у `main()` замість хардкоду дефолтів.

## Завдання C — щоденне автооновлення

`.cowork/update.sh` робить повний цикл: `git pull` джерел → `generate.py` → `mkdocs build --strict` → commit → push → `gh-deploy`. Перевірити в ньому шляхи (`PBIP_WIN`, `WIKI`, `DOCS`) і зареєструвати в Task Scheduler:
```bat
schtasks /Create /TN pdp-docs-update /SC DAILY /ST 07:00 ^
 /TR "\"C:\Program Files\Git\bin\bash.exe\" -lc 'GH_USER=<owner> GH_TOKEN=<pat> bash /c/github/pdp-docs/.cowork/update.sh >> /c/github/pdp-docs/.cowork/update.log 2>&1'"
```
Токен зберігати у змінних середовища машини або Credential Manager, не в тексті задачі. Перевірити ідемпотентність: повторний запуск без змін у джерелах не повинен плодити порожні коміти (у скрипті вже `commit || echo no changes`).

## Завдання D — доопрацювання якості (за наявності часу)

1. **Бізнес-покриття (201 міра без визначення).** Підходи, у порядку віддачі:
   - Розширити wiki-індекс: окрім «Таблиць джерел даних», парсити текстові розділи (напр. `Сторінка-Результативність-та-оцінка.md` має описи блоків) і зіставляти за назвою міри/ключовими словами.
   - Для SVG/складених мір — зіставляти за **мірами-залежностями** (успадковувати business від базової міри, на яку посилається SVG).
   - Ручні правки — у поле `manualNotes` JSON (зберігається між регенераціями; розділ `## Нотатки` будується з нього).
   - Явні відповідності — у `sources.json` → `mapping`.
2. **Сутності.** `definition` порожній. Додати опис таблиць (з wiki за фактовою таблицею `DM.*`) і, за потреби, requirementRefs з тексту.
3. **requirementRefs → клікабельні.** Зараз це текстові шляхи сторінок wiki. Конвертувати в Azure DevOps URL (потрібен базовий URL організації/проєкту wiki).
4. **erDiagram у `model.md`.** Імена таблиць із пробілом/крапкою (`t_AC Burnout`, `p_AC.Loss_Productivity`) у mermaid `erDiagram` потребують санітизації (замінити `\W`→`_`), інакше відповідні вузли не рендеряться. DAX/каталогу не стосується.

## Критерії завершення (DoD)

- Сайт відкривається на GitHub Pages, працює вбудований пошук.
- `mkdocs build --strict` без помилок.
- `git push` у `main` і `gh-pages` виконані; Pages = `gh-pages`/root.
- Task Scheduler запускає `update.sh` щодня; лог пишеться.
- (опц.) Бізнес-покриття зросло; `validation.md` відображає актуальні прогалини.

## Застереження

- Бізнес-суть **не вигадувати** — лише цитати з wiki або `manualNotes`.
- Кодування UTF-8; slug файлів — ASCII (транслітерація кирилиці в `generate.py`).
- Вхідні теки (PBIP, wiki) — **тільки читання**; запис лише в `pdp-docs`.
- Casing колонок у DAX/моделі зберігати точно (джерело — UPPER_SNAKE_CASE).
- Останній стан генерації — у `.cowork/state.json` (commit PBIP, лічильники).
