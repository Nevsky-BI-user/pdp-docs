# AC.Оцінка.Чистий час в офісі, год.

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
		SELECTEDVALUE('fact_Loss_of_Productivity'[Net_Office_Time_Norm_Deviation]),
		0, " ✅ ",
		0.5, " ⚠️ ",
		1, "❌",
		"━"
	)
RETURN COALESCE( _res, "-" )
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Net_Office_Time_Norm_Deviation`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Net_Office_Time_Norm_Deviation → Чистий час в офісі, год.

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Net_Office_Time_Norm_Deviation]`

## Схема

```mermaid
graph LR
  M["AC.Оцінка.Чистий час в офісі, год."]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
