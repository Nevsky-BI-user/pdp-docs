# PP.min_Y_axis_rcd

*тека `Personal_Profile\Життєвий цикл`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Життєвий цикл` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
MINX(
    VALUES('dim_Date'[Date]),
    [PP.РЦД]
) * 0.6
```

### Джерела даних


Колонки: `Date`

Power Query: `dim_Date`

### Залежності (таблиці й колонки)

Таблиці: `dim_Date`

Колонки: `dim_Date[Date]`

### Схема

```mermaid
graph LR
  M["PP.min_Y_axis_rcd"]
  M --> dim_Date["dim_Date"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовує:** [PP.РЦД](../measures/pp-rtsd.md)

## Нотатки

_порожньо_
