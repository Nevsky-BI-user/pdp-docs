# GP.Результативність.Оцінка OKR.Середня кількість KR на OKR.CY

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Результативність та оцінка\Оцінка OKR` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _res =
DIVIDE(
    [GP.Результативність.Оцінка OKR.Загальна кількість KR.CY], 
    [GP.Результативність.Оцінка OKR.Загальна кількість OKR.CY], BLANK())

RETURN _res
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [GP.Результативність.Оцінка OKR.Загальна кількість KR.CY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-kr-cy.md), [GP.Результативність.Оцінка OKR.Загальна кількість OKR.CY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-okr-cy.md)


## Схема

```mermaid
graph LR
  M["GP.Результативність.Оцінка OKR.Середня кількість KR на OKR.CY"]
```

## Нотатки

_порожньо_
