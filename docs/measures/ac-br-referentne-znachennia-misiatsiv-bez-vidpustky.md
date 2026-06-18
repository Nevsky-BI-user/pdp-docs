# AC.BR.Референтне значення.Місяців без відпустки

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Export` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
IF(NOT(ISBLANK([AC.BR.Кількість місяців без якісної відпустки])),">9")
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [AC.BR.Кількість місяців без якісної відпустки](../measures/ac-br-kilkist-misiatsiv-bez-iakisnoi-vidpustky.md)


## Схема

```mermaid
graph LR
  M["AC.BR.Референтне значення.Місяців без відпустки"]
```

## Нотатки

_порожньо_
