# PP.Дата прийому в організацію (останній)

*тека `Personal_Profile\Загальна інформація`*

## Бізнес-суть

LAST_ORGANIZATION_HIRE_DATE → Стаж в організації (останній)  <br>Дата прийому

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _res = SELECTEDVALUE('fact_employee_seniority_by_month'[LAST_ORGANIZATION_HIRE_DATE])
RETURN 
	COALESCE(
		FORMAT(
			_res,
			"dd.mm.yyyy"
		),
		"-"
	)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_employee_seniority_by_month_PDP`

Колонки: `LAST_ORGANIZATION_HIRE_DATE`

Power Query: `fact_employee_seniority_by_month`

### Залежності (таблиці й колонки)

Таблиці: `fact_employee_seniority_by_month`

Колонки: `fact_employee_seniority_by_month[LAST_ORGANIZATION_HIRE_DATE]`

### Схема

```mermaid
graph LR
  M["PP.Дата прийому в організацію (останній)"]
  M --> fact_employee_seniority_by_month["fact_employee_seniority_by_month"]
```

## Нотатки

_порожньо_
