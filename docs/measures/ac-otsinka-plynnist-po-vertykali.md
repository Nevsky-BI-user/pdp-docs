# AC.Оцінка.Плинність % по вертикалі

*тека `Analytical Cases\Loss_Productivity\Main`*

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
		SELECTEDVALUE('fact_Loss_of_Productivity'[Vertical_Employee_Turnover]),
		0, " ✅ ",
		0.5, " ⚠️ ",
		1, "❌",
		"━"
	)
RETURN COALESCE( _res, "-" )
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Vertical_Employee_Turnover`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Vertical_Employee_Turnover]`

### Схема

```mermaid
graph LR
  M["AC.Оцінка.Плинність % по вертикалі"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

---

## Бізнес-суть

Vertical_Employee_Turnover → Плинність % по вертикалі

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Плинність % по вертикалі](../measures/ac-switch-plynnist-po-vertykali.md)

## Нотатки

_порожньо_
