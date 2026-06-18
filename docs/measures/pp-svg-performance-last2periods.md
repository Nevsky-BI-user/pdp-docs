# PP.SVG.Performance.Last2Periods

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Результативність` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _fontFamily = "Segoe UI"

-- Значення для барів
VAR _prev_val  = [PP.Оцінка результативності попередній рік]
VAR _last_val  = [PP.Оцінка результативності поточний рік]

-- Підписи років для осі X
VAR _prev_year = AVERAGE('fact_Burnout_Indicators'[PREV_YEAR_PERFORMANCE])
VAR _last_year = AVERAGE('fact_Burnout_Indicators'[LAST_YEAR_PERFORMANCE])

VAR _PrevHas = NOT ISBLANK(_prev_val)
VAR _LastHas = NOT ISBLANK(_last_val)
VAR _BarCount = IF(_PrevHas, 1, 0) + IF(_LastHas, 1, 0)

-- Геометрія
VAR _MaxValue = 5
VAR _W = 100
VAR _H = 80
VAR _BarWidth = 14
VAR _Rx = _BarWidth / 2
VAR _ValueY = 7
VAR _ClassY = 14
VAR _BarTop = 19
VAR _BarBot = 67
VAR _BarMaxH = _BarBot - _BarTop
VAR _YearY = 76

-- Центри барів за x
VAR _CxPrev =
    SWITCH(
        TRUE(),
        _PrevHas && _LastHas, 30,
        _PrevHas, 50,
        BLANK()
    )
VAR _CxLast =
    SWITCH(
        TRUE(),
        _PrevHas && _LastHas, 70,
        _LastHas, 50,
        BLANK()
    )

-- Колір/клас prev
VAR _FillPrev =
    SWITCH(
        TRUE(),
        _prev_val < 3,     "#9e241e",
        _prev_val <= 3.39, "#a5a4a6",
        _prev_val <= 3.89, "#e9c246",
        _prev_val <= 4.29, "#5a974d",
        _prev_val <= 5.00, "#8bd6ea",
        "#a5a4a6"
    )
VAR _ClsPrev =
    SWITCH(
        TRUE(),
        _prev_val < 3,     "D",
        _prev_val <= 3.39, "C",
        _prev_val <= 3.89, "B",
        _prev_val <= 4.29, "A",
        _prev_val <= 5.00, "TOP A"
    )
VAR _HPrev  = MIN(DIVIDE(_prev_val, _MaxValue, 0), 1) * _BarMaxH
VAR _YPrev  = _BarBot - _HPrev
VAR _BxPrev = _CxPrev - _Rx

-- Колір/клас last
VAR _FillLast =
    SWITCH(
        TRUE(),
        _last_val < 3,     "#9e241e",
        _last_val <= 3.39, "#a5a4a6",
        _last_val <= 3.89, "#e9c246",
        _last_val <= 4.29, "#5a974d",
        _last_val <= 5.00, "#8bd6ea",
        "#a5a4a6"
    )
VAR _ClsLast =
    SWITCH(
        TRUE(),
        _last_val < 3,     "D",
        _last_val <= 3.39, "C",
        _last_val <= 3.89, "B",
        _last_val <= 4.29, "A",
        _last_val <= 5.00, "TOP A"
    )
VAR _HLast  = MIN(DIVIDE(_last_val, _MaxValue, 0), 1) * _BarMaxH
VAR _YLast  = _BarBot - _HLast
VAR _BxLast = _CxLast - _Rx

-- Колонка prev
VAR _ColPrev =
    IF(
        _PrevHas,
        "<text x='" & _CxPrev & "' y='" & _ValueY & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:6px; fill:" & _FillPrev & "; font-weight:700;'>" &
            SUBSTITUTE(FORMAT(_prev_val, "0.00"), ".", ",") &
        "</text>" &
        "<text x='" & _CxPrev & "' y='" & _ClassY & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:4.5px; fill:" & _FillPrev & "; font-weight:600; letter-spacing:0.2px;'>" &
            _ClsPrev &
        "</text>" &
        "<rect x='" & FORMAT(_BxPrev, "0.0") & "' y='" & FORMAT(_YPrev, "0.0") & "' width='" & FORMAT(_BarWidth, "0.0") & "' height='" & FORMAT(_HPrev, "0.0") & "' rx='" & FORMAT(_Rx, "0.0") & "' fill='" & _FillPrev & "'/>" &
        "<text x='" & _CxPrev & "' y='" & _YearY & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:4.5px; fill:#94A3B8; font-weight:500;'>" &
            FORMAT(_prev_year, "0") &
        "</text>",
        ""
    )

-- Колонка last
VAR _ColLast =
    IF(
        _LastHas,
        "<text x='" & _CxLast & "' y='" & _ValueY & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:6px; fill:" & _FillLast & "; font-weight:700;'>" &
            SUBSTITUTE(FORMAT(_last_val, "0.00"), ".", ",") &
        "</text>" &
        "<text x='" & _CxLast & "' y='" & _ClassY & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:4.5px; fill:" & _FillLast & "; font-weight:600; letter-spacing:0.2px;'>" &
            _ClsLast &
        "</text>" &
        "<rect x='" & FORMAT(_BxLast, "0.0") & "' y='" & FORMAT(_YLast, "0.0") & "' width='" & FORMAT(_BarWidth, "0.0") & "' height='" & FORMAT(_HLast, "0.0") & "' rx='" & FORMAT(_Rx, "0.0") & "' fill='" & _FillLast & "'/>" &
        "<text x='" & _CxLast & "' y='" & _YearY & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:4.5px; fill:#94A3B8; font-weight:500;'>" &
            FORMAT(_last_year, "0") &
        "</text>",
        ""
    )

VAR _Empty =
    "<text x='" & _W/2 & "' y='" & _H/2 & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:11px; fill:#A0AEC0; font-style:italic;'>Дані відсутні</text>"

VAR _Body = IF(_BarCount = 0, _Empty, _ColPrev & _ColLast)

VAR _SVG =
    "<div style='width:100%;height:100%;overflow:hidden;display:flex;align-items:center;justify-content:center;'><svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 " & _W & " " & _H & "' preserveAspectRatio='xMidYMid meet' overflow='hidden' style='display:block; max-width:100%; max-height:100%; overflow:hidden;'>" &
        _Body &
    "</svg></div>"

RETURN _SVG
```

