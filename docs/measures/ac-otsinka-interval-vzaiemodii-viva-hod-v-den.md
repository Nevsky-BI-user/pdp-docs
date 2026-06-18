# AC.Оцінка.Інтервал взаємодії (Viva), год. в день

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
		SELECTEDVALUE('fact_Loss_of_Productivity'[Collab_Span_Norm]),
		0, " ✅ ",
		0.5, " ⚠️ ",
		1, "❌",
		"━"
	)
RETURN COALESCE( _res, "-" )
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Collab_Span_Norm`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Collab_Span_Norm → Інтервал взаємодії (Viva), год. в день

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Collab_Span_Norm]`

## Схема

```mermaid
graph LR
  M["AC.Оцінка.Інтервал взаємодії (Viva), год. в день"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
