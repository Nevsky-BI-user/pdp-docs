# PP.SVG.Оцінка результативності.Total

*тека `Personal_Profile\Результативність та оцінка\Результативність`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Результативність та оцінка\Результативність` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _fontFamily = "Segoe UI"
VAR _labelColor = "#003A5D"
VAR _MaxValue = 5

// --- Параметри підпису ---
VAR _ValueFontSize = 10
VAR _TopTextH = 28
VAR _BottomMargin = 22

// --- Дані ---
VAR _data_sup = SUMMARIZE(
	'fact_Employee_Performance_Total',
	'fact_Employee_Performance_Total'[performance_PBI_order],
	'fact_Employee_Performance_Total'[performence_period],
	"Value1", [PP.Оцінка результативності.Керівником.Total],
	"Value2", [PP.Оцінка результативності.Самооцінка.Total]
)

// --- Геометрія полотна ---
VAR _W = 640
VAR _H = 150
VAR _MarginTop = 8
VAR _MarginLR = 40
VAR _ChartTop = _MarginTop + _TopTextH
VAR _ChartBot = _H - _BottomMargin
VAR _ChartH = _ChartBot - _ChartTop

VAR _BarCount = COUNTROWS(_data_sup)
VAR _BarWidth = 20
VAR _BarGap = 10
VAR _GroupWidth = (_BarWidth * 2) + _BarGap
VAR _AvailableW = _W - 2 * _MarginLR
VAR _GroupGap = IF(_BarCount > 1, (_AvailableW - _BarCount * _GroupWidth) / (_BarCount - 1), 0)
VAR _StartX = _MarginLR

// --- Побудова ---
VAR _BarsSVG = CONCATENATEX(
	ADDCOLUMNS(
		ADDCOLUMNS(
			_data_sup,
			"@i", RANKX(_data_sup, [performance_PBI_order], , ASC, Dense) - 1
		),
		"@xGroup", _StartX + [@i] * (_GroupWidth + _GroupGap)
	),
	VAR _v1 = [Value1]
	VAR _v2 = [Value2]

	VAR _class1 = SWITCH(TRUE(),
		ISBLANK(_v1), "",
		_v1 < 3, "D",
		_v1 <= 3.39, "C",
		_v1 <= 3.89, "B",
		_v1 <= 4.29, "A",
		_v1 <= 5.00, "A+"
	)

	VAR _class2 = SWITCH(TRUE(),
		ISBLANK(_v2), "",
		_v2 < 3, "D",
		_v2 <= 3.39, "C",
		_v2 <= 3.89, "B",
		_v2 <= 4.29, "A",
		_v2 <= 5.00, "A+"
	)

	VAR _ColorFill1 = SWITCH(_class1,
		"A+", "#8bd6ea",
		"A", "#5a974d",
		"B", "#e9c246",
		"C", "#9e241e",
		"D", "#a5a4a6",
		"#a5a4a6"
	)

	VAR _ColorFill2 = SWITCH(_class2,
		"A+", "#8bd6ea",
		"A", "#5a974d",
		"B", "#e9c246",
		"C", "#9e241e",
		"D", "#a5a4a6",
		"#a5a4a6"
	)

	VAR _label1 = FORMAT(_v1, "0.00") & IF(_class1 <> "", " (" & _class1 & ")", "")
	VAR _label2 = FORMAT(_v2, "0.00") & IF(_class2 <> "", " (" & _class2 & ")", "")

	VAR _x1 = [@xGroup]
	VAR _x2 = [@xGroup] + _BarWidth + _BarGap
	VAR _cx = [@xGroup] + (_GroupWidth / 2)

	VAR _h1 = MIN(DIVIDE(_v1, _MaxValue, 0), 1) * _ChartH
	VAR _y1 = _ChartBot - _h1
	VAR _h2 = MIN(DIVIDE(_v2, _MaxValue, 0), 1) * _ChartH
	VAR _y2 = _ChartBot - _h2

	VAR _rects =
		"<rect x='" & _x1 & "' y='" & _ChartTop & "' width='" & _BarWidth & "' height='" & _ChartH & "' fill='" & _ColorFill1 & "' fill-opacity='0.1' stroke='" & _ColorFill1 & "' stroke-width='1' stroke-opacity='0.3' />" &
		"<rect x='" & _x2 & "' y='" & _ChartTop & "' width='" & _BarWidth & "' height='" & _ChartH & "' fill='" & _ColorFill2 & "' fill-opacity='0.1' />" &
		"<rect x='" & _x1 & "' y='" & FORMAT(_y1, "0.0") & "' width='" & _BarWidth & "' height='" & FORMAT(_h1, "0.0") & "' fill='" & _ColorFill1 & "' stroke='" & _ColorFill1 & "' stroke-width='1' />" &
		"<rect x='" & _x2 & "' y='" & FORMAT(_y2, "0.0") & "' width='" & _BarWidth & "' height='" & FORMAT(_h2, "0.0") & "' fill='" & _ColorFill2 & "' fill-opacity='0.7' />"

	VAR _labelMidX = _x1 + _BarWidth + (_BarGap / 2)
	VAR _labels =
		"<text x='" & (_labelMidX - 3) & "' y='" & (_ChartTop - 12) & "' text-anchor='end' style='font-family:" & _fontFamily & "; font-size:" & _ValueFontSize & "px; fill:" & _labelColor & "; font-weight:700;'>" & _label1 & "</text>" &
		"<text x='" & (_labelMidX + 3) & "' y='" & (_ChartTop - 12) & "' text-anchor='start' style='font-family:" & _fontFamily & "; font-size:" & _ValueFontSize & "px; fill:" & _labelColor & ";'>" & _label2 & "</text>"

	VAR _periodLabel =
		"<text x='" & _cx & "' y='" & (_H - 5) & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:12px; fill:" & _labelColor & "; font-weight:600;'>" &
		SUBSTITUTE([performence_period], "&", "&amp;") &
		"</text>"

	RETURN _rects & _labels & _periodLabel,
	"",
	[performance_PBI_order], ASC
)

RETURN
"<svg xmlns='http://www.w3.org/2000/svg' width='100%' height='" & _H & "' viewBox='0 0 " & _W & " " & _H & "' preserveAspectRatio='xMinYMid meet'>
	" & _BarsSVG & "
</svg>"
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Employee_Performance_General_PBI`

