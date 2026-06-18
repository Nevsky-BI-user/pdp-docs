# PP.Метрика.Розмір/ширина мережі 3м

*тека `Personal_Profile\Паспорт\Метрики`*

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

**Використовує:** [PP.Розмір мережі (співробітник, 3м)](../measures/pp-rozmir-merezhi-spivrobitnyk-3m.md), [PP.Ширина мережі (співробітник, 3м)](../measures/pp-shyryna-merezhi-spivrobitnyk-3m.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Метрики` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _v = [PP.Розмір мережі (співробітник, 3м)]
VAR _w = [PP.Ширина мережі (співробітник, 3м)]
RETURN
	IF(ISBLANK(_v), "Дані відсутні", FORMAT(_v, "0")) 
    & " / " & IF(ISBLANK(_w), "Дані відсутні", FORMAT(_w, "0"))
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["PP.Метрика.Розмір/ширина мережі 3м"]
```

## Нотатки

_порожньо_
