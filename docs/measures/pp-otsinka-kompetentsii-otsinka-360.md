# PP.Оцінка компетенцій.Оцінка 360

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | — |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
AVERAGE('fact_360_Assessment'[Competency_Rate])
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_360_Assessment`

Колонки: `Competency_Rate`

Power Query: `fact_360_Assessment`

### Залежності (таблиці й колонки)

Таблиці: `fact_360_Assessment`

Колонки: `fact_360_Assessment[Competency_Rate]`

### Схема

```mermaid
graph LR
  M["PP.Оцінка компетенцій.Оцінка 360"]
  M --> fact_360_Assessment["fact_360_Assessment"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [PP.SVG.Оцінка компетенцій.Загальна по блоках](../measures/pp-svg-otsinka-kompetentsii-zahalna-po-blokakh.md), [PP.SVG.Оцінка компетенцій.Компетенція](../measures/pp-svg-otsinka-kompetentsii-kompetentsiia.md), [PP.SVG.Оцінка компетенцій.Хітмап по блоках](../measures/pp-svg-otsinka-kompetentsii-khitmap-po-blokakh.md)

## Нотатки

_порожньо_
