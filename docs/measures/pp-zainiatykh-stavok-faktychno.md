# PP.Зайнятих ставок фактично

*тека `Personal_Profile\Загальна інформація`*

## Бізнес-суть

FTE_FACT → Зайнятих ставок фактично

Поле завжди має значення, пусте поле не допускається

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
COALESCE(
	SELECTEDVALUE('fact_Employee_List'[FTE_FACT]),
	"-"
)
```

### Джерела даних


Колонки: `FTE_FACT`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[FTE_FACT]`

### Схема

```mermaid
graph LR
  M["PP.Зайнятих ставок фактично"]
  M --> fact_Employee_List["fact_Employee_List"]
```

## Нотатки

_порожньо_
