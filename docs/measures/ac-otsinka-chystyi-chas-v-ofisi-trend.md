# AC.Оцінка.Чистий час в офісі Тренд (%)

*тека `Analytical Cases\Loss_Productivity\Main`*

!!! abstract "Джерела даних"
    `DM.vw_R27_fact_Loss_of_Productivity`

## Бізнес-суть

Net_Office_Time_Trend_Pct → Чистий час в офісі Тренд (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Чистий час в офісі Тренд (%)](../measures/ac-switch-chystyi-chas-v-ofisi-trend.md)

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
		SELECTEDVALUE('fact_Loss_of_Productivity'[Net_Office_Time_Trend_Pct]),
		0, " ✅ ",
		0.5, " ⚠️ ",
		1, "❌",
		"━"
	)
RETURN COALESCE( _res, "-" )
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Net_Office_Time_Trend_Pct`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Net_Office_Time_Trend_Pct]`

### Схема

```mermaid
graph LR
  M["AC.Оцінка.Чистий час в офісі Тренд (%)"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

## Нотатки

_порожньо_
