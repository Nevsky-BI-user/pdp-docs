# PP.Колір шапки тултіпу

*тека `Personal_Profile\Життєвий цикл`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Життєвий цикл` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _first_date = 
    CALCULATE (
        FIRSTNONBLANK(
            'dim_Date'[Date],
            [PP.РЦД]
        ),
        ALLSELECTED( 'dim_Date'[Date] )
    )
VAR _result = 
    SWITCH(
        TRUE(),
        SELECTEDVALUE('fact_Employee_History_Position'[IS_APRIL_SALARY_REVIEW]), "#5B59C2",
        SELECTEDVALUE('fact_Employee_History_Position'[IS_TECH_POSITION_CHANGE]),  "#0F8C6E",
        SELECTEDVALUE('fact_Employee_History_Position'[IS_TECH_SALARY_TRANSFER]), "#C28814",
        SELECTEDVALUE('dim_Date'[Date]) = _first_date, "#7A8AA0",
        "#7A8AA0"
    )
RETURN _result
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Employee_History_Position`

Колонки: `Date`, `IS_APRIL_SALARY_REVIEW`, `IS_TECH_POSITION_CHANGE`, `IS_TECH_SALARY_TRANSFER`

Power Query: `dim_Date`

### Залежності (таблиці й колонки)

Таблиці: `dim_Date`, `fact_Employee_History_Position`

Колонки: `dim_Date[Date]`, `fact_Employee_History_Position[IS_APRIL_SALARY_REVIEW]`, `fact_Employee_History_Position[IS_TECH_POSITION_CHANGE]`, `fact_Employee_History_Position[IS_TECH_SALARY_TRANSFER]`

### Схема

```mermaid
graph LR
  M["PP.Колір шапки тултіпу"]
  M --> dim_Date["dim_Date"]
  M --> fact_Employee_History_Position["fact_Employee_History_Position"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Життєвий цикл
- [TT:Життєвий цикл](../report/tt-zhyttievyi-tsykl.md)

## Пов'язані міри

**Використовує:** [PP.РЦД](../measures/pp-rtsd.md)

## Нотатки

_порожньо_
