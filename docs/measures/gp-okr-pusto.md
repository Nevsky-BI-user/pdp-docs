# GP.OKR пусто

*тека `Group_Profile\_Main\SVG`*

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовує:** [GP.OKR  попередній рік](../measures/gp-okr-poperednii-rik.md), [GP.OKR  поточний рік](../measures/gp-okr-potochnyi-rik.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\SVG` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
IF(
	ISBLANK([GP.OKR  поточний рік]) && ISBLANK([GP.OKR  попередній рік]),
	"Дані"&UNICHAR(10)&"відсутні",
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
  M["GP.OKR пусто"]
```

## Нотатки

_порожньо_
