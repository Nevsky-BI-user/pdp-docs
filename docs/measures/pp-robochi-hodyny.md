# PP.Робочі години

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\_Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _v = SELECTEDVALUE('fact_Employee_List'[WORKING_HOURS])
RETURN 
	COALESCE(
		_v,
		"-"
	)
```

## Джерела


Колонки: `WORKING_HOURS`

Power Query: `fact_Employee_List`

## Бізнес-суть

WORKING_HOURS → Робочі години

**Вимоги:** `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[WORKING_HOURS]`

## Схема

```mermaid
graph LR
  M["PP.Робочі години"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
