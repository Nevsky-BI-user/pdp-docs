# GP.Оцінка результативності пусто

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\SVG` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
IF(
	ISBLANK([GP.Оцінка результативності попередній рік]) && ISBLANK([GP.Оцінка результативності поточний рік]),
	"Дані"&UNICHAR(10)&"відсутні",
	""
)
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [GP.Оцінка результативності попередній рік](../measures/gp-otsinka-rezultatyvnosti-poperednii-rik.md), [GP.Оцінка результативності поточний рік](../measures/gp-otsinka-rezultatyvnosti-potochnyi-rik.md)


## Схема

```mermaid
graph LR
  M["GP.Оцінка результативності пусто"]
```

## Нотатки

_порожньо_
