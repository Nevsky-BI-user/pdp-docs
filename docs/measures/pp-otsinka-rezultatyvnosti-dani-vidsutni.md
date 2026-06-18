# PP.Оцінка результативності.Дані відсутні

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Результативність` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
IF(
    ISBLANK([PP.Оцінка результативності.Керівником.Total])
    && ISBLANK([PP.Оцінка результативності.Керівником])
    && ISBLANK([PP.Оцінка результативності.Самооцінка.Total])
    && ISBLANK([PP.Оцінка результативності.Самооцінка]), 
    "Дані відсутні", 
    ""
)
```

## Джерела

—

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [PP.Оцінка результативності.Керівником](../measures/pp-otsinka-rezultatyvnosti-kerivnykom.md), [PP.Оцінка результативності.Керівником.Total](../measures/pp-otsinka-rezultatyvnosti-kerivnykom-total.md), [PP.Оцінка результативності.Самооцінка](../measures/pp-otsinka-rezultatyvnosti-samootsinka.md), [PP.Оцінка результативності.Самооцінка.Total](../measures/pp-otsinka-rezultatyvnosti-samootsinka-total.md)


## Схема

```mermaid
graph LR
  M["PP.Оцінка результативності.Дані відсутні"]
```

## Нотатки

_порожньо_
