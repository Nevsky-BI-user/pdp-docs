# AC.Оцінка.Доля днів польових робіт (%)

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
		SELECTEDVALUE('fact_Loss_of_Productivity'[Fieldwork_Share_by_Norm]),
		0, " ✅ ",
		0.5, " ⚠️ ",
		1, "❌",
		"━"
	)
RETURN COALESCE( _res, "-" )
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Fieldwork_Share_by_Norm`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Fieldwork_Share_by_Norm → Доля днів польових робіт (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Fieldwork_Share_by_Norm]`

## Схема

```mermaid
graph LR
  M["AC.Оцінка.Доля днів польових робіт (%)"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
