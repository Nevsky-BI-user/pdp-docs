# PP.Дата прийому в холдинг (неперервний)

*тека `Personal_Profile\Загальна інформація`*

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
VAR _res = SELECTEDVALUE('fact_employee_seniority_by_month'[LAST_HOLDING_HIRE_DATE])
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

Колонки: `LAST_HOLDING_HIRE_DATE`

Power Query: `fact_employee_seniority_by_month`

### Залежності (таблиці й колонки)

Таблиці: `fact_employee_seniority_by_month`

Колонки: `fact_employee_seniority_by_month[LAST_HOLDING_HIRE_DATE]`

### Схема

```mermaid
graph LR
  M["PP.Дата прийому в холдинг (неперервний)"]
  M --> fact_employee_seniority_by_month["fact_employee_seniority_by_month"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Життєвий цикл

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
