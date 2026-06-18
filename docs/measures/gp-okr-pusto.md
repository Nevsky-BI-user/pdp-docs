# GP.OKR пусто

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
	ISBLANK([GP.OKR  поточний рік]) && ISBLANK([GP.OKR  попередній рік]),
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

Міри: [GP.OKR  попередній рік](../measures/gp-okr-poperednii-rik.md), [GP.OKR  поточний рік](../measures/gp-okr-potochnyi-rik.md)


## Схема

```mermaid
graph LR
  M["GP.OKR пусто"]
```

## Нотатки

_порожньо_
