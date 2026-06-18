# PP.Офіс (штат)

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
	SELECTEDVALUE('fact_Employee_List'[POSITION_OFFICE_ADRESS]),
	"-"
)
```

## Джерела


Колонки: `POSITION_OFFICE_ADRESS`

Power Query: `fact_Employee_List`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[POSITION_OFFICE_ADRESS]`

## Схема

```mermaid
graph LR
  M["PP.Офіс (штат)"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
