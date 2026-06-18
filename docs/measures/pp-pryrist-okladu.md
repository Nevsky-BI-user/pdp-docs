# PP.Приріст окладу

*тека `Personal_Profile\TRS`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
GrowthLabel(
VAR _CurrentRCD = [PP.Оклад]
VAR _CurrentDate = MAX ( 'dim_Date'[Date] )
VAR _PrevDate =
    CALCULATE (
        LASTNONBLANK ( 'dim_Date'[Date], [PP.Оклад] ),
        FILTER (
            ALLSELECTED ( 'dim_Date'[Date] ),
            'dim_Date'[Date] < _CurrentDate
        )
    )
VAR _IsFirstPoint = ISBLANK ( _PrevDate )
VAR _PrevRCD =
    CALCULATE (
        [PP.Оклад],
        'dim_Date'[Date] = _PrevDate
    )
VAR _GrowthPct =
    ( DIVIDE ( _CurrentRCD, _PrevRCD ) - 1 ) * 100
VAR _Result =
    SWITCH (
        TRUE (),
        ISBLANK ( _CurrentRCD ), BLANK (),
        _IsFirstPoint, 0,
        ISBLANK ( _PrevRCD ) || _PrevRCD = 0, BLANK (),
        _GrowthPct
    )
RETURN
    _Result)
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
  M["PP.Приріст окладу"]
  M --> dim_Date["dim_Date"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

**Використовує:** [PP.Оклад](../measures/pp-oklad.md)

## Нотатки

_порожньо_
