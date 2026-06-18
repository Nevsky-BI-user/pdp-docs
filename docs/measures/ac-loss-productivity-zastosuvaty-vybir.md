# AC.Loss_Productivity.Застосувати вибір

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Loss_Productivity\Formatting` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _v = 
	SWITCH(
		SELECTEDVALUE('t_HierarchyTypes'[HierarchyType]),
		"Hierarchy", CALCULATE(COUNTROWS(VALUES('fact_Loss_of_Productivity'[USER_ACCESS_ID]))),
		"Lead Team",
		CALCULATE(
			COUNTROWS(VALUES('fact_Loss_of_Productivity'[USER_ACCESS_ID])),
			TREATAS(VALUES(dim_Admin_LT_OS[USER_ACCESS_ID]), 'fact_Loss_of_Productivity'[USER_ACCESS_ID])
		)
	)
RETURN 
	"Застосувати вибір ("& 
		COALESCE(
			TRIM(
				FORMAT(
					COALESCE(_v, 0),
					"[uk-UA]# ##0"
				)
			),
			0
		) 
	& ")"
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `HierarchyType`, `USER_ACCESS_ID`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `fact_Loss_of_Productivity`, `t_HierarchyTypes`

Колонки: `fact_Loss_of_Productivity[USER_ACCESS_ID]`, `t_HierarchyTypes[HierarchyType]`

## Схема

```mermaid
graph LR
  M["AC.Loss_Productivity.Застосувати вибір"]
  M --> fact_Loss_of_Productivity
  M --> t_HierarchyTypes
```

## Нотатки

_порожньо_
