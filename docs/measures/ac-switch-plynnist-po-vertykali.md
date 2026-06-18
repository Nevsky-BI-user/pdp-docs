# AC.Switch.Плинність % по вертикалі

*тека `Analytical Cases\Loss_Productivity\Main`*

## Бізнес-суть

Плинність % по вертикалі

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## На сторінках звіту

[Продуктивність працівників](../report/produktyvnist-pratsivnykiv.md)

## Пов'язані міри

**Використовує:** [AC.Дані.Плинність % по вертикалі](../measures/ac-dani-plynnist-po-vertykali.md), [AC.Оцінка.Плинність % по вертикалі](../measures/ac-otsinka-plynnist-po-vertykali.md)

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
VAR _subperson = SELECTEDVALUE('fact_Loss_of_Productivity'[Person_Name])
VAR _metric_relevance = 
    CALCULATE(
        MIN('t_Loss_Productivity_Metrics_by_Persona'[Value]),
        't_Loss_Productivity_Metrics_by_Persona'[SubPerson] = _subperson,
        't_Loss_Productivity_Metrics_by_Persona'[Metric_Name] = "Vertical_Employee_Turnover"
    )
VAR _result = 
    SWITCH(
        SELECTEDVALUE('t_AC Burnout'[Burnout_Indicator]),
        "Оцінка", [AC.Оцінка.Плинність % по вертикалі],
        "Дані", [AC.Дані.Плинність % по вертикалі]
    )
RETURN IF(_metric_relevance = "NA", "NA", _result)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`, `DWH.t_SPO_HR_Person_Matrix_with_Coefficient`

Колонки: `Burnout_Indicator`, `Metric_Name`, `Person_Name`, `SubPerson`, `Value`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`, `t_AC Burnout`, `t_Loss_Productivity_Metrics_by_Persona`

Колонки: `fact_Loss_of_Productivity[Person_Name]`, `t_AC Burnout[Burnout_Indicator]`, `t_Loss_Productivity_Metrics_by_Persona[Metric_Name]`, `t_Loss_Productivity_Metrics_by_Persona[SubPerson]`, `t_Loss_Productivity_Metrics_by_Persona[Value]`

### Схема

```mermaid
graph LR
  M["AC.Switch.Плинність % по вертикалі"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
  M --> t_AC_Burnout["t_AC Burnout"]
  M --> t_Loss_Productivity_Metrics_by_Persona["t_Loss_Productivity_Metrics_by_Persona"]
```

## Нотатки

_порожньо_