Колонки: `performance_PBI_order`, `performence_period`

Power Query: `fact_Employee_Performance_Total`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_Performance_Total`

Колонки: `fact_Employee_Performance_Total[performance_PBI_order]`, `fact_Employee_Performance_Total[performence_period]`

### Схема

```mermaid
graph LR
  M["PP.SVG.Оцінка результативності.Total"]
  M --> fact_Employee_Performance_Total["fact_Employee_Performance_Total"]
```

---

## Бізнес-суть

**Бізнес-назва:** Оцінка результативності

**Вимоги (ТЗ):**

- [Індивідуальний профіль працівника › Історія по посадам](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%86%D0%BD%D0%B4%D0%B8%D0%B2%D1%96%D0%B4%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0/%D0%86%D1%81%D1%82%D0%BE%D1%80%D1%96%D1%8F%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D0%B0%D0%B4%D0%B0%D0%BC)
- [Індивідуальний профіль працівника › Історія по посадам › Реліз 1. Історія по посадам](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%86%D0%BD%D0%B4%D0%B8%D0%B2%D1%96%D0%B4%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0/%D0%86%D1%81%D1%82%D0%BE%D1%80%D1%96%D1%8F%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D0%B0%D0%B4%D0%B0%D0%BC/%D0%A0%D0%B5%D0%BB%D1%96%D0%B7%201.%20%D0%86%D1%81%D1%82%D0%BE%D1%80%D1%96%D1%8F%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D0%B0%D0%B4%D0%B0%D0%BC)

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Результативність та оцінка › Результативність

## Пов'язані міри

**Використовує:** [PP.Оцінка результативності.Керівником.Total](../measures/pp-otsinka-rezultatyvnosti-kerivnykom-total.md), [PP.Оцінка результативності.Самооцінка.Total](../measures/pp-otsinka-rezultatyvnosti-samootsinka-total.md)

## Нотатки

_порожньо_
