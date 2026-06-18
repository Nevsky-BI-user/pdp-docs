# PP.Підрозділ 1

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
COALESCE(
	SELECTEDVALUE('dim_Admin_OS'[SUBDIVISION_LVL_1]),
	"-"
)
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `SUBDIVISION_LVL_1`

Power Query: `dim_Admin_OS`

## Бізнес-суть

SUBDIVISION_LVL_1 → subdivision_lvl_1

**Вимоги:** `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)/Додаткові-вимоги-до-вітрини-Плинність`

## Залежності

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[SUBDIVISION_LVL_1]`

## Схема

```mermaid
graph LR
  M["PP.Підрозділ 1"]
  M --> dim_Admin_OS
```

## Нотатки

_порожньо_
