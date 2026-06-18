# AC.Оцінка.Інтервал взаємодії (Viva), год. в день

*тека `Analytical Cases\Loss_Productivity\Main`*

!!! abstract "Джерела даних"
    `DM.vw_R27_fact_Loss_of_Productivity`

## Бізнес-суть

Collab_Span_Norm → Інтервал взаємодії (Viva), год. в день

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Інтервал взаємодії (Viva), год. в день](../measures/ac-switch-interval-vzaiemodii-viva-hod-v-den.md)

---

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

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Collab_Span_Norm`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Collab_Span_Norm]`

### Схема

```mermaid
graph LR
  M["AC.Оцінка.Інтервал взаємодії (Viva), год. в день"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

## Нотатки

_порожньо_