## Джерела


Колонки: `LAST_YEAR_PERFORMANCE`, `PREV_YEAR_PERFORMANCE`

Power Query: `fact_Burnout_Indicators`

## Бізнес-суть

LAST_YEAR_PERFORMANCE → Значення останнього року оцінки результативності; PREV_YEAR_PERFORMANCE → Значення передостаннього  року оцінки результативності; PREV_YEAR_PERFORMANCE → Значення передостанній  року оцінки результативності

Ці дані виводяться в деталізацію по тренду оцінки результативності

**Вимоги:** `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника/Додати-інформацію-про-оцінку-результативності-працівника-в-Картку-працівника`, `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`, `Командний-профіль/Паспортна-частина-групового-профілю/Додати-інформацію-про-ОКР-команди-та-середню-оцінку-результативності-по-команді`

## Залежності

Міри: [PP.Оцінка результативності попередній рік](../measures/pp-otsinka-rezultatyvnosti-poperednii-rik.md), [PP.Оцінка результативності поточний рік](../measures/pp-otsinka-rezultatyvnosti-potochnyi-rik.md)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[LAST_YEAR_PERFORMANCE]`, `fact_Burnout_Indicators[PREV_YEAR_PERFORMANCE]`

## Схема

```mermaid
graph LR
  M["PP.SVG.Performance.Last2Periods"]
  M --> fact_Burnout_Indicators
```

## Нотатки

_порожньо_
