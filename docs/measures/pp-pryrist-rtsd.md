# PP.Приріст РЦД

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Життєвий цикл` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _CurrentRCD = [PP.РЦД]
VAR _CurrentDate = MAX ( 'dim_Date'[Date] )
VAR _PrevDate =
    CALCULATE (
        LASTNONBLANK ( 'dim_Date'[Date], [PP.РЦД] ),
        FILTER (
            ALLSELECTED ( 'dim_Date'[Date] ),
            'dim_Date'[Date] < _CurrentDate
        )
    )
VAR _IsFirstPoint = ISBLANK ( _PrevDate )
VAR _PrevRCD =
    CALCULATE (
        [PP.РЦД],
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
    _Result
```

## Джерела


Колонки: `Date`

Power Query: `dim_Date`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.РЦД](../measures/pp-rtsd.md)

Таблиці: `dim_Date`

Колонки: `dim_Date[Date]`

## Схема

```mermaid
graph LR
  M["PP.Приріст РЦД"]
  M --> dim_Date
```

## Нотатки

_порожньо_
