# PP.Колір приросту РЦД

*тека `Personal_Profile\Життєвий цикл`*

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

**Використовує:** [PP.Приріст РЦД](../measures/pp-pryrist-rtsd.md)

---

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
VAR _Val = [PP.Приріст РЦД]
RETURN
    SWITCH(
        TRUE(),
        _Val > 0, "#1F7A47",
        _Val < 0, "#A82828",
        "#6B7B8E"
    )
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["PP.Колір приросту РЦД"]
```

## Нотатки

_порожньо_
