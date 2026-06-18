# GP.Кількість співробітників всього, чол. - String

*тека `Group_Profile\_Main\Дані про команду`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\Дані про команду` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
			
TRIM(
	FORMAT(
		COALESCE([GP.Кількість співробітників всього, чол. - Integer], "-"),
		"### ###"
	))
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["GP.Кількість співробітників всього, чол. - String"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Group Profile](../report/group-profile.md) · [Під ризиком мобілізації](../report/pid-ryzykom-mobilizatsii.md)

## Пов'язані міри

**Використовує:** [GP.Кількість співробітників всього, чол. - Integer](../measures/gp-kilkist-spivrobitnykiv-vsoho-chol-integer.md)

**Використовується в:** [GP.Команда](../measures/gp-komanda.md)

## Нотатки

_порожньо_
