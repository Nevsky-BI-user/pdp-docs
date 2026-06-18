# PP.Підрозділ 3

*тека `Personal_Profile\Загальна інформація`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
COALESCE(
	SELECTEDVALUE('dim_Admin_OS'[SUBDIVISION_LVL_3]),
	"-"
)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `SUBDIVISION_LVL_3`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[SUBDIVISION_LVL_3]`

### Схема

```mermaid
graph LR
  M["PP.Підрозділ 3"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Загальна інформація

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
