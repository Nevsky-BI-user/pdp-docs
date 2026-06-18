# PP.button_detalization_font_color

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
IF(
	ISBLANK(COUNTROWS('fact_Employee_List')),
	"#9A0303",
	"#003A5D"
)
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

—

## Схема

```mermaid
graph LR
  M["PP.button_detalization_font_color"]
```

## Нотатки

_порожньо_
