# GP.Кількість співробітників у декретній відпустці

*тека `Group_Profile\Загальна інформація` · формат `0;-0;0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Загальна інформація` |
| formatString | `0;-0;0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _filter_lt= TREATAS(VALUES( dim_Admin_LT_OS[USER_ACCESS_ID] ), 'fact_Employee_List'[USER_ACCESS_ID])
VAR _admin = 
CALCULATE(
	COUNTROWS(VALUES('fact_Employee_List'[person_key])),
	ALL('dim_Admin_OS'[STATUS_NAME]),
	KEEPFILTERS('fact_Employee_List'[is_maternity_leave] = 1)
)
VAR _admin_lt = 
CALCULATE(
	COUNTROWS(VALUES('fact_Employee_List'[person_key])),
	ALL('dim_Admin_OS'[STATUS_NAME]),
	KEEPFILTERS('fact_Employee_List'[is_maternity_leave] = 1),
	_filter_lt
)
VAR _res = 
	SWITCH(
		SELECTEDVALUE('t_HierarchyTypes'[Index]),
		0, _admin_lt,
		1, _admin
	)
RETURN 
	TRIM(
		FORMAT(	
			COALESCE(_res, "-"), 
			"### ###" 
		) 
	)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `Index`, `STATUS_NAME`, `USER_ACCESS_ID`, `is_maternity_leave`, `person_key`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_Employee_List`, `t_HierarchyTypes`

Колонки: `dim_Admin_OS[STATUS_NAME]`, `fact_Employee_List[USER_ACCESS_ID]`, `fact_Employee_List[is_maternity_leave]`, `fact_Employee_List[person_key]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Кількість співробітників у декретній відпустці"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_Employee_List["fact_Employee_List"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

**Бізнес-назва:** Кількість співробітників у декретній відпустці

### Опис із ТЗ

Розрахункове поле. Підрахувати скільки працівників у команді, де `is_maternity_leave` = 1   Потрібно рахувати унікальну к-ть, щоб двічі не рахували тих, в кого осн місце і сумісництво.

**Вимоги (ТЗ):**

- [Командний профіль › Сторінка Загальна інформація про команду](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%9A%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C/%D0%A1%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0%20%D0%97%D0%B0%D0%B3%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%20%D1%96%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D1%96%D1%8F%20%D0%BF%D1%80%D0%BE%20%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%83)

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
