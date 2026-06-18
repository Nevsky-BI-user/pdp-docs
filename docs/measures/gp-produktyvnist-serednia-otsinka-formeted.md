# GP.Продуктивність.Середня Оцінка.Formeted

*тека `Group_Profile\_Main\Продуктивність`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\Продуктивність` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _res = [GP.Продуктивність.Середня оцінка команди.Значення]

RETURN
TRIM( 
        COALESCE( 
            SUBSTITUTE(FORMAT( _res, "#,0.00" ), ",", " "), "-"
        )
    )
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["GP.Продуктивність.Середня Оцінка.Formeted"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Group Profile](../report/group-profile.md) — Версія 2 › Індикатори здоров'я команди

## Пов'язані міри

**Використовує:** [GP.Продуктивність.Середня оцінка команди.Значення](../measures/gp-produktyvnist-serednia-otsinka-komandy-znachennia.md)

## Нотатки

_порожньо_
