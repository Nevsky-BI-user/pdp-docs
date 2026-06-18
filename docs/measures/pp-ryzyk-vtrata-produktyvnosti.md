# PP.Ризик.Втрата продуктивності

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Ризики` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _employee_id = SELECTEDVALUE('dim_Admin_OS'[EMPLOYEE_ID])
VAR _v =
	CALCULATE(
		SELECTEDVALUE('fact_Loss_of_Productivity'[Total_Risk_Productive_Name]),
		'fact_Loss_of_Productivity'[EMPLOYEE_ID] = _employee_id
	)
RETURN COALESCE(_v, "Дані відсутні")
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `EMPLOYEE_ID`, `Total_Risk_Productive_Name`

Power Query: `dim_Admin_OS`

## Бізнес-суть

Total_Risk_Productive_Name → Ризик втрати продуктивності

**Вимоги:** `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника/Редизайн-паспортної-частини`, `Кейс-Втрати-Продуктивності-Працівників`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Таблиці: `dim_Admin_OS`, `fact_Loss_of_Productivity`

Колонки: `dim_Admin_OS[EMPLOYEE_ID]`, `fact_Loss_of_Productivity[EMPLOYEE_ID]`, `fact_Loss_of_Productivity[Total_Risk_Productive_Name]`

## Схема

```mermaid
graph LR
  M["PP.Ризик.Втрата продуктивності"]
  M --> dim_Admin_OS
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
