# pdp-docs — документація семантичної моделі PDP

Самооновлюваний сайт-документація Power BI-проєкту **People Digital Profile**.
Три узгоджені форми з єдиного джерела: JSON-каталог → Markdown → сайт MkDocs Material.

## Структура
- `catalog/` — структурне джерело істини (JSON), поза сайтом.
- `docs/` — вміст сайту (Markdown), `docs_dir` MkDocs.
- `.cowork/` — `sources.json`, `state.json`, `generate.py` (генератор), `publish.sh`.
- `mkdocs.yml` — конфіг сайту.

## Локально
```
pip install -r requirements.txt
python3 .cowork/generate.py        # TMDL → catalog/ → docs/
mkdocs serve                       # попередній перегляд
mkdocs build --strict              # валідація збірки
```

## Публікація
```
GH_USER=логін GH_TOKEN=ghp_xxx bash .cowork/publish.sh
```
Потім один раз: Settings → Pages → Deploy from a branch → `gh-pages` / root.

## Обсяг
Пілот: displayFolder `Personal_Profile\Результативність та оцінка\OKR` (27 мір, 5 сутностей).
