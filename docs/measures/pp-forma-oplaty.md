# PP.Форма оплати

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
VAR _maxd = [PP.history_position_maxd]
VAR _res = 
    CALCULATE(
        SELECTEDVALUE(fact_Employee_History_Position[TARIFF_RATE_TYPE_CODE]),
        'fact_Employee_History_Position'[PERIOD] = _maxd
    )
RETURN COALESCE(_res, "—")
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Employee_History_Position`

Колонки: `PERIOD`, `TARIFF_RATE_TYPE_CODE`

Power Query: `fact_Employee_History_Position`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_History_Position`

Колонки: `fact_Employee_History_Position[PERIOD]`, `fact_Employee_History_Position[TARIFF_RATE_TYPE_CODE]`

### Схема

```mermaid
graph LR
  M["PP.Форма оплати"]
  M --> fact_Employee_History_Position["fact_Employee_History_Position"]
```

---

## Бізнес-суть

PERIOD → Дата нарахування премії Зірка МХП; PERIOD → Дата; PERIOD → Період нарахування; PERIOD → Період; TARIFF_RATE_TYPE_CODE → Вид оплати праці (тарифної ставки); TARIFF_RATE_TYPE_CODE → Вид Тарифної Ставки

Це дата нарахування/виплати премії Зірка МХП (accrual_types_key = '9781d4aa-3a0d-1458-623a-7a93e90a2284'   та category_of_accrual_sort  = '2' ) Поточний період Назви змапити українською:  <br>ЧАСОВАЯ - Погодинна  <br>ДНЕВНАЯ - Денна  <br>СДЕЛЬНАЯ - Відрядна  <br>МЕСЯЧНАЯ_ПО_ЧАСАМ - Місячна по годинам  <br>МЕСЯЧНАЯ - Місячна

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Деталізація-на-сторінці-Винагорода`, `Допоміжні-вітрини-для-звіту/Таблиця-(вью)-для-розрахунку-метрики-Укомплектованість-штату`, `Допоміжні-вітрини-для-звіту/Таблиця-періодична-(попередні-12-міс)-для-розрахунку-метрики-Середній-дохід`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

**Використовує:** [PP.history_position_maxd](../measures/pp-history-position-maxd.md)

## Нотатки

_порожньо_
