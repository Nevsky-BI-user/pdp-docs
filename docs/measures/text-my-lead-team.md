# text.My_lead_team

*тека `Navigation\Group`*

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
| displayFolder | `Navigation\Group` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SWITCH(
    SELECTEDVALUE('dim_Admin_OS'[USER_ROLE]),
    "HRBP", "Мої прямі підопічні",
    "Мої прямі підлеглі"
)
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
  M["text.My_lead_team"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

## Нотатки

_порожньо_
