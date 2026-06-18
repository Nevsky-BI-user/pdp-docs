# PP.OKR.Вага KR

*тека `Personal_Profile\Результативність та оцінка\OKR`*

## Бізнес-суть

KR_WEIGHT → Вага КР

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди/Створити-блок-Виконання-OKR`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Результативність та оцінка\OKR` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
AVERAGE('fact_OKR_Key_Results'[KR_WEIGHT])
```

### Джерела даних

Вихідні таблиці: `DM.R27_fact_OKR_Key_Results`

Колонки: `KR_WEIGHT`

Power Query: `fact_OKR_Key_Results`

### Залежності (таблиці й колонки)

Таблиці: `fact_OKR_Key_Results`

Колонки: `fact_OKR_Key_Results[KR_WEIGHT]`

### Схема

```mermaid
graph LR
  M["PP.OKR.Вага KR"]
  M --> fact_OKR_Key_Results["fact_OKR_Key_Results"]
```

## Нотатки

_порожньо_
