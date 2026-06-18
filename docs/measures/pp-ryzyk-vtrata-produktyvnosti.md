# PP.Ризик.Втрата продуктивності

*тека `Personal_Profile\Паспорт\Ризики`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Ризики` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _employee_id = SELECTEDVALUE('dim_Admin_OS'[EMPLOYEE_ID])
VAR _v =
	CALCULATE(
		SELECTEDVALUE('fact_Loss_of_Productivity'[Total_Risk_Productive_Name]),
		'fact_Loss_of_Productivity'[EMPLOYEE_ID] = _employee_id
	)
RETURN COALESCE(_v, "Дані відсутні")
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `EMPLOYEE_ID`, `Total_Risk_Productive_Name`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_Loss_of_Productivity`

Колонки: `dim_Admin_OS[EMPLOYEE_ID]`, `fact_Loss_of_Productivity[EMPLOYEE_ID]`, `fact_Loss_of_Productivity[Total_Risk_Productive_Name]`

### Схема

```mermaid
graph LR
  M["PP.Ризик.Втрата продуктивності"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
