# GP.Кількість співробітників у декретній відпустці

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Загальна інформація` |
| formatString | `0;-0;0` |
| dataType | — |
| Прихована | ні |

## DAX

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

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `Index`, `STATUS_NAME`, `USER_ACCESS_ID`, `is_maternity_leave`, `person_key`

Power Query: `dim_Admin_OS`

## Бізнес-суть

STATUS_NAME → Статус працівника; STATUS_NAME → Статус співробітника; is_maternity_leave → Кількість співробітників у декретній відпустці

Поле зберігається в довіднику [dm.vw_R27_dim_Employee_Status]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем [status_key].  <br>Поле Статус не може бути пустим, бо у працівника він завжди є. Розрахункове поле. Підрахувати скільки працівників у команді, де is_maternity_leave = 1  <br>Потрібно рахувати унікальну к-ть, щоб двічі не рахували тих, в кого осн місце і сумісництво.

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Таблиці: `dim_Admin_OS`, `fact_Employee_List`, `t_HierarchyTypes`

Колонки: `dim_Admin_OS[STATUS_NAME]`, `fact_Employee_List[USER_ACCESS_ID]`, `fact_Employee_List[is_maternity_leave]`, `fact_Employee_List[person_key]`, `t_HierarchyTypes[Index]`

## Схема

```mermaid
graph LR
  M["GP.Кількість співробітників у декретній відпустці"]
  M --> dim_Admin_OS
  M --> fact_Employee_List
  M --> t_HierarchyTypes
```

## Нотатки

_порожньо_
