# AC.Дані.Результативність по KPI (%)

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
VAR _res = SELECTEDVALUE('fact_Loss_of_Productivity'[Award_Norm_Pct])
RETURN COALESCE(_res, "—")
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Award_Norm_Pct`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Award_Norm_Pct]`

### Схема

```mermaid
graph LR
  M["AC.Дані.Результативність по KPI (%)"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

---

## Бізнес-суть

Award_Norm_Pct → Результативність по KPI (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Результативність по KPI (%)](../measures/ac-switch-rezultatyvnist-po-kpi.md)

## Нотатки

_порожньо_
