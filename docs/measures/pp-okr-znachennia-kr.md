# PP.OKR.Значення KR

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
AVERAGE('fact_OKR_Key_Results'[KR_AVG_RATE])
```

## Джерела

Вихідні таблиці: `DM.R27_fact_OKR_Key_Results`

Колонки: `KR_AVG_RATE`

Power Query: `fact_OKR_Key_Results`

## Бізнес-суть

KR_AVG_RATE → Середньозважена оцінка KR з плану

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди/Створити-блок-Виконання-OKR`

## Залежності

Таблиці: `fact_OKR_Key_Results`

Колонки: `fact_OKR_Key_Results[KR_AVG_RATE]`

## Схема

```mermaid
graph LR
  M["PP.OKR.Значення KR"]
  M --> fact_OKR_Key_Results
```

## Нотатки

_порожньо_
