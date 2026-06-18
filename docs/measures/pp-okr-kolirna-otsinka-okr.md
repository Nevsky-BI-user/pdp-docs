# PP.OKR.Колірна оцінка OKR

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
SELECTEDVALUE('fact_OKR_Goals'[OKR_COLOR_RATE])
```

## Джерела

Вихідні таблиці: `DM.R27_fact_OKR_Goals`

Колонки: `OKR_COLOR_RATE`

Power Query: `fact_OKR_Goals`

## Бізнес-суть

OKR_COLOR_RATE → Колірна оцінка ОКР з плану

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди/Створити-блок-Виконання-OKR`

## Залежності

Таблиці: `fact_OKR_Goals`

Колонки: `fact_OKR_Goals[OKR_COLOR_RATE]`

## Схема

```mermaid
graph LR
  M["PP.OKR.Колірна оцінка OKR"]
  M --> fact_OKR_Goals
```

## Нотатки

_порожньо_
