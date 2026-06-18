# PP.Формат роботи (працівник)

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
	SELECTEDVALUE('fact_Employee_List'[EMP_WORK_FORMAT]),
	"-"
)
```

## Джерела


Колонки: `EMP_WORK_FORMAT`

Power Query: `fact_Employee_List`

## Бізнес-суть

EMP_WORK_FORMAT → Формат роботи

**Вимоги:** `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EMP_WORK_FORMAT]`

## Схема

```mermaid
graph LR
  M["PP.Формат роботи (працівник)"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
