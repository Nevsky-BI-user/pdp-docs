# GP.Середня кількість днів невикористаної відпустки співробітником

*тека `Group_Profile\_Main\Дані про команду`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\Дані про команду` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
TRIM( 
		COALESCE( 
			FORMAT( [AC.Середня кількість днів невикористаної відпустки], "0.00" ), "-"
		)
	)

// VAR _admin =
//     AVERAGEX( 
//         VALUES( dim_Admin_OS[USER_ACCESS_ID] ), 
//         CALCULATE( 
//             SUM('fact_Metrics'[VACATION_RESERVE_BY_MAIN_POSITION])
//         )
//     )
// VAR _admin_lt =
//     CALCULATE(
//         AVERAGEX( 
//             VALUES( dim_Admin_OS[USER_ACCESS_ID] ), 
//             CALCULATE( 
//                 SUM('fact_Metrics'[VACATION_RESERVE_BY_MAIN_POSITION])
//             )
//         ),
//         TREATAS(VALUES( dim_Admin_LT_OS[USER_ACCESS_ID] ), fact_Employee_List[USER_ACCESS_ID])
//     )
// VAR _res = 
//     SWITCH(
//         SELECTEDVALUE( t_HierarchyTypes[Index] ),
//         0, _admin_lt,
//         1, _admin
//     )
// RETURN
//     TRIM( 
//         COALESCE( 
//             FORMAT( _res, "0.00" ), "-"
//         )
//     )
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `Index`, `USER_ACCESS_ID`, `VACATION_RESERVE_BY_MAIN_POSITION`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_Employee_List`, `fact_Metrics`, `t_HierarchyTypes`

Колонки: `dim_Admin_OS[USER_ACCESS_ID]`, `fact_Employee_List[USER_ACCESS_ID]`, `fact_Metrics[VACATION_RESERVE_BY_MAIN_POSITION]`, `t_HierarchyTypes[Index]`

### Схема

```mermaid
graph LR
  M["GP.Середня кількість днів невикористаної відпустки співробітником"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_Employee_List["fact_Employee_List"]
  M --> fact_Metrics["fact_Metrics"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
```

---

## Бізнес-суть

VACATION_RESERVE_BY_MAIN_POSITION → Залишок відпустки

Це залишок днів відпусток, по яким формується резерв відпусток по підприємству /п)  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [ DM.vw_R27_fact_Vacation_Reserve].  <br>Цифру округлювати до цілих в більшу сторону, якщо цифра після коми 5-9, і в меншу сторону, якщо цифра після коми 0-4.  <br>Не включати в MVP, але потрібно буде додати цей же показник, але в роках. Це відношення норми днів відпусток до залишку відпусток. Норма днів відпусток - відсутній в джерелах даних, потрібно досліджувати.

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Здоров'я-та-благополуччя-працівника`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [AC.Середня кількість днів невикористаної відпустки](../measures/ac-serednia-kilkist-dniv-nevykorystanoi-vidpustky.md)

## Нотатки

_порожньо_
