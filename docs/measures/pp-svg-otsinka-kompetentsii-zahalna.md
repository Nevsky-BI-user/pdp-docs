# PP.SVG.Оцінка компетенцій.Загальна

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
VAR _labelColor = "#003A5D"
VAR _MaxValue = 5
VAR _TrackOpacity = "0.15"          // прозорість світлої доріжки за стовпцем

// --- Дані: середня оцінка по роках ---
VAR _data = SUMMARIZE(
	'fact_360_Assessment',
	'fact_360_Assessment'[Assessment_Year],
	"Value", [PP.Оцінка компетенцій.Загальна]
)

// --- Геометрія полотна ---
VAR _W = 369                        // 410 × 0.9 — ширина із запасом 10%
VAR _H = 202                        // 224 × 0.9 — висота із запасом 10%
VAR _MarginLR = 4

// --- Бар (капсула) ---
VAR _BarWidth = 26
VAR _BarRadius = _BarWidth / 2      // 13 — повне округлення торців

// --- Бейдж року (пігулка) ---
VAR _BadgeW = 88
VAR _BadgeH = 32
VAR _BadgeRadius = _BadgeH / 2      // 16
VAR _BadgeTop = 8
VAR _BadgeTextBaseY = 30

// --- Підпис значення ---
VAR _ValueFontSize = 13
VAR _ValueBaseY = 60

// --- Доріжка (трек) і висота заливки ---
VAR _TrackTop = 74
VAR _TrackBottom = _H - 8           // 194
VAR _TrackHeight = _TrackBottom - _TrackTop   // 120

// --- Центрування блоку ---
VAR _BarCount = COUNTROWS(_data)
VAR _GroupWidth = 96                // слот року: резервує ширину підпису, щоб сусідні не накладались
VAR _AvailableW = _W - 2 * _MarginLR
VAR _GroupGapDesired = 16
VAR _MaxGapThatFits = IF(_BarCount > 1, (_AvailableW - _BarCount * _GroupWidth) / (_BarCount - 1), 0)
VAR _GroupGap = MAX(0, MIN(_GroupGapDesired, _MaxGapThatFits))
VAR _TotalContentWidth = _BarCount * _GroupWidth + (_BarCount - 1) * _GroupGap
VAR _StartX = (_W - _TotalContentWidth) / 2

// --- Побудова ---
VAR _BarsSVG = CONCATENATEX(
	ADDCOLUMNS(
		ADDCOLUMNS(
			_data,
			"@i", RANKX(_data, [Assessment_Year], , ASC, Dense) - 1
		),
		"@cx", _StartX + [@i] * (_GroupWidth + _GroupGap) + _GroupWidth / 2
	),
	VAR _v = [Value]

	VAR _class = SWITCH(TRUE(),
		ISBLANK(_v), "",
		_v < 3, "D",
		_v < 3.4, "C",
		_v < 3.75, "B",
		_v <= 4.25, "A",
		"TOP A"
	)

	VAR _Color = SWITCH(_class,
		"TOP A", "#16C8E8",
		"A", "#2EA84F",
		"B", "#F2B100",
		"C", "#9A9A9A",
		"D", "#E2231A",
		"#9A9A9A"
	)

	VAR _label = FORMAT(_v, "0.00") & IF(_class <> "", " (" & _class & ")", "")

	VAR _cx = [@cx]
	VAR _xBar = _cx - _BarWidth / 2
	VAR _xBadge = _cx - _BadgeW / 2

	VAR _fillH = MIN(DIVIDE(_v, _MaxValue, 0), 1) * _TrackHeight
	VAR _yFill = _TrackBottom - _fillH

	VAR _track =
		"<rect x='" & FORMAT(_xBar, "0.0", "en-US") & "' y='" & _TrackTop & "' width='" & _BarWidth & "' height='" & _TrackHeight & "' rx='" & _BarRadius & "' fill='" & _Color & "' fill-opacity='" & _TrackOpacity & "' />"

	VAR _fill =
		"<rect x='" & FORMAT(_xBar, "0.0", "en-US") & "' y='" & FORMAT(_yFill, "0.0", "en-US") & "' width='" & _BarWidth & "' height='" & FORMAT(_fillH, "0.0", "en-US") & "' rx='" & _BarRadius & "' fill='" & _Color & "' />"

	VAR _badge =
		"<rect x='" & FORMAT(_xBadge, "0.0", "en-US") & "' y='" & _BadgeTop & "' width='" & _BadgeW & "' height='" & _BadgeH & "' rx='" & _BadgeRadius & "' fill='#EBEBEB' />" &
		"<text x='" & FORMAT(_cx, "0.0", "en-US") & "' y='" & _BadgeTextBaseY & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:15px; fill:" & _labelColor & "; font-weight:700;'>" & FORMAT([Assessment_Year], "0") & "</text>"

	VAR _valueLabel =
		"<text x='" & FORMAT(_cx, "0.0", "en-US") & "' y='" & _ValueBaseY & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:" & _ValueFontSize & "px; fill:" & _labelColor & "; font-weight:600;'>" & _label & "</text>"

	RETURN _badge & _valueLabel & _track & _fill,
	"",
	[Assessment_Year], ASC
)

RETURN
"<svg xmlns='http://www.w3.org/2000/svg' width='" & _W & "' height='" & _H & "' viewBox='0 0 " & _W & " " & _H & "' preserveAspectRatio='xMidYMid meet'>
	" & _BarsSVG & "
</svg>"
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_360_Assessment`

Колонки: `Assessment_Year`

Power Query: `fact_360_Assessment`

### Залежності (таблиці й колонки)

Таблиці: `fact_360_Assessment`

Колонки: `fact_360_Assessment[Assessment_Year]`

### Схема

```mermaid
graph LR
  M["PP.SVG.Оцінка компетенцій.Загальна"]
  M --> fact_360_Assessment["fact_360_Assessment"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Результативність та оцінка › Оцінка компетенцій

## Пов'язані міри

**Використовує:** [PP.Оцінка компетенцій.Загальна](../measures/pp-otsinka-kompetentsii-zahalna.md)

## Нотатки

_порожньо_
