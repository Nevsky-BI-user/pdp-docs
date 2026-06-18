# PP.ЖЦ_Підприємство

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
VAR _maxd = [PP.history_position_maxd]
VAR _res = 
    CALCULATE(
        SELECTEDVALUE(fact_Employee_History_Position[ORGANIZATION_NAME]),
        'fact_Employee_History_Position'[PERIOD] = _maxd
    )
RETURN _res
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Employee_History_Position`

Колонки: `ORGANIZATION_NAME`, `PERIOD`

Power Query: `fact_Employee_History_Position`

## Бізнес-суть

ORGANIZATION_NAME → Організація; PERIOD → Дата нарахування премії Зірка МХП; PERIOD → Дата; PERIOD → Період нарахування; PERIOD → Період

Це дата нарахування/виплати премії Зірка МХП (accrual_types_key = '9781d4aa-3a0d-1458-623a-7a93e90a2284'   та category_of_accrual_sort  = '2' ) Поточний період

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Деталізація-на-сторінці-Винагорода`, `Допоміжні-вітрини-для-звіту/Таблиця-(вью)-для-розрахунку-метрики-Укомплектованість-штату`, `Допоміжні-вітрини-для-звіту/Таблиця-періодична-(попередні-12-міс)-для-розрахунку-метрики-Середній-дохід`

## Залежності

Міри: [PP.history_position_maxd](../measures/pp-history-position-maxd.md)

Таблиці: `fact_Employee_History_Position`

Колонки: `fact_Employee_History_Position[ORGANIZATION_NAME]`, `fact_Employee_History_Position[PERIOD]`

## Схема

```mermaid
graph LR
  M["PP.ЖЦ_Підприємство"]
  M --> fact_Employee_History_Position
```

## Нотатки

_порожньо_
