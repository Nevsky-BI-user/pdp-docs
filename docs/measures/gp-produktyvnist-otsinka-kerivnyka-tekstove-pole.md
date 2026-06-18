# GP.Продуктивність.Оцінка керівника.Текстове поле

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
VAR _category = [GP.Продуктивність.Оцінка керівника.Категорія]
VAR _rate_value = [GP.Продуктивність.Оцінка керівника.Значення]
RETURN 
    --"Оцінка керівника - " &
    IF(
        ISBLANK(_rate_value),
        "Дані відсутні",
         _category & ", " & ROUND(_rate_value,2)
    )
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["GP.Продуктивність.Оцінка керівника.Текстове поле"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [GP.Продуктивність.Оцінка керівника.Значення](../measures/gp-produktyvnist-otsinka-kerivnyka-znachennia.md), [GP.Продуктивність.Оцінка керівника.Категорія](../measures/gp-produktyvnist-otsinka-kerivnyka-katehoriia.md)

## Нотатки

_порожньо_
