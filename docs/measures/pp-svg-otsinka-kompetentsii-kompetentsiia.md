# PP.SVG.Оцінка компетенцій.Компетенція

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | — |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _fontFamily = "Segoe UI"

-- ── Палітра ──
VAR _cSelf   = "#2547D0"   // Самооцінка
VAR _cExpert = "#9DBFF9"   // Експертна оцінка
VAR _cR360   = "#5B8DEF"   // Оцінка 360
VAR _tSelf   = "#D5E0FA"   // доріжка Самооцінки
VAR _tExpert = "#E8F1FE"   // доріжка Експертної оцінки
VAR _tR360   = "#DCE8FC"   // доріжка Оцінки 360
VAR _valColor  = "#1F2A44" // підпис значення
VAR _catColor  = "#3A4660" // підпис компетенції
VAR _legColor  = "#3A4660" // легенда
VAR _hdrColor  = "#1F2A44" // заголовок категорії (блоку)
VAR _panelFill = "#F5F7FB" // фон панелі блоку

-- ── Шкала ──
VAR _MaxValue = 5

-- ── Геометрія: бари / групи ──
VAR _BarWidth   = 18
VAR _BarGapIn   = 6
VAR _GroupWidth = (_BarWidth * 3) + (_BarGapIn * 2)   // 66
VAR _GroupGap   = 24                                   // між компетенціями в блоці
VAR _PanelPadX  = 10                                   // внутрішнє поле панелі
VAR _ColGap     = 14                                   // між колонками сітки

-- ── Геометрія: блок (зсуви від верху блоку) ──
VAR _TitleDY  = 14
VAR _ValueDY  = 30
VAR _BarTopDY = 36
VAR _BarH     = 56
VAR _CompDY1  = 104
VAR _CompDY2  = 115
VAR _BlockH   = 122
VAR _BlockGap = 8
VAR _BlockPitch = _BlockH + _BlockGap                 // 130
VAR _TopBand  = 30                                    // зона легенди + відступ до блоків
VAR _ValueFont = 8
VAR _CatFont   = 9

-- ── Дані: три міри по кожній компетенції ──
VAR _comp0 =
    SUMMARIZE('fact_360_Assessment', 'fact_360_Assessment'[Category_Name], 'fact_360_Assessment'[Competency_Name])
VAR _comp =
    ADDCOLUMNS(
        _comp0,
        "Self",   [PP.Оцінка компетенцій.Самооцінка],
        "Expert", [PP.Оцінка компетенцій.Експертна оцінка],
        "R360",   [PP.Оцінка компетенцій.Оцінка 360]
    )
VAR _compF =
    FILTER(
        _comp,
        NOT(ISBLANK([Self])) || NOT(ISBLANK([Expert])) || NOT(ISBLANK([R360]))
    )

-- ── Категорії: індекс блоку, к-сть компетенцій, ширина вмісту ──
VAR _catBase = SUMMARIZE(_compF, [Category_Name])
VAR _catA =
    ADDCOLUMNS(
        _catBase,
        "@catIdx", RANKX(_catBase, [Category_Name], , ASC, Dense),
        "@n", VAR _c = [Category_Name] RETURN COUNTROWS(FILTER(_compF, [Category_Name] = _c))
    )
VAR _catTbl =
    ADDCOLUMNS(
        _catA,
        "@cw", [@n] * _GroupWidth + ([@n] - 1) * _GroupGap
    )

-- ── Розміри сітки/полотна ──
VAR _maxCW = MAXX(_catTbl, [@cw])
VAR _ColW  = _maxCW + 2 * _PanelPadX                  // рівна ширина колонки
VAR _nCat  = COUNTROWS(_catTbl)
VAR _nRows = ROUNDUP(_nCat / 2, 0)                    // рядків у сітці (2 колонки)

-- ── Легенда (геометрія) ──
VAR _legStartX = 4
VAR _legW1 = 16 + LEN("Самооцінка") * 7
VAR _legW2 = 16 + LEN("Експертна оцінка") * 7
VAR _legW3 = 16 + LEN("Оцінка 360") * 7
VAR _legGap = 18
VAR _legX1 = _legStartX
VAR _legX2 = _legStartX + _legW1 + _legGap
VAR _legX3 = _legStartX + _legW1 + _legGap + _legW2 + _legGap
VAR _legendRight = _legX3 + _legW3
VAR _LegendY = 10

VAR _W = ROUND( MAX(2 * _ColW + _ColGap, _legendRight + 2), 0 )
VAR _H = _TopBand + _nRows * _BlockPitch - _BlockGap + 2

