# GP.ОКР.Оцінка керівника.Колір

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
VAR _rate_value = [GP.ОКР.Оцінка керівника.Значення]
VAR _color = 
    SWITCH(
        TRUE(),
        ISBLANK(_rate_value), "Дані відсутні",
        _rate_value >= 101, "Суперзелений",
        _rate_value >= 91, "Зелений",
        _rate_value >= 75, "Жовто-Зелений",
        _rate_value >= 50, "Жовтий",
        _rate_value >= 25, "Жовто-червоний",
        _rate_value >= 0, "Червоний"
    )

RETURN _color
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["GP.ОКР.Оцінка керівника.Колір"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовує:** [GP.ОКР.Оцінка керівника.Значення](../measures/gp-okr-otsinka-kerivnyka-znachennia.md)

**Використовується в:** [GP.OKP.Color.Оцінка керівника.Текстове поле](../measures/gp-okp-color-otsinka-kerivnyka-tekstove-pole.md), [GP.ОКР.Оцінка керівника.Текстове поле](../measures/gp-okr-otsinka-kerivnyka-tekstove-pole.md)

## Нотатки

_порожньо_
