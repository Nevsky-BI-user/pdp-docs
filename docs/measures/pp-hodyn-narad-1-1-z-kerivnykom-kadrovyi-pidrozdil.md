# PP.Годин нарад 1:1 з керівником (кадровий підрозділ)

*тека `Personal_Profile\Viva\Viva management & Coaching`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Viva\Viva management & Coaching` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR department = 
FIRSTNONBLANKVALUE(
		VALUES('dim_Admin_OS'[ORDER_NUM]),
		CALCULATE(SELECTEDVALUE('dim_Admin_OS'[PERSONNEL_UNIT])))

VAR __val =
CALCULATE(
	[PP.Годин нарад 1:1 з керівником (Холдинг)],
	dim_Unit[PERSONNEL_UNIT] = department)

RETURN __val
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_dim_Unit`

Колонки: `ORDER_NUM`, `PERSONNEL_UNIT`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `dim_Unit`

Колонки: `dim_Admin_OS[ORDER_NUM]`, `dim_Admin_OS[PERSONNEL_UNIT]`, `dim_Unit[PERSONNEL_UNIT]`

### Схема

```mermaid
graph LR
  M["PP.Годин нарад 1:1 з керівником (кадровий підрозділ)"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> dim_Unit["dim_Unit"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Personal Profile](../report/personal-profile.md) · [Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [PP.Годин нарад 1:1 з керівником (Холдинг)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-kholdynh.md)

## Нотатки

_порожньо_