-- ── Легенда (розмітка) ──
VAR _Legend =
    "<circle cx='" & FORMAT(_legX1 + 5, "0.0", "en-US") & "' cy='" & _LegendY & "' r='5' fill='" & _cSelf & "'/>" &
    "<text x='" & FORMAT(_legX1 + 15, "0.0", "en-US") & "' y='" & (_LegendY + 4) & "' style='font-family:" & _fontFamily & "; font-size:12px; fill:" & _legColor & "; font-weight:600;'>Самооцінка</text>" &
    "<circle cx='" & FORMAT(_legX2 + 5, "0.0", "en-US") & "' cy='" & _LegendY & "' r='5' fill='" & _cExpert & "'/>" &
    "<text x='" & FORMAT(_legX2 + 15, "0.0", "en-US") & "' y='" & (_LegendY + 4) & "' style='font-family:" & _fontFamily & "; font-size:12px; fill:" & _legColor & "; font-weight:600;'>Експертна оцінка</text>" &
    "<circle cx='" & FORMAT(_legX3 + 5, "0.0", "en-US") & "' cy='" & _LegendY & "' r='5' fill='" & _cR360 & "'/>" &
    "<text x='" & FORMAT(_legX3 + 15, "0.0", "en-US") & "' y='" & (_LegendY + 4) & "' style='font-family:" & _fontFamily & "; font-size:12px; fill:" & _legColor & "; font-weight:600;'>Оцінка 360</text>"

-- ── Панелі блоків + заголовки категорій (сітка 2 колонки) ──
VAR _Blocks =
    CONCATENATEX(
        _catTbl,
        VAR _ci  = [@catIdx]
        VAR _cat = [Category_Name]
        VAR _col = MOD(_ci - 1, 2)
        VAR _row = QUOTIENT(_ci - 1, 2)
        VAR _px  = _col * (_ColW + _ColGap)
        VAR _py  = _TopBand + _row * _BlockPitch
        RETURN
            "<rect x='" & FORMAT(_px, "0.0", "en-US") & "' y='" & FORMAT(_py, "0.0", "en-US") & "' width='" & FORMAT(_ColW, "0.0", "en-US") & "' height='" & _BlockH & "' rx='10' fill='" & _panelFill & "'/>" &
            "<text x='" & FORMAT(_px + _PanelPadX, "0.0", "en-US") & "' y='" & FORMAT(_py + _TitleDY, "0.0", "en-US") & "' style='font-family:" & _fontFamily & "; font-size:12px; fill:" & _hdrColor & "; font-weight:700;'>" & SUBSTITUTE(_cat, "&", "&amp;") & "</text>",
        "",
        [@catIdx], ASC
    )

