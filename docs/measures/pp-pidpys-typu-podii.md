# PP.Підпис типу події

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Життєвий цикл` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

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

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Employee_History_Position`

Колонки: `EVENT_LIST`, `PERIOD`

Power Query: `fact_Employee_History_Position`

## Бізнес-суть

PERIOD → Дата нарахування премії Зірка МХП; PERIOD → Дата; PERIOD → Період нарахування; PERIOD → Період

Це дата нарахування/виплати премії Зірка МХП (accrual_types_key = '9781d4aa-3a0d-1458-623a-7a93e90a2284'   та category_of_accrual_sort  = '2' ) Поточний період

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Деталізація-на-сторінці-Винагорода`, `Допоміжні-вітрини-для-звіту/Таблиця-(вью)-для-розрахунку-метрики-Укомплектованість-штату`, `Допоміжні-вітрини-для-звіту/Таблиця-періодична-(попередні-12-міс)-для-розрахунку-метрики-Середній-дохід`

## Залежності

Таблиці: `fact_Employee_History_Position`

Колонки: `fact_Employee_History_Position[EVENT_LIST]`, `fact_Employee_History_Position[PERIOD]`

## Схема

```mermaid
graph LR
  M["PP.Підпис типу події"]
  M --> fact_Employee_History_Position
```

## Нотатки

_порожньо_
