# PP.OKR.Колірна оцінка KR

*тека `Personal_Profile\Результативність та оцінка\OKR`*

!!! abstract "Джерела даних"
    `DM.R27_fact_OKR_Key_Results`

## Бізнес-суть

KR_COLOR_RATE → КР виконано; KR_COLOR_RATE → КР не виконано; KR_COLOR_RATE → Коефіцієнт колірної оцінки КР з плану

Якщо поле kr_color_rate >= 25 Якщо поле Calc_Performance_Desc_Rate <= 24.99 Якщо поле Calc_Performance_Desc_Rate < 25

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
AVERAGE('fact_OKR_Key_Results'[KR_COLOR_RATE])
```

### Джерела даних

Вихідні таблиці: `DM.R27_fact_OKR_Key_Results`

Колонки: `KR_COLOR_RATE`

Power Query: `fact_OKR_Key_Results`

### Залежності (таблиці й колонки)

Таблиці: `fact_OKR_Key_Results`

Колонки: `fact_OKR_Key_Results[KR_COLOR_RATE]`

### Схема

```mermaid
graph LR
  M["PP.OKR.Колірна оцінка KR"]
  M --> fact_OKR_Key_Results["fact_OKR_Key_Results"]
```

## Нотатки

_порожньо_
