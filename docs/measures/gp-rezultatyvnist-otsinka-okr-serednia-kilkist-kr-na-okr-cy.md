# GP.Результативність.Оцінка OKR.Середня кількість KR на OKR.CY

*тека `Group_Profile\Результативність та оцінка\Оцінка OKR`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Результативність та оцінка\Оцінка OKR` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _res =
DIVIDE(
    [GP.Результативність.Оцінка OKR.Загальна кількість KR.CY], 
    [GP.Результативність.Оцінка OKR.Загальна кількість OKR.CY], BLANK())

RETURN _res
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["GP.Результативність.Оцінка OKR.Середня кількість KR на OKR.CY"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [GP.Результативність.Оцінка OKR.Загальна кількість KR.CY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-kr-cy.md), [GP.Результативність.Оцінка OKR.Загальна кількість OKR.CY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-okr-cy.md)

## Нотатки

_порожньо_
