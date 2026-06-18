# AC.Ризик

*тека `Analytical Cases\Burnout_Risk\Main`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _val = SELECTEDVALUE('fact_Burnout_Indicators'[IS_TOTAL_RISK])
VAR _txt = COALESCE(_val, "Не визначено")

VAR _fill =
	SWITCH(
		_txt,
		"Потребує уваги", "#FDE0D0",
		"Показники в нормі", "#D0E8F2",
		"#C9CFD6"
	)
VAR _textColor =
	SWITCH(
		_txt,
		"Потребує уваги", "#A63D00",
		"Показники в нормі", "#004D73",
		"#3B4552"
	)
VAR _stroke =
	SWITCH(
		_txt,
		"Потребує уваги", "#D55E00",
		"Показники в нормі", "#0072B2",
		"#AEB6BF"
	)

VAR _rectW = 110
VAR _rectH = 16
VAR _r = 8
VAR _font = 10
VAR _centerX = _rectW / 2

RETURN
"data:image/svg+xml;utf8," &
"<svg xmlns='http://www.w3.org/2000/svg' width='" & _rectW & "' height='" & _rectH & "'>
<rect x='0' y='0' rx='"&_r&"' ry='"&_r&"' width='"&_rectW&"' height='"&_rectH&"' fill='"&_fill&"' stroke='"&_stroke&"' stroke-width='0.8'/>
<text x='"&_centerX&"' y='"&(_rectH/2)&"' font-size='"&_font&"px' font-family='Segoe UI' font-weight='500' text-anchor='middle' dominant-baseline='central' fill='"&_textColor&"'>"&_txt&"</text>
</svg>"
```

### Джерела даних


Колонки: `IS_TOTAL_RISK`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[IS_TOTAL_RISK]`

### Схема

```mermaid
graph LR
  M["AC.Ризик"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

---

## Бізнес-суть

**Бізнес-назва:** Ризик

**Вимоги (ТЗ):**

- [Кейс Утримання працівників › Опис джерел для сторінки "Кейс звільнення (вигорання)"](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%9A%D0%B5%D0%B9%D1%81%20%D0%A3%D1%82%D1%80%D0%B8%D0%BC%D0%B0%D0%BD%D0%BD%D1%8F%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D1%96%D0%B2/%D0%9E%D0%BF%D0%B8%D1%81%20%D0%B4%D0%B6%D0%B5%D1%80%D0%B5%D0%BB%20%D0%B4%D0%BB%D1%8F%20%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8%20%22%D0%9A%D0%B5%D0%B9%D1%81%20%D0%B7%D0%B2%D1%96%D0%BB%D1%8C%D0%BD%D0%B5%D0%BD%D0%BD%D1%8F%20%28%D0%B2%D0%B8%D0%B3%D0%BE%D1%80%D0%B0%D0%BD%D0%BD%D1%8F%29%22)

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Burnout.Tooltip](../measures/ac-burnout-tooltip.md), [AC.Switch.Ризик](../measures/ac-switch-ryzyk.md)

## Нотатки

_порожньо_
