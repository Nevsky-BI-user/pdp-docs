# AC.Оцінка.1:1 в сер. на 1 підлеглого, год.

*тека `Analytical Cases\Loss_Productivity\Main`*

## Бізнес-суть

Manager_Coaching_per_One_Employee → 1:1 в сер. на 1 підлеглого, год.

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.1:1 в сер. на 1 підлеглого, год.](../measures/ac-switch-1-1-v-ser-na-1-pidlehloho-hod.md)

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
		SELECTEDVALUE('fact_Loss_of_Productivity'[Manager_Coaching_per_One_Employee]),
		0, " ✅ ",
		0.5, " ⚠️ ",
		1, "❌",
		"━"
	)
RETURN COALESCE( _res, "-" )
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Manager_Coaching_per_One_Employee`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Manager_Coaching_per_One_Employee]`

### Схема

```mermaid
graph LR
  M["AC.Оцінка.1:1 в сер. на 1 підлеглого, год."]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

## Нотатки

_порожньо_
