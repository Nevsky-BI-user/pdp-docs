# PP.Зайнятих ставок фактично

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
	SELECTEDVALUE('fact_Employee_List'[FTE_FACT]),
	"-"
)
```

## Джерела


Колонки: `FTE_FACT`

Power Query: `fact_Employee_List`

## Бізнес-суть

FTE_FACT → Зайнятих ставок фактично

Поле завжди має значення, пусте поле не допускається

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[FTE_FACT]`

## Схема

```mermaid
graph LR
  M["PP.Зайнятих ставок фактично"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
