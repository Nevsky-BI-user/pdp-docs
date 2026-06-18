# PP.Відсоток зміни фіксованої винагороди

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | `0.00%;-0.00%;0.00%` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _Now = [PP.Розмір фіксованої винагороди плановий, за місяць ПОТОЧНИЙ]
VAR _YearAgo = [PP.Розмір фіксованої винагороди плановий, за місяць СТАНОМ НА РІК НАЗАД]
VAR _result = DIVIDE(_Now-COALESCE(_YearAgo, _Now),_YearAgo, "Дані відсутні")
RETURN _result
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.Розмір фіксованої винагороди плановий, за місяць ПОТОЧНИЙ](../measures/pp-rozmir-fiksovanoi-vynahorody-planovyi-za-misiats-potochnyi.md), [PP.Розмір фіксованої винагороди плановий, за місяць СТАНОМ НА РІК НАЗАД](../measures/pp-rozmir-fiksovanoi-vynahorody-planovyi-za-misiats-stanom-na-rik-nazad.md)


## Схема

```mermaid
graph LR
  M["PP.Відсоток зміни фіксованої винагороди"]
```

## Нотатки

_порожньо_
