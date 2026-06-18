# AC.Чи є ризик вигорання через відсутність відпусток?

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
//НЕ видаляти пробіли для ✅
VAR _res = 
	SWITCH(
		SELECTEDVALUE('fact_Burnout_Indicators'[IS_VACATION_RISK]),
		"Відсутній", " ✅ ",
		"Ризик", "❌",
		"━"
	)
RETURN COALESCE( _res, "-" )
```

### Джерела даних


Колонки: `IS_VACATION_RISK`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[IS_VACATION_RISK]`

### Схема

```mermaid
graph LR
  M["AC.Чи є ризик вигорання через відсутність відпусток?"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

---

## Бізнес-суть

IS_VACATION_RISK → Чи є ризик вигорання через відсутність відпусток?

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Кількість місяців без якісної відпустки за ост. 3 роки](../measures/ac-switch-kilkist-misiatsiv-bez-iakisnoi-vidpustky-za-ost-3-roky.md)

## Нотатки

_порожньо_
