# GP.Рівень команди в ієрархії

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
FIRSTNONBLANKVALUE(
	'dim_Admin_OS'[ORDER_NUM_2],
	MIN('dim_Admin_OS'[EMP_HIERARCHY_LEVEL])
)
```

## Джерела

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMP_HIERARCHY_LEVEL`, `ORDER_NUM_2`

Power Query: `dim_Admin_OS`

## Бізнес-суть

EMP_HIERARCHY_LEVEL → Рівень в ієрархії

Якщо значення в полі відсутнє, то потрібно визначити проблему та виправити

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Індивідуальний-профіль-працівника`

## Залежності

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[EMP_HIERARCHY_LEVEL]`, `dim_Admin_OS[ORDER_NUM_2]`

## Схема

```mermaid
graph LR
  M["GP.Рівень команди в ієрархії"]
  M --> dim_Admin_OS
```

## Нотатки

_порожньо_
