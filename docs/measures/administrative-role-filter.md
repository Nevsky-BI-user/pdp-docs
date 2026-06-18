# Administrative_role_filter

*тека `_Technical` · формат `0`*

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
| displayFolder | `_Technical` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
COUNTROWS(
    FILTER(
        'dim_Admin_OS', 
        SEARCH(USERPRINCIPALNAME(), dim_Admin_OS[path_column_email], , 0) > 0
    )
)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `path_column_email`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[path_column_email]`

### Схема

```mermaid
graph LR
  M["Administrative_role_filter"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

## Нотатки

_порожньо_
