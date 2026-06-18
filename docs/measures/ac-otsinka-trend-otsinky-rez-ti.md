# AC.Оцінка.Тренд Оцінки рез-ті (%)

*тека `Analytical Cases\Loss_Productivity\Main`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Loss_Productivity\Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
//НЕ видаляти пробіли для ✅
VAR _val = SELECTEDVALUE('fact_Loss_of_Productivity'[Trend_Rate_Pct])
VAR _vw = 110
VAR _vh = 16

/* палітра */
VAR _colRisk   = "#E03232"
VAR _colOk     = "#33C072"
VAR _colOkBd   = "#1F8E5A"
VAR _colWarn   = "#FFB800"
VAR _colWarnBd = "#E0A000"
VAR _colNone   = "#9AA0A6"

/* ✅ галочка — по центру */
VAR _okSvg =
"data:image/svg+xml;utf8," &
"<svg xmlns='http://www.w3.org/2000/svg' width='"&_vw&"' height='"&_vh&"' viewBox='0 0 110 16' preserveAspectRatio='xMidYMid meet'>" &
"<g transform='translate(48,2) scale(0.85)'>" &
	"<rect x='1.5' y='1.5' width='13' height='13' rx='2' fill='"&_colOk&"' stroke='"&_colOkBd&"' stroke-width='1.2'/>" &
	"<polyline points='4,8.5 7.1,11.2 12.8,4.8' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/>" &
"</g>" &
"</svg>"

/* ⚠️ знак оклику в жовтому трикутнику — по центру */
VAR _warnSvg =
"data:image/svg+xml;utf8," &
"<svg xmlns='http://www.w3.org/2000/svg' width='"&_vw&"' height='"&_vh&"' viewBox='0 0 110 16' preserveAspectRatio='xMidYMid meet'>" &
"<g transform='translate(48,1) scale(0.85)'>" &
	"<path d='M8,1 L15.5,14 L0.5,14 Z' fill='"&_colWarn&"' stroke='"&_colWarnBd&"' stroke-width='1' stroke-linejoin='round'/>" &
	"<line x1='8' y1='5.5' x2='8' y2='9.5' stroke='black' stroke-width='1.8' stroke-linecap='round'/>" &
	"<circle cx='8' cy='12' r='1' fill='black'/>" &
"</g>" &
"</svg>"

/* ❌ хрестик — по центру */
VAR _riskSvg =
"data:image/svg+xml;utf8," &
"<svg xmlns='http://www.w3.org/2000/svg' width='"&_vw&"' height='"&_vh&"' viewBox='0 0 110 16' preserveAspectRatio='xMidYMid meet'>" &
"<g transform='translate(48,2) scale(0.85)'>" &
	"<line x1='3.5' y1='3.5' x2='14.5' y2='14.5' stroke='"&_colRisk&"' stroke-width='2.6' stroke-linecap='round'/>" &
	"<line x1='14.5' y1='3.5' x2='3.5'  y2='14.5' stroke='"&_colRisk&"' stroke-width='2.6' stroke-linecap='round'/>" &
"</g>" &
"</svg>"

/* — коротке тире — по центру */
VAR _dashSvg =
"data:image/svg+xml;utf8," &
"<svg xmlns='http://www.w3.org/2000/svg' width='"&_vw&"' height='"&_vh&"' viewBox='0 0 110 16' preserveAspectRatio='xMidYMid meet'>" &
"<g transform='translate(48,1.5)'>" &
	"<line x1='2' y1='9' x2='13' y2='9' stroke='"&_colNone&"' stroke-width='1.2' stroke-linecap='round'/>" &
"</g>" &
"</svg>"

VAR _res =
	SWITCH(
		_val,
		0,   _okSvg,
		0.5, _warnSvg,
		1,   _riskSvg,
		_dashSvg
	)

RETURN _res
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Trend_Rate_Pct`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Trend_Rate_Pct]`

### Схема

```mermaid
graph LR
  M["AC.Оцінка.Тренд Оцінки рез-ті (%)"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

---

## Бізнес-суть

**Бізнес-назва:** Тренд Оцінки рез-ті (%)

**Вимоги (ТЗ):**

- [Кейс Втрати Продуктивності Працівників](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%9A%D0%B5%D0%B9%D1%81%20%D0%92%D1%82%D1%80%D0%B0%D1%82%D0%B8%20%D0%9F%D1%80%D0%BE%D0%B4%D1%83%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D1%81%D1%82%D1%96%20%D0%9F%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D1%96%D0%B2)

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Тренд Оцінки рез-ті (%)](../measures/ac-switch-trend-otsinky-rez-ti.md)

## Нотатки

_порожньо_
