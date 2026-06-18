# AC.Чи є ризик вигорання по результатам оцінки OKR?

*тека `Analytical Cases\Burnout_Risk\Main`*

## Бізнес-суть

IS_OKR_RISK → Чи є ризик вигорання по результатам оцінки OKR?

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Тренд оцінки OKR](../measures/ac-switch-trend-otsinky-okr.md)

---

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
//НЕ видаляти пробіли для ✅
VAR _val = SELECTEDVALUE('fact_Burnout_Indicators'[IS_OKR_RISK])

VAR _vw = 110
VAR _vh = 16

/* палітра */
VAR _colRisk = "#E03232"  // насичений червоний
VAR _colOk   = "#33C072"
VAR _colOkBd = "#1F8E5A"
VAR _colNone = "#9AA0A6"

/* ✅ галочка — по центру */
VAR _okSvg =
"data:image/svg+xml;utf8," &
"<svg xmlns='http://www.w3.org/2000/svg' width='"&_vw&"' height='"&_vh&"' viewBox='0 0 110 16' preserveAspectRatio='xMidYMid meet'>" &
"<g transform='translate(48,2) scale(0.85)'>" &
	"<rect x='1.5' y='1.5' width='13' height='13' rx='2' fill='"&_colOk&"' stroke='"&_colOkBd&"' stroke-width='1.2'/>" &
	"<polyline points='4,8.5 7.1,11.2 12.8,4.8' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/>" &
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

/* резервна риска — по центру */
VAR _noneSvg =
"data:image/svg+xml;utf8," &
"<svg xmlns='http://www.w3.org/2000/svg' width='"&_vw&"' height='"&_vh&"' viewBox='0 0 110 16' preserveAspectRatio='xMidYMid meet'>" &
"<g transform='translate(48,2) scale(0.85)'>" &
	"<line x1='2' y1='8' x2='18' y2='8' stroke='"&_colNone&"' stroke-width='1.4' stroke-linecap='round'/>" &
"</g>" &
"</svg>"

VAR _res =
	SWITCH(
		TRUE(),
		_val = "Ризик",     _riskSvg,
		_val = "Відсутній", _okSvg,
		ISBLANK(_val),      _dashSvg,
		_noneSvg
	)

RETURN _res
```

### Джерела даних


Колонки: `IS_OKR_RISK`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[IS_OKR_RISK]`

### Схема

```mermaid
graph LR
  M["AC.Чи є ризик вигорання по результатам оцінки OKR?"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

## Нотатки

_порожньо_
