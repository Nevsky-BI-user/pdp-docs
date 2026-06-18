# PP.Річний бонус окладів

*тека `Personal_Profile\TRS`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _v = 
	CALCULATE(
		MAXX(
			'fact_Employee_List',
			'fact_Employee_List'[BONUS_YEAR_SALARY_CNT]
		)
	)

// VAR _v = 
//     CALCULATE(
//         MAXX(
//             'fact_TRS_Plan',
//             'fact_TRS_Plan'[BONUS_YEAR_SALARY_CNT]
//         ),
//         fact_TRS_Plan[IS_ACTUAL]=TRUE(),
//         fact_TRS_Plan[CALC_TYPE_CODE]="UAH",
//         fact_TRS_Plan[category_name]="Фіксована винагорода"
//     )
RETURN "Окладів: "&_v
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_TRS_Plan_PDP`

Колонки: `BONUS_YEAR_SALARY_CNT`, `CALC_TYPE_CODE`, `IS_ACTUAL`, `category_name`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`, `fact_TRS_Plan`

Колонки: `fact_Employee_List[BONUS_YEAR_SALARY_CNT]`, `fact_TRS_Plan[BONUS_YEAR_SALARY_CNT]`, `fact_TRS_Plan[CALC_TYPE_CODE]`, `fact_TRS_Plan[IS_ACTUAL]`, `fact_TRS_Plan[category_name]`

### Схема

```mermaid
graph LR
  M["PP.Річний бонус окладів"]
  M --> fact_Employee_List["fact_Employee_List"]
  M --> fact_TRS_Plan["fact_TRS_Plan"]
```

---

## Бізнес-суть

BONUS_YEAR_SALARY_CNT → Премія річна кіл-ть окладів; BONUS_YEAR_SALARY_CNT → Річний бонус; BONUS_YEAR_SALARY_CNT → Доля команди з річним бонусом, %; category_name → Назва блоку

Станом на дату події <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [DM.vw_R27_fact_Employee_List_PDP]  <br>Відібрати записи по працівнику по працівнику [person_key], періоду [Period], організації [organization_key], підрозділу [division_key], посаді [position_key]<br> BONUS_YEAR_SALARY_CNT - кількість окладів  <br>Розмір премії = Min_Tariff_Rate помножити на BONUS_MONTH_SALARY_CNT - сума (к-сть окладів*оклад)  <br>Якщо по працівнику записи відсутні, то показати прочерк "-". Відбір робити за період станом на 12 міс. тому  <br>BONUS_YEAR_SALARY_CNT- кількі

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Деталізація-на-сторінці-Винагорода`, `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка/Блок-Оцінка-компетенцій`, `Командний-профіль/Сторінка-TRS-команди`, `Командний-профіль/Сторінка-TRS-команди/Сторінка-Винагорода-групового-профілю#вимоги-до-звіту`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди/Блок-Оцінка-компетенцій-(груповий-профіль)`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
