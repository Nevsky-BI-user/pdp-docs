# PP.Надомний інвалід (квота)

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
COALESCE(
	SWITCH(
		SELECTEDVALUE('fact_Employee_List'[DISABLED_TYPE]),
		"Технічні з інвалідністю", "Так",
		"Ні"
	),
	"-"
)
```

## Джерела


Колонки: `DISABLED_TYPE`

Power Query: `fact_Employee_List`

## Бізнес-суть

Надомний інвалід (квота)

<br>  <br>Якщо 1 - Так, якщо 0 - Ні.

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[DISABLED_TYPE]`

## Схема

```mermaid
graph LR
  M["PP.Надомний інвалід (квота)"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
