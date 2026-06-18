# User_role_filter

*тека `USER` · формат `0`*

!!! abstract "Джерела даних"
    `DM.vw_R27_dim_Employee_Access_List`

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `USER` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
 VAR _selected_role = SELECTEDVALUE('dim_Admin_OS'[USER_ROLE])
 VAR _is_HRBP = 
    IF(
        CALCULATE(
            COUNTROWS('dim_Admin_OS'),
            'dim_Admin_OS'[USER_ROLE] = "HRBP"
        ) > 1,
        1
    )
 VAR _is_administrative_manager = 
     IF(
        CALCULATE(
            COUNTROWS('dim_Admin_OS'),
            'dim_Admin_OS'[USER_ROLE] = "Адміністративний керівник"
        ) >= 1,
        1
    )
VAR _res = 
    SWITCH(
        SELECTEDVALUE('dim_Admin_OS'[USER_ROLE]),
        "HRBP", IF(_is_HRBP = 1,1),
        IF(_is_administrative_manager = 1,1)
    )
RETURN _res
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `USER_ROLE`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[USER_ROLE]`

### Схема

```mermaid
graph LR
  M["User_role_filter"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

## Нотатки

_порожньо_
