# PP.Підпис типу події

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
VAR _maxd = 
    CALCULATE(
        MAX('fact_Employee_History_Position'[PERIOD]),
        ALLSELECTED('dim_Date')
    )
VAR _mind = 
    CALCULATE(
        MIN('fact_Employee_History_Position'[PERIOD]),
        ALLSELECTED('dim_Date')
    )
VAR _result = 
    SWITCH(
        TRUE(),
        SELECTEDVALUE('fact_Employee_History_Position'[PERIOD]) = _maxd, "Кінцева точка",
        SELECTEDVALUE('fact_Employee_History_Position'[PERIOD]) = _mind, "Стартова точка",
        SELECTEDVALUE('fact_Employee_History_Position'[EVENT_LIST])
    )
RETURN SELECTEDVALUE('fact_Employee_History_Position'[EVENT_LIST])
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Employee_History_Position`

Колонки: `EVENT_LIST`, `PERIOD`

Power Query: `fact_Employee_History_Position`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_History_Position`

Колонки: `fact_Employee_History_Position[EVENT_LIST]`, `fact_Employee_History_Position[PERIOD]`

### Схема

```mermaid
graph LR
  M["PP.Підпис типу події"]
  M --> fact_Employee_History_Position["fact_Employee_History_Position"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [TT:Життєвий цикл](../report/tt-zhyttievyi-tsykl.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
