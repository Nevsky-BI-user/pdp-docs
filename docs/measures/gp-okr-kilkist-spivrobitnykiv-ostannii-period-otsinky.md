# GP.ОКР.Кількість співробітників (Останній період оцінки)

*тека `Group_Profile\_Main\ОКР` · формат `0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\ОКР` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
//************* ROLE FILTERS **************
VAR _filter_lt = TREATAS(VALUES(dim_Admin_LT_OS[USER_ACCESS_ID]), 'dim_Admin_OS'[USER_ACCESS_ID])

VAR lastYear = [GP.ОКР.Останній рік]
/* *********** ADMIN *********** */
VAR _admin =
CALCULATE(
        DISTINCTCOUNT('fact_Employee_OKR'[USER_ACCESS_ID]),
        'fact_Employee_OKR'[PLAN_YEAR] = lastYear)
        // FILTER(
        //     'fact_Employee_OKR',
        //     'fact_Employee_OKR'[order] = 1))

/* *********** ADMIN LT *********** */
VAR _admin_lt =
CALCULATE(
        DISTINCTCOUNT('fact_Employee_OKR'[USER_ACCESS_ID]),
        'fact_Employee_OKR'[PLAN_YEAR] = lastYear,
        // FILTER(
        //     'fact_Employee_OKR',
        //     'fact_Employee_OKR'[order] = 1),
        _filter_lt)

VAR _res = 
	SWITCH(
		SELECTEDVALUE( t_HierarchyTypes[Index] ),
		0, _admin_lt,
		1, _admin
	)

/* *********** RESULT *********** */
RETURN COALESCE(_res, 0)
```

### Джерела даних

Вихідні таблиці: `DM.R27_fact_OKR_Goals`, `DM.vw_R27_dim_Employee_Access_List`

Колонки: `Index`, `PLAN_YEAR`, `USER_ACCESS_ID`, `order`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_Employee_OKR`, `t_HierarchyTypes`

Колонки: `dim_Admin_OS[USER_ACCESS_ID]`, `fact_Employee_OKR[PLAN_YEAR]`, `fact_Employee_OKR[USER_ACCESS_ID]`, `fact_Employee_OKR[order]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.ОКР.Кількість співробітників (Останній період оцінки)"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_Employee_OKR["fact_Employee_OKR"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

PLAN_YEAR → Рік ОКР; PLAN_YEAR → Значення останнього року оцінки ОКР; PLAN_YEAR → Значення передостаннього  року оцінки ОКР

Останнє доступне значення станом на дату поточного запису, релевантне відповідній оцінці результативності. Значення останнього року оцінки ОКР визначати в залежності від того, які дані доступні на поточний момент. Наприклад, протягом 2025 року в оцінку брати коефіцієнт індивідуального бонусу працівника за 2023-2024 роки, бо за 2025 рік оцінки ще немає. Тому останній рік буде 2024. На початку 2026 року, коли з'являться результати оцінки ОКР за 2025 рік, потрібно буде змістити період і брати 2025 рік.  <br>  <br>Для того, що визначити період (рік), за який виставлено індивідуальний бонус, потріб

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника/Редизайн-паспортної-частини`, `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди/Створити-блок-Виконання-OKR`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовує:** [GP.ОКР.Останній рік](../measures/gp-okr-ostannii-rik.md)

**Використовується в:** [GP.OKR.SVG.Bar chart](../measures/gp-okr-svg-bar-chart.md), [GP.ОКР.К-ть співробітників, що оцінюються.Текстове поле](../measures/gp-okr-k-t-spivrobitnykiv-shcho-otsiniuiutsia-tekstove-pole.md)

## Нотатки

_порожньо_
