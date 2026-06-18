# GP.Кількість Ветеранів

*тека `Group_Profile\Загальна інформація` · формат `0;-0;0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Загальна інформація` |
| formatString | `0;-0;0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _filter_lt= TREATAS(VALUES( dim_Admin_LT_OS[USER_ACCESS_ID] ), 'fact_Employee_List'[USER_ACCESS_ID])
VAR _admin = 
	CALCULATE(
		COUNTROWS(VALUES('fact_Employee_List'[person_key])),
		ALL('dim_Admin_OS'[STATUS_NAME]),
		'dim_Person'[IS_VETERAN] = 1
	)
VAR _admin_lt = 
	CALCULATE(
		COUNTROWS(VALUES('fact_Employee_List'[person_key])),
		ALL('dim_Admin_OS'[STATUS_NAME]),
		'dim_Person'[IS_VETERAN] = 1,
		_filter_lt
	)
VAR _res = 
	SWITCH(
		SELECTEDVALUE('t_HierarchyTypes'[Index]),
		0, _admin_lt,
		1, _admin
	)
RETURN 
	TRIM(
		FORMAT(	
			COALESCE(_res, "-"), 
			"### ###" 
		) 
	)	
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_dim_Person_PDP`

Колонки: `IS_VETERAN`, `Index`, `STATUS_NAME`, `USER_ACCESS_ID`, `person_key`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `dim_Person`, `fact_Employee_List`, `t_HierarchyTypes`

Колонки: `dim_Admin_OS[STATUS_NAME]`, `dim_Person[IS_VETERAN]`, `fact_Employee_List[USER_ACCESS_ID]`, `fact_Employee_List[person_key]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Кількість Ветеранів"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> dim_Person["dim_Person"]
  M --> fact_Employee_List["fact_Employee_List"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

STATUS_NAME → Статус працівника; STATUS_NAME → Статус співробітника; IS_VETERAN → Статус Ветеран; IS_VETERAN → Кількість Ветеранів; IS_VETERAN → Кількість демобілізованих

Поле зберігається в довіднику [dm.vw_R27_dim_Employee_Status]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем [status_key].  <br>Поле Статус не може бути пустим, бо у працівника він завжди є. Поле зберігається в довіднику dm.vw_R27_dim_person ]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List], через відповідний зв’язок за ключем [person_key].  <br>Якщо 1 - Так, якщо 0 - Ні. Розрахункове поле. Підрахувати скільки прац

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду/Редизайн-сторінки-Загальна-інформація`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
