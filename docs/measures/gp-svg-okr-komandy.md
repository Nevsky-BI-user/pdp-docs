# GP.SVG.OKR команди

*тека `Group_Profile\_Main\SVG`*

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовує:** [GP.OKR  попередній рік](../measures/gp-okr-poperednii-rik.md), [GP.OKR  поточний рік](../measures/gp-okr-potochnyi-rik.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\SVG` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
// OKR: бари + колір за відсотком від 5 балів
VAR _fontFamily      = "Segoe UI"
VAR _labelColor      = "#222222"
VAR _MaxValue        = MAX(100, MAX([GP.OKR  попередній рік], [GP.OKR  поточний рік]) *1.1)

// --- параметри підпису над баром (один рядок) ---
VAR _ValueFontSize = 11
VAR _LineH         = 11
VAR _TopTextH      = 2 * _LineH

// --- дані ---
VAR _data =
	UNION(
		ROW("@Year", INT(YEAR(TODAY())-2), "Value", [GP.OKR  попередній рік]),
		ROW("@Year", INT(YEAR(TODAY()))-1,    "Value", [GP.OKR  поточний рік])
	)

// --- геометрія полотна ---
VAR _W          = 250
VAR _H          = 150
VAR _MarginTop  = 8
VAR _MarginBot  = 22
VAR _ChartTop   = _MarginTop + _TopTextH + 2
VAR _ChartBot   = _H - _MarginBot
VAR _ChartH     = _ChartBot - _ChartTop

VAR _BarCount   = MAX(1, COUNTROWS(_data))
VAR _BarWidth   = 20
VAR _Gap        = 30
VAR _TotalBarsW = _BarCount * _BarWidth + (_BarCount - 1) * _Gap
VAR _StartX     = (_W - _TotalBarsW) / 2
VAR _RX         = _BarWidth / 2

// --- побудова ---
VAR _BarsSVG =
	CONCATENATEX(
		ADDCOLUMNS(
			ADDCOLUMNS(_data, "@i", RANKX(_data, [@Year], , ASC, Dense) - 1),
			"@x",  _StartX + [@i] * (_BarWidth + _Gap),
			"@cx", _StartX + [@i] * (_BarWidth + _Gap) + _BarWidth / 2
		),
		VAR _x    = [@x]
		VAR _cx   = [@cx]
		VAR _v    = [Value]
		VAR _vmax = _MaxValue

		// відсоток від максимуму у цілих (0–100+)
		VAR _pct  = 100 * DIVIDE(_v, _vmax, 0)

		// колір за діапазонами: >100; 100–91; 90–75; 74–50; 49–25; 24–0
		VAR _FillColor =
			SWITCH(
				TRUE(),
				_v > 100,               "#2E8B57",   // більше 100
				_v >= 91,               "#A0E695",   // 100–91
				_v >= 75,               "#D0E37E",   // 90–75
				_v >= 50,               "#FFE066",   // 74–50
				_v >= 25,               "#FFA64D",   // 49–25
				_v >  0,                "#FF7777",    // 24–0
				"#222222"
				--"#F5F5F5"
			)

		// заповнення
		VAR _ratio = MIN(DIVIDE(_v, _vmax, 0), 1)
		VAR _fillH = _ratio * _ChartH
		VAR _yFill = _ChartBot - _fillH

		// фон бару
		VAR _bgRect =
			"<rect x='" & _x & "' y='" & _ChartTop &
			"' width='" & _BarWidth & "' height='" & _ChartH &
			"' rx='" & _RX & "' ry='" & _RX &
			"' fill='" & _FillColor & "' fill-opacity='0.15' />"

		// заповнений бар
		VAR _fillRect =
			"<rect x='" & _x & "' y='" & FORMAT(_yFill, "0.0") &
			"' width='" & _BarWidth & "' height='" & FORMAT(_fillH, "0.0") &
			"' rx='" & _RX & "' ry='" & _RX &
			"' fill='" & _FillColor & "' />"

		// однорядковий підпис над баром (тільки значення)
		VAR _valueText =
			"<text x='" & FORMAT(_cx,"0.0") & "' y='" & (_MarginTop + _ValueFontSize) &
			"' text-anchor='middle' style=""font-family:" & _fontFamily &
			"; font-size:" & _ValueFontSize & "px; fill:" & _labelColor &
			"; font-weight:400;"">" &
				IF(ISBLANK(_v), "-", FORMAT(_v, "# ##0.0")) &
			"</text>"
		// VAR _valueText =
		//     IF(
		//         NOT ISBLANK(_v),
		//         "<text x='" & FORMAT(_cx,"0.0") & "' y='" & (_MarginTop + _ValueFontSize) &
		//         "' text-anchor='middle' style=""font-family:" & _fontFamily &
		//         "; font-size:" & _ValueFontSize & "px; fill:" & _labelColor &
		//         "; font-weight:400;"">" &
		//             FORMAT(_v, "# ##0.0") &
		//         "</text>",
		//         ""
		//     )

		// підпис року під баром
		VAR _labelText =
			"<text x='" & FORMAT(_cx,"0.0") & "' y='" & (_H - 4) &
			"' text-anchor='middle' style=""font-family:" & _fontFamily &
			"; font-size:11px; fill:" & _labelColor & ";"">" &
			SUBSTITUTE([@Year], "&", "&amp;") & "</text>"
		// VAR _labelText =
		//     IF(
		//         NOT ISBLANK(_v),
		//         "<text x='" & FORMAT(_cx,"0.0") & "' y='" & (_H - 4) &
		//         "' text-anchor='middle' style=""font-family:" & _fontFamily &
		//         "; font-size:11px; fill:" & _labelColor & ";"">" &
		//         SUBSTITUTE([@Year], "&", "&amp;") & "</text>",
		//         "-"
		//     )
		RETURN _bgRect & _fillRect & _valueText & _labelText,
	)

RETURN
"<svg xmlns='http://www.w3.org/2000/svg' width='" & _W & "' height='" & _H &
"' viewBox='0 0 " & _W & " " & _H & "'>
<rect x='0' y='0' width='" & _W & "' height='" & _H & "' fill='white'/>
" & _BarsSVG & "
</svg>"
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["GP.SVG.OKR команди"]
```

## Нотатки

_порожньо_
