# AC.BR.Референтне значення.Місяців без відпустки

*тека `Analytical Cases\Burnout_Risk\Export`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Export` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
IF(NOT(ISBLANK([AC.BR.Кількість місяців без якісної відпустки])),">9")
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["AC.BR.Референтне значення.Місяців без відпустки"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Утримання працівників](../report/utrymannia-pratsivnykiv.md)

## Пов'язані міри

**Використовує:** [AC.BR.Кількість місяців без якісної відпустки](../measures/ac-br-kilkist-misiatsiv-bez-iakisnoi-vidpustky.md)

## Нотатки

_порожньо_
