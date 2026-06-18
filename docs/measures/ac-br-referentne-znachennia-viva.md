# AC.BR.Референтне значення.Viva

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
IF(NOT(ISBLANK([AC.BR.Перепрацювання Viva])),">=1 год")
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [AC.BR.Перепрацювання Viva](../measures/ac-br-perepratsiuvannia-viva.md)


## Схема

```mermaid
graph LR
  M["AC.BR.Референтне значення.Viva"]
```

## Нотатки

_порожньо_
