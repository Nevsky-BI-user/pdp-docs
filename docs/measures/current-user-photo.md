# current_user_photo_

*тека `USER`*

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
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _url =
    CALCULATE(
        VALUES('dim_Admin_OS'[URL_FOTO]),
        'dim_Admin_OS'[EMPLOYEE_EMAIL] = USERPRINCIPALNAME()
    )
RETURN
IF(
    NOT ISBLANK(_url),
    "<div style='display:flex;justify-content:center;align-items:center;width:100%;height:100%;background:transparent;'>
        <img src='" & _url & "' width='150' height='150' style='border-radius:8px;object-fit:cover;background:transparent;'/>
    </div>",
    ""
)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMPLOYEE_EMAIL`, `URL_FOTO`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[EMPLOYEE_EMAIL]`, `dim_Admin_OS[URL_FOTO]`

### Схема

```mermaid
graph LR
  M["current_user_photo_"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

## Нотатки

_порожньо_
