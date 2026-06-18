# filtered_users_check

*тека `_Technical`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `_Technical` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _users_list =
	SUMMARIZE(
		'dim_Admin_OS',
		'dim_Admin_OS'[FULL_NAME],
		'dim_Admin_OS'[ORDER_NUM_2]
	)
VAR _res =
	CONCATENATEX (
		_users_list,
		'dim_Admin_OS'[FULL_NAME],
		", " & UNICHAR(10),
		'dim_Admin_OS'[ORDER_NUM_2],
		ASC
	)
RETURN
	_res
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `FULL_NAME`, `ORDER_NUM_2`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[FULL_NAME]`, `dim_Admin_OS[ORDER_NUM_2]`

### Схема

```mermaid
graph LR
  M["filtered_users_check"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
