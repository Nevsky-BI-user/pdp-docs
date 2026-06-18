# GP.Кількість співробітників всього, чол.

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\Дані про команду` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _Admin_lt = 
    CALCULATETABLE(
        VALUES('dim_Admin_LT_OS'[USER_ACCESS_ID]),
        'dim_Admin_LT_OS'[USER_ROLE]  = "Адміністративний керівник"
    )

VAR _HRBP_lt = 
    CALCULATETABLE(
        VALUES(dim_Admin_LT_OS[USER_ACCESS_ID]),
        'dim_Admin_LT_OS'[USER_ROLE]  = "HRBP"
    )
VAR _Admin = 
	SWITCH(
		SELECTEDVALUE('t_HierarchyTypes'[HierarchyType]),
		"Hierarchy",
		CALCULATE(
			COUNTROWS(VALUES('dim_Admin_OS'[USER_ACCESS_ID])),
            'dim_Admin_OS'[USER_ROLE]  = "Адміністративний керівник"
		),
		"Lead Team",
		CALCULATE(
			COUNTROWS(VALUES('dim_Admin_OS'[USER_ACCESS_ID])),
			TREATAS(_Admin_lt, 'dim_Admin_OS'[USER_ACCESS_ID]),
            'dim_Admin_OS'[USER_ROLE]  = "Адміністративний керівник"
		)
	)

VAR _HRBP = 
	SWITCH(
		SELECTEDVALUE('t_HierarchyTypes'[HierarchyType]),
		"Hierarchy",
		CALCULATE(
			COUNTROWS(VALUES('dim_Admin_OS'[USER_ACCESS_ID])),
            'dim_Admin_OS'[USER_ROLE]  = "HRBP"
		),
		"Lead Team",
		CALCULATE(
			COUNTROWS(VALUES('dim_Admin_OS'[USER_ACCESS_ID])),
			TREATAS(_HRBP_lt, 'dim_Admin_OS'[USER_ACCESS_ID]),
            'dim_Admin_OS'[USER_ROLE]  = "HRBP"
		)
	)

VAR _res = 
    SWITCH(
        SELECTEDVALUE('dim_Admin_OS'[USER_ROLE]),
        "Адміністративний керівник", _Admin,
        "HRBP", _HRBP
    )

RETURN 
	TRIM(
		FORMAT(
			COALESCE(_res, "-"),
			"### ###"
		) 
	)
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `HierarchyType`, `USER_ACCESS_ID`, `USER_ROLE`

Power Query: `dim_Admin_OS`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `dim_Admin_OS`, `t_HierarchyTypes`

Колонки: `dim_Admin_LT_OS[USER_ACCESS_ID]`, `dim_Admin_LT_OS[USER_ROLE]`, `dim_Admin_OS[USER_ACCESS_ID]`, `dim_Admin_OS[USER_ROLE]`, `t_HierarchyTypes[HierarchyType]`

## Схема

```mermaid
graph LR
  M["GP.Кількість співробітників всього, чол."]
  M --> dim_Admin_OS
  M --> t_HierarchyTypes
```

## Нотатки

_порожньо_
