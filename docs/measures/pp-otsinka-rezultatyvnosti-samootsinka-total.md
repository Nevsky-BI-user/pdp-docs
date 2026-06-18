# PP.Оцінка результативності.Самооцінка.Total

*тека `Personal_Profile\Результативність та оцінка\Результативність` · формат `0.00`*

## Бізнес-суть

General_Self_Rate → Загальна самооцінка працівника

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [PP.SVG.Оцінка результативності.Total](../measures/pp-svg-otsinka-rezultatyvnosti-total.md), [PP.Оцінка результативності.Дані відсутні](../measures/pp-otsinka-rezultatyvnosti-dani-vidsutni.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Результативність та оцінка\Результативність` |
| formatString | `0.00` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
CALCULATE(AVERAGE('fact_Employee_Performance_Total'[General_Self_Rate]))
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Employee_Performance_General_PBI`

Колонки: `General_Self_Rate`

Power Query: `fact_Employee_Performance_Total`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_Performance_Total`

Колонки: `fact_Employee_Performance_Total[General_Self_Rate]`

### Схема

```mermaid
graph LR
  M["PP.Оцінка результативності.Самооцінка.Total"]
  M --> fact_Employee_Performance_Total["fact_Employee_Performance_Total"]
```

## Нотатки

_порожньо_
