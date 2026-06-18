# PP.Оцінка результативності.Самооцінка

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Результативність та оцінка\Результативність` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
CALCULATE(AVERAGE('fact_Employee_Performance'[Salf_Rate]))
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Employee_Performance_PBI`

Колонки: `Salf_Rate`

Power Query: `fact_Employee_Performance`

## Бізнес-суть

Salf_Rate → Оцінка кожного індикатора працівником

**Вимоги:** `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Таблиці: `fact_Employee_Performance`

Колонки: `fact_Employee_Performance[Salf_Rate]`

## Схема

```mermaid
graph LR
  M["PP.Оцінка результативності.Самооцінка"]
  M --> fact_Employee_Performance
```

## Нотатки

_порожньо_
