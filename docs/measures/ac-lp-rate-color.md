# AC.LP.Rate_color

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Loss_Productivity\Formatting` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _indicator = SELECTEDVALUE('t_AC Burnout'[Burnout_Indicator])
VAR _color = IF(_indicator = "Дані", "#F9F8F8", "#00FFFFFF")
RETURN
_color
```

## Джерела


Колонки: `Burnout_Indicator`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `t_AC Burnout`

Колонки: `t_AC Burnout[Burnout_Indicator]`

## Схема

```mermaid
graph LR
  M["AC.LP.Rate_color"]
  M --> t_AC Burnout
```

## Нотатки

_порожньо_
