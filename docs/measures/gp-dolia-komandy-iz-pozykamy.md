# GP.Доля команди із позиками

*тека `Group_Profile\TRS` · формат `0.00%;-0.00%;0.00%`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\TRS` |
| formatString | `0.00%;-0.00%;0.00%` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
//************* ROLE FILTERS **************
VAR _roleIndex = SELECTEDVALUE ( 't_HierarchyTypes'[Index], 1 )   -- 0 = LT, 1 = Admin
VAR _filter_lt = TREATAS ( VALUES ( 'dim_Admin_LT_OS'[USER_ACCESS_ID] ),dim_Admin_OS[USER_ACCESS_ID] )

/* *********** ADMIN *********** */
VAR _admin = 
DIVIDE(
    CALCULATE(
        DISTINCTCOUNT('fact_Repayment_Credit'[USER_ACCESS_ID]),
        'fact_Repayment_Credit'[ACTION_END_DATE] > TODAY()),
    [GP.Кількість співробітників всього, чол. - Integer])

/* *********** LT *********** */
VAR _admin_lt =
DIVIDE(
    CALCULATE(
        DISTINCTCOUNT('fact_Repayment_Credit'[USER_ACCESS_ID]),
        'fact_Repayment_Credit'[ACTION_END_DATE] > TODAY(),
        _filter_lt),
    [GP.Кількість співробітників всього, чол. - Integer])

VAR _res =
	SWITCH (
		_roleIndex,
		0, _admin_lt,    -- LT
		1, _admin,       -- Admin
		_admin
	)
RETURN 
COALESCE(_res, "-")
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_Repayment_Credit_PDP`

Колонки: `ACTION_END_DATE`, `Index`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_Repayment_Credit`, `t_HierarchyTypes`

Колонки: `dim_Admin_LT_OS[USER_ACCESS_ID]`, `dim_Admin_OS[USER_ACCESS_ID]`, `fact_Repayment_Credit[ACTION_END_DATE]`, `fact_Repayment_Credit[USER_ACCESS_ID]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Доля команди із позиками"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_Repayment_Credit["fact_Repayment_Credit"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

**Бізнес-назва:** Доля команди із позиками

### Опис із ТЗ

Потрібно підрахувати кількість працівників у команді, по яким є записи в таблиці DM.`vw_R27_fact_Repayment_Credit_PDP` та поле `action_end_date`>поточна дата (діюча позика) та поділити на поточну кількість членів команди. В деталізацію вивести ПІБ таких працівників, вид і розмір позики, дати видачі та погашення.

??? note "Поля-джерела та пов'язані бізнес-метрики (1)"
    | Поле | Бізнес-метрики |
    |---|---|
    | `ACTION_END_DATE` | Доля команди із позиками |

**Вимоги (ТЗ):**

- [Командний профіль › Сторінка TRS команди › Доопрацювання сторінки TRS](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%9A%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C/%D0%A1%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0%20TRS%20%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8/%D0%94%D0%BE%D0%BE%D0%BF%D1%80%D0%B0%D1%86%D1%8E%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F%20%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8%20TRS)

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [GP.Кількість співробітників всього, чол. - Integer](../measures/gp-kilkist-spivrobitnykiv-vsoho-chol-integer.md)

## Нотатки

_порожньо_
