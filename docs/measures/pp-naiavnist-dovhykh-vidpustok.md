# PP.Наявність довгих відпусток

*тека `Personal_Profile\Здоров'я та благополуччя`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Здоров'я та благополуччя` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _qty = [PP.Кількість довгих відпусток]
VAR _days = [PP.Тривалість довгих відпусток]
VAR _res = 
	_qty & 
	IF(
		OR(ISBLANK(_days), _days = 0), 
		BLANK(), 
		" (" & _days & " дн.)"
	)
RETURN _res
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["PP.Наявність довгих відпусток"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Здоров'я та благополуччя

## Пов'язані міри

**Використовує:** [PP.Кількість довгих відпусток](../measures/pp-kilkist-dovhykh-vidpustok.md), [PP.Тривалість довгих відпусток](../measures/pp-tryvalist-dovhykh-vidpustok.md)

## Нотатки

_порожньо_
