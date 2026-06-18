# current_user_name

*тека `USER`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `USER` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _fullname =
    CALCULATE(
        VALUES('dim_Admin_OS'[EMPLOYEE_NAME]),
        'dim_Admin_OS'[EMPLOYEE_EMAIL] = USERPRINCIPALNAME()
    )
VAR _pos1 = FIND(" ", _fullname, 1, LEN(_fullname))
VAR _curr_time = HOUR(UTCNOW()+2)
VAR _intro =
    SWITCH(
        TRUE(),
        _curr_time < 10, ", доброго ранку!",
        _curr_time < 17, ", доброго дня!",
        ", доброго вечора!"
    )
RETURN 
IF(
    NOT ISBLANK(_fullname),
    MID(_fullname, _pos1 + 1, LEN(_fullname)) & _intro,
    ""
)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMPLOYEE_EMAIL`, `EMPLOYEE_NAME`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[EMPLOYEE_EMAIL]`, `dim_Admin_OS[EMPLOYEE_NAME]`

### Схема

```mermaid
graph LR
  M["current_user_name"]
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
