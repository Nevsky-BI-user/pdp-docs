# PP.OKR.Вага OKR

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Результативність та оцінка\OKR` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
AVERAGE('fact_OKR_Goals'[OKR_WEIGHT])
```

## Джерела

Вихідні таблиці: `DM.R27_fact_OKR_Goals`

Колонки: `OKR_WEIGHT`

Power Query: `fact_OKR_Goals`

## Бізнес-суть

OKR_WEIGHT → Вага ОКР

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди/Створити-блок-Виконання-OKR`

## Залежності

Таблиці: `fact_OKR_Goals`

Колонки: `fact_OKR_Goals[OKR_WEIGHT]`

## Схема

```mermaid
graph LR
  M["PP.OKR.Вага OKR"]
  M --> fact_OKR_Goals
```

## Нотатки

_порожньо_
