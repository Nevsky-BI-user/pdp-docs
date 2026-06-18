# PP.Метрика.Розмір/ширина мережі 3м

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Метрики` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _v = [PP.Розмір мережі (співробітник, 3м)]
VAR _w = [PP.Ширина мережі (співробітник, 3м)]
RETURN
	IF(ISBLANK(_v), "Дані відсутні", FORMAT(_v, "0")) 
    & " / " & IF(ISBLANK(_w), "Дані відсутні", FORMAT(_w, "0"))
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.Розмір мережі (співробітник, 3м)](../measures/pp-rozmir-merezhi-spivrobitnyk-3m.md), [PP.Ширина мережі (співробітник, 3м)](../measures/pp-shyryna-merezhi-spivrobitnyk-3m.md)


## Схема

```mermaid
graph LR
  M["PP.Метрика.Розмір/ширина мережі 3м"]
```

## Нотатки

_порожньо_
