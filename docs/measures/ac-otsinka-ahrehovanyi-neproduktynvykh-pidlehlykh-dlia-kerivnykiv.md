# AC.Оцінка.Агрегований % непродуктинвих підлеглих для керівників

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
		SELECTEDVALUE('fact_Loss_of_Productivity'[Unproductive_Subordinate_Pct]),
		0, " ✅ ",
		0.5, " ⚠️ ",
		1, "❌",
		"━"
	)
RETURN COALESCE( _res, "-" )
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Unproductive_Subordinate_Pct`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Unproductive_Subordinate_Pct → Агрегований % непродуктинвих підлеглих для керівників

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Unproductive_Subordinate_Pct]`

## Схема

```mermaid
graph LR
  M["AC.Оцінка.Агрегований % непродуктинвих підлеглих для керівників"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
