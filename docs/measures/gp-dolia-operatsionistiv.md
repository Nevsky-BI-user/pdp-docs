# GP.Доля операціоністів

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _filter_lt= TREATAS(VALUES( dim_Admin_LT_OS[USER_ACCESS_ID] ), 'fact_Employee_List'[USER_ACCESS_ID])
VAR _admin = 
	DIVIDE(
		CALCULATE(
			COUNTROWS('fact_Employee_List'), 
			'fact_Employee_List'[POSITION_CATEGORY_ORIGINAL] = "Операціоністи"
		),
		COUNTROWS('fact_Employee_List')
	)
VAR _admin_lt = 
	CALCULATE(
		DIVIDE(
			CALCULATE(
				COUNTROWS( 'fact_Employee_List' ),
				'fact_Employee_List'[POSITION_CATEGORY_ORIGINAL] = "Операціоністи"
			),
			COUNTROWS( 'fact_Employee_List' )
		),
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
			"0.00%"
		) 
	)
```

## Джерела


Колонки: `Index`, `POSITION_CATEGORY_ORIGINAL`, `USER_ACCESS_ID`

Power Query: `fact_Employee_List`

## Бізнес-суть

Доля операціоністів

Розрахункове поле: відношення кількості Операціоністів у команді до загальної кількості працівників.  <br>Відношення кількості працівників, для яких position_categoty_original = 'Операціоністи' до загальної чисельності команди (метрика Кількість співробітників всього, чол.)

**Вимоги:** `Командний-профіль/Сторінка-Загальна-інформація-про-команду`

## Залежності

Таблиці: `fact_Employee_List`, `t_HierarchyTypes`

Колонки: `fact_Employee_List[POSITION_CATEGORY_ORIGINAL]`, `fact_Employee_List[USER_ACCESS_ID]`, `t_HierarchyTypes[Index]`

## Схема

```mermaid
graph LR
  M["GP.Доля операціоністів"]
  M --> fact_Employee_List
  M --> t_HierarchyTypes
```

## Нотатки

_порожньо_
