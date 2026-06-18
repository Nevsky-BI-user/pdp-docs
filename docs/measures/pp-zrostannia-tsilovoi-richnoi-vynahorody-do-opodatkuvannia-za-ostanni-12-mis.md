# PP.Зростання цільової річної винагороди, до оподаткування (за останні 12 міс.)

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | `#,0.0%;-#,0.0%;#,0.0%` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _Now = [PP.Цільовий розмір річної винагороди, до оподаткування]
VAR _Prev =  [PP.Цільовий розмір річної винагороди, до оподаткування (12 місяців назад)]
VAR _res = DIVIDE(_Now-COALESCE(_Prev, _Now),_Prev, "Дані відсутні")
RETURN _res
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.Цільовий розмір річної винагороди, до оподаткування](../measures/pp-tsilovyi-rozmir-richnoi-vynahorody-do-opodatkuvannia.md), [PP.Цільовий розмір річної винагороди, до оподаткування (12 місяців назад)](../measures/pp-tsilovyi-rozmir-richnoi-vynahorody-do-opodatkuvannia-12-misiatsiv-nazad.md)


## Схема

```mermaid
graph LR
  M["PP.Зростання цільової річної винагороди, до оподаткування (за останні 12 міс.)"]
```

## Нотатки

_порожньо_
