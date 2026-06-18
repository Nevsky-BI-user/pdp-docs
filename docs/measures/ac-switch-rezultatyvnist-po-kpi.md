# AC.Switch.Результативність по KPI (%)

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
VAR _subperson = SELECTEDVALUE('fact_Loss_of_Productivity'[Person_Name])
VAR _metric_relevance = 
    CALCULATE(
        MIN('t_Loss_Productivity_Metrics_by_Persona'[Value]),
        't_Loss_Productivity_Metrics_by_Persona'[SubPerson] = _subperson,
        't_Loss_Productivity_Metrics_by_Persona'[Metric_Name] = "Award_Norm"
    )
VAR _result = 
    SWITCH(
        SELECTEDVALUE('t_AC Burnout'[Burnout_Indicator]),
        "Оцінка", [AC.Оцінка.Результативність по KPI (%)],
        "Дані", [AC.Дані.Результативність по KPI (%)]
    )
RETURN IF(_metric_relevance = "NA", "NA", _result)
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`, `DWH.t_SPO_HR_Person_Matrix_with_Coefficient`

Колонки: `Burnout_Indicator`, `Metric_Name`, `Person_Name`, `SubPerson`, `Value`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Результативність по KPI (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## Залежності

Міри: [AC.Дані.Результативність по KPI (%)](../measures/ac-dani-rezultatyvnist-po-kpi.md), [AC.Оцінка.Результативність по KPI (%)](../measures/ac-otsinka-rezultatyvnist-po-kpi.md)

Таблиці: `fact_Loss_of_Productivity`, `t_AC Burnout`, `t_Loss_Productivity_Metrics_by_Persona`

Колонки: `fact_Loss_of_Productivity[Person_Name]`, `t_AC Burnout[Burnout_Indicator]`, `t_Loss_Productivity_Metrics_by_Persona[Metric_Name]`, `t_Loss_Productivity_Metrics_by_Persona[SubPerson]`, `t_Loss_Productivity_Metrics_by_Persona[Value]`

## Схема

```mermaid
graph LR
  M["AC.Switch.Результативність по KPI (%)"]
  M --> fact_Loss_of_Productivity
  M --> t_AC Burnout
  M --> t_Loss_Productivity_Metrics_by_Persona
```

## Нотатки

_порожньо_
