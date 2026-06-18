# GP.Співробітники, які розуміють та демонструють цінності компанії (%)

*тека `Group_Profile\_Main\Індикатори здоров'я команди`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\_Main\Індикатори здоров'я команди` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _current_direction = 
	FIRSTNONBLANKVALUE(
		'dim_Admin_OS'[ORDER_NUM_2],
		MIN('dim_Admin_OS'[DIRECTION])
	)

VAR _current_sub_direction = 
	FIRSTNONBLANKVALUE(
		'dim_Admin_OS'[ORDER_NUM_2],
		MIN('dim_Admin_OS'[SUB_DIRECTION])
	)

VAR _current_email = 
	FIRSTNONBLANKVALUE(
		'dim_Admin_OS'[ORDER_NUM_2],
		MIN('dim_Admin_OS'[EMPLOYEE_EMAIL])
	)
VAR _current_user = USERPRINCIPALNAME()

VAR _direction_res = 
CALCULATE(
	SUM('fact_EXCEL_Group_Profile_General_Metric'[Value_Knowledge]),
	FILTER(
		'fact_EXCEL_Group_Profile_General_Metric',
		'fact_EXCEL_Group_Profile_General_Metric'[Record_Type] = "DIRECTION"
		&&'fact_EXCEL_Group_Profile_General_Metric'[Direction_Name] = _current_direction))

VAR _sub_direction_res = 
CALCULATE(
	SUM('fact_EXCEL_Group_Profile_General_Metric'[Value_Knowledge]),
	FILTER(
		'fact_EXCEL_Group_Profile_General_Metric',
		fact_EXCEL_Group_Profile_General_Metric[Record_Type] = "SUBDIRECTION"
		&& 'fact_EXCEL_Group_Profile_General_Metric'[Direction_Name] = _current_sub_direction))

VAR top_employee_list = 
SELECTCOLUMNS(
	FILTER(
	ALL('dim_Admin_OS'), 
	'dim_Admin_OS'[POSITION_CATEGORY_DETAIL] = "Топ-менеджмент" 
	|| 'dim_Admin_OS'[EMPLOYEE_EMAIL] in 
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
            "a.domanskyi@mhp.com.ua",
            "d.konogray@mhp.com.ua",
            "r.zvonenko@mhp.com.ua",
            "s.p.nikolaiev@mhp.com.ua",
            "a.evshel@mhp.com.ua",
            "t.sakhno@mhp.com.ua",
            "i.zakharchuk@mhp.com.ua",
            "yu.polovyna@mhp.com.ua",
            "o.neskromnyy@mhp.com.ua",
            "n.heizburh@mhp.com.ua",
            "ole.va.moroz@mhp.com.ua",
            "i.savinska@mhp.com.ua",
            "v.malakhova@mhp.com.ua",
            "a.kiriiak@mhp.com.ua",
            "t.hrytseniuk@mhp.com.ua",
            "s.perepichka@mhp.com.ua",
            "o.pasko@mhp.com.ua",
            "m.vyshnevetskyi@mhp.com.ua",
            "ka.m.shevchenko@mhp.com.ua",
            "i.tverdokhlib@mhp.com.ua",
            "d.i.mazurenko@mhp.com.ua",
            "d.bohdanova@mhp.com.ua",
            "v.o.gusak@mhp.com.ua",
            "v.vorontsov@mhp.com.ua",
            "srv_powerbi_ebitda@mhp.com.ua",
            "o.tsaltsalko0@mhpo365.onmicrosoft.com"
        }),
	"EmailColumn", 'dim_Admin_OS'[EMPLOYEE_EMAIL])

VAR _res =
IF(_current_user in top_employee_list, _direction_res)

RETURN
IF(
	ISBLANK(_res),
	"-", 
	TRIM(_res) & "%"
)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DWH.t_SPO_HR_Group_Profile_General_Metric`

Колонки: `DIRECTION`, `Direction_Name`, `EMPLOYEE_EMAIL`, `ORDER_NUM_2`, `POSITION_CATEGORY_DETAIL`, `Record_Type`, `SUB_DIRECTION`, `Value_Knowledge`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_EXCEL_Group_Profile_General_Metric`

Колонки: `dim_Admin_OS[DIRECTION]`, `dim_Admin_OS[EMPLOYEE_EMAIL]`, `dim_Admin_OS[ORDER_NUM_2]`, `dim_Admin_OS[POSITION_CATEGORY_DETAIL]`, `dim_Admin_OS[SUB_DIRECTION]`, `fact_EXCEL_Group_Profile_General_Metric[Direction_Name]`, `fact_EXCEL_Group_Profile_General_Metric[Record_Type]`, `fact_EXCEL_Group_Profile_General_Metric[Value_Knowledge]`

### Схема

```mermaid
graph LR
  M["GP.Співробітники, які розуміють та демонструють цінності компанії (%)"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_EXCEL_Group_Profile_General_Metric["fact_EXCEL_Group_Profile_General_Metric"]
```

---

## Бізнес-суть

**Бізнес-назва:** Співробітники, які розуміють та демонструють цінності компанії (%)

### Опис із ТЗ

Значення виводити у відсотках %

**Вимоги (ТЗ):**

- [Командний профіль › Паспортна частина групового профілю › Редизайн паспортної частини групового профілю](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%9A%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C/%D0%9F%D0%B0%D1%81%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%B0%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%D0%BD%D0%B0%20%D0%B3%D1%80%D1%83%D0%BF%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8E/%D0%A0%D0%B5%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%20%D0%BF%D0%B0%D1%81%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%BE%D1%97%20%D1%87%D0%B0%D1%81%D1%82%D0%B8%D0%BD%D0%B8%20%D0%B3%D1%80%D1%83%D0%BF%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8E)

## На сторінках звіту

- [Group Profile](../report/group-profile.md) — Версія 2 › Індикатори здоров'я команди

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
