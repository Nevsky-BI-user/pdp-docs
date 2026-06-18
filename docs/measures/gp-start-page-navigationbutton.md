# GP.Start_Page_NavigationButton

*тека `Navigation\Group`*

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
VAR _min = CALCULATE(MIN('dim_Admin_OS'[path_length]))
VAR _max = CALCULATE(MAX('dim_Admin_OS'[path_length]))
VAR _res = 
	IF(
		_max - _min = 1,
		"Group Profile",
		IF(
			[Current_user] IN 
				{
				"yu.kosyuk@mhp.com.ua",
				"andriy.bulakh@mhp.com.ua",
				"a.h.bulakh@mhp.com.ua",
				"a.gromova@mhp.com.ua",
				"o.tsaltsalko@mhp.com.ua",
				"a.androsiuk@mhp.com.ua",
				"a.horbenko@mhp.com.ua",
				"o.sulima@mhp.com.ua",
				"v.alimov@mhp.com.ua",
				"v.korinevskyi@mhp.com.ua",
				"a.domanskyi@mhp.com.ua"
				} ||   SELECTEDVALUE('dim_Admin_OS'[USER_ROLE]) = "HRBP",
			"GP.NAV-0",
			SWITCH(
				[Current_User_Admin_Hierarchy_Level],
				1, "GP.NAV-1",
				2, "GP.NAV-1",
				3, "GP.NAV-1",
				4, "GP.NAV-1",
				5, "GP.NAV-1",
				6, "GP.NAV-1",
				7, "GP.NAV-1",
				8, "GP.NAV-1"
			)
		)
	)
RETURN _res
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `USER_ROLE`, `path_length`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[USER_ROLE]`, `dim_Admin_OS[path_length]`

### Схема

```mermaid
graph LR
  M["GP.Start_Page_NavigationButton"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Navigation

## Пов'язані міри

**Використовує:** [Current_User_Admin_Hierarchy_Level](../measures/current-user-admin-hierarchy-level.md), [Current_user](../measures/current-user.md)

## Нотатки

_порожньо_
