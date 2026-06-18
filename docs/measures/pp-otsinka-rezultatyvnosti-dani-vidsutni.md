# PP.Оцінка результативності.Дані відсутні

*тека `Personal_Profile\Паспорт\Результативність`*

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

**Використовує:** [PP.Оцінка результативності.Керівником](../measures/pp-otsinka-rezultatyvnosti-kerivnykom.md), [PP.Оцінка результативності.Керівником.Total](../measures/pp-otsinka-rezultatyvnosti-kerivnykom-total.md), [PP.Оцінка результативності.Самооцінка](../measures/pp-otsinka-rezultatyvnosti-samootsinka.md), [PP.Оцінка результативності.Самооцінка.Total](../measures/pp-otsinka-rezultatyvnosti-samootsinka-total.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Результативність` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

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

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["PP.Оцінка результативності.Дані відсутні"]
```

## Нотатки

_порожньо_