-- ── Групи барів усередині блоків ──
VAR _Cols =
    CONCATENATEX(
        ADDCOLUMNS(
            _compF,
            "@ci", VAR _c = [Category_Name] RETURN RANKX(_catBase, [Category_Name], , ASC, Dense),
            "@j",
                VAR _c = [Category_Name]
                VAR _nm = [Competency_Name]
                RETURN COUNTROWS(FILTER(_compF, [Category_Name] = _c && [Competency_Name] < _nm))
        ),
        VAR _cat = [Competency_Name]
        VAR _vSelf = [Self]
        VAR _vExpert = [Expert]
        VAR _vR360 = [R360]
        VAR _ci  = [@ci]
        VAR _c   = [Category_Name]
        VAR _n   = COUNTROWS(FILTER(_compF, [Category_Name] = _c))
        VAR _cw  = _n * _GroupWidth + (_n - 1) * _GroupGap
        VAR _col = MOD(_ci - 1, 2)
        VAR _row = QUOTIENT(_ci - 1, 2)
        VAR _px  = _col * (_ColW + _ColGap)
        VAR _py  = _TopBand + _row * _BlockPitch
        VAR _groupsStartX = _px + (_ColW - _cw) / 2            // центрування груп у колонці
        VAR _x   = _groupsStartX + [@j] * (_GroupWidth + _GroupGap)
        VAR _x1  = _x
        VAR _x2  = _x + _BarWidth + _BarGapIn
        VAR _x3  = _x + 2 * (_BarWidth + _BarGapIn)
        VAR _cxG = _x + _GroupWidth / 2
        VAR _barTop = _py + _BarTopDY
        VAR _barBot = _barTop + _BarH
        VAR _valueY = _py + _ValueDY
        VAR _compY1 = _py + _CompDY1
        VAR _compY2 = _py + _CompDY2

        VAR _hSelf = MIN(DIVIDE(_vSelf, _MaxValue, 0), 1) * _BarH
        VAR _ySelf = _barBot - _hSelf
        VAR _hExpert = MIN(DIVIDE(_vExpert, _MaxValue, 0), 1) * _BarH
        VAR _yExpert = _barBot - _hExpert
        VAR _hR360 = MIN(DIVIDE(_vR360, _MaxValue, 0), 1) * _BarH
        VAR _yR360 = _barBot - _hR360

        -- доріжки (прямокутні)
        VAR _tracks =
            "<rect x='" & FORMAT(_x1, "0.0", "en-US") & "' y='" & FORMAT(_barTop, "0.0", "en-US") & "' width='" & _BarWidth & "' height='" & _BarH & "' fill='" & _tSelf & "'/>" &
            "<rect x='" & FORMAT(_x2, "0.0", "en-US") & "' y='" & FORMAT(_barTop, "0.0", "en-US") & "' width='" & _BarWidth & "' height='" & _BarH & "' fill='" & _tExpert & "'/>" &
            "<rect x='" & FORMAT(_x3, "0.0", "en-US") & "' y='" & FORMAT(_barTop, "0.0", "en-US") & "' width='" & _BarWidth & "' height='" & _BarH & "' fill='" & _tR360 & "'/>"

        -- заливки (прямокутні, лише за наявності значення)
        VAR _fills =
            IF(ISBLANK(_vSelf), "", "<rect x='" & FORMAT(_x1, "0.0", "en-US") & "' y='" & FORMAT(_ySelf, "0.0", "en-US") & "' width='" & _BarWidth & "' height='" & FORMAT(_hSelf, "0.0", "en-US") & "' fill='" & _cSelf & "'/>") &
            IF(ISBLANK(_vExpert), "", "<rect x='" & FORMAT(_x2, "0.0", "en-US") & "' y='" & FORMAT(_yExpert, "0.0", "en-US") & "' width='" & _BarWidth & "' height='" & FORMAT(_hExpert, "0.0", "en-US") & "' fill='" & _cExpert & "'/>") &
            IF(ISBLANK(_vR360), "", "<rect x='" & FORMAT(_x3, "0.0", "en-US") & "' y='" & FORMAT(_yR360, "0.0", "en-US") & "' width='" & _BarWidth & "' height='" & FORMAT(_hR360, "0.0", "en-US") & "' fill='" & _cR360 & "'/>")

        -- підписи значень над барами
        VAR _vlabels =
            "<text x='" & FORMAT(_x1 + _BarWidth / 2, "0.0", "en-US") & "' y='" & FORMAT(_valueY, "0.0", "en-US") & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:" & _ValueFont & "px; fill:" & _valColor & "; font-weight:600;'>" & IF(ISBLANK(_vSelf), "", FORMAT(_vSelf, "0.00")) & "</text>" &
            "<text x='" & FORMAT(_x2 + _BarWidth / 2, "0.0", "en-US") & "' y='" & FORMAT(_valueY, "0.0", "en-US") & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:" & _ValueFont & "px; fill:" & _valColor & "; font-weight:600;'>" & IF(ISBLANK(_vExpert), "", FORMAT(_vExpert, "0.00")) & "</text>" &
            "<text x='" & FORMAT(_x3 + _BarWidth / 2, "0.0", "en-US") & "' y='" & FORMAT(_valueY, "0.0", "en-US") & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:" & _ValueFont & "px; fill:" & _valColor & "; font-weight:600;'>" & IF(ISBLANK(_vR360), "", FORMAT(_vR360, "0.00")) & "</text>"

        -- підпис компетенції (перенос за першим пробілом)
        VAR _spacePos = SEARCH(" ", _cat, 1, 0)
        VAR _catLine1 = IF(_spacePos > 0, LEFT(_cat, _spacePos - 1), _cat)
        VAR _catLine2 = IF(_spacePos > 0, MID(_cat, _spacePos + 1, 200), "")
        VAR _catLabel =
            "<text x='" & FORMAT(_cxG, "0.0", "en-US") & "' y='" & FORMAT(_compY1, "0.0", "en-US") & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:" & _CatFont & "px; fill:" & _catColor & "; font-weight:600;'>" & SUBSTITUTE(_catLine1, "&", "&amp;") & "</text>" &
            IF(_catLine2 = "", "", "<text x='" & FORMAT(_cxG, "0.0", "en-US") & "' y='" & FORMAT(_compY2, "0.0", "en-US") & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:" & _CatFont & "px; fill:" & _catColor & "; font-weight:600;'>" & SUBSTITUTE(_catLine2, "&", "&amp;") & "</text>")

        RETURN _tracks & _fills & _vlabels & _catLabel,
        "",
        [@ci], ASC, [@j], ASC
    )

RETURN
"<svg xmlns='http://www.w3.org/2000/svg' width='100%' height='100%' viewBox='0 0 " & FORMAT(_W, "0") & " " & FORMAT(_H, "0") & "' preserveAspectRatio='xMidYMid meet'>"
& _Blocks
& _Cols
& _Legend
& "</svg>"
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_360_Assessment`

Колонки: `Category_Name`, `Competency_Name`

Power Query: `fact_360_Assessment`

### Залежності (таблиці й колонки)

Таблиці: `fact_360_Assessment`

Колонки: `fact_360_Assessment[Category_Name]`, `fact_360_Assessment[Competency_Name]`

### Схема

```mermaid
graph LR
  M["PP.SVG.Оцінка компетенцій.Компетенція"]
  M --> fact_360_Assessment["fact_360_Assessment"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Результативність та оцінка › Оцінка компет.Детально

## Пов'язані міри

**Використовує:** [PP.Оцінка компетенцій.Експертна оцінка](../measures/pp-otsinka-kompetentsii-ekspertna-otsinka.md), [PP.Оцінка компетенцій.Оцінка 360](../measures/pp-otsinka-kompetentsii-otsinka-360.md), [PP.Оцінка компетенцій.Самооцінка](../measures/pp-otsinka-kompetentsii-samootsinka.md)

## Нотатки

_порожньо_
