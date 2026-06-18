# AC.Оцінка.Тренд Результативності по KPI (%)

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Loss_Productivity\Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
//НЕ видаляти пробіли для ✅
VAR _res = 
	SWITCH(
		SELECTEDVALUE('fact_Loss_of_Productivity'[Award_Trend_Pct]),
		0, " ✅ ",
		0.5, " ⚠️ ",
		1, "❌",
		"━"
	)
RETURN COALESCE( _res, "-" )
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Award_Trend_Pct`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Award_Trend_Pct → Тренд Результативності по KPI (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Award_Trend_Pct]`

## Схема

```mermaid
graph LR
  M["AC.Оцінка.Тренд Результативності по KPI (%)"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
