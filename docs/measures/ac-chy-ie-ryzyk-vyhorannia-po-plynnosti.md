# AC.Чи є ризик вигорання по плинності?

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
	SELECTEDVALUE('fact_Burnout_Indicators'[IS_TURNOVER_RISK]),
	"Ризик", "❌",
	"Відсутній", " ✅ ",
	"━"
)
RETURN COALESCE( _res, "-" )
```

## Джерела


Колонки: `IS_TURNOVER_RISK`

Power Query: `fact_Burnout_Indicators`

## Бізнес-суть

IS_TURNOVER_RISK → Чи є ризик вигорання по плинності?

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## Залежності

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[IS_TURNOVER_RISK]`

## Схема

```mermaid
graph LR
  M["AC.Чи є ризик вигорання по плинності?"]
  M --> fact_Burnout_Indicators
```

## Нотатки

_порожньо_
