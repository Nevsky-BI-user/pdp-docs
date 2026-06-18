# GP.ОКР.Середня оцінка команди.Текстове поле

*тека `Group_Profile\_Main\ОКР`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\ОКР` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _rate_value = [GP.ОКР.Середня оцінка команди.Значення]

VAR _color = [GP.ОКР.Середня оцінка команди.Колір]
RETURN 
    IF(
        ISBLANK(_rate_value),
        "Дані відсутні",
         _color & ", " & TRIM(_rate_value)
    )
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["GP.ОКР.Середня оцінка команди.Текстове поле"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [GP.ОКР.Середня оцінка команди.Значення](../measures/gp-okr-serednia-otsinka-komandy-znachennia.md), [GP.ОКР.Середня оцінка команди.Колір](../measures/gp-okr-serednia-otsinka-komandy-kolir.md)

## Нотатки

_порожньо_
