# AC.Чи є ризик вигорання через перепрацювання?

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
//НЕ видаляти пробіли для ✅
VAR _res = 
	SWITCH(
		SELECTEDVALUE('fact_Burnout_Indicators'[IS_VIVA_RISK]),
		"Ризик", "❌",
		"Відсутній", " ✅ ",
		"━"
	)
RETURN COALESCE( _res, "-" )
```

## Джерела


Колонки: `IS_VIVA_RISK`

Power Query: `fact_Burnout_Indicators`

## Бізнес-суть

IS_VIVA_RISK → Чи є ризик вигорання через перепрацювання?

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## Залежності

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[IS_VIVA_RISK]`

## Схема

```mermaid
graph LR
  M["AC.Чи є ризик вигорання через перепрацювання?"]
  M --> fact_Burnout_Indicators
```

## Нотатки

_порожньо_
