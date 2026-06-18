# fact_TRS_Plan

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_TRS_Plan` |
| Джерела | `DM.vw_R27_fact_TRS_Plan_PDP` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| PERIOD | dateTime | PERIOD |  |
| EMPLOYEE_NAME | string | EMPLOYEE_NAME |  |
| IS_ACTIVE | boolean | IS_ACTIVE |  |
| ACCRUAL_ORG_CODE | string | ACCRUAL_ORG_CODE |  |
| ACCRUAL_ORG_NAME | string | ACCRUAL_ORG_NAME |  |
| CATEGORY_NAME | string | CATEGORY_NAME |  |
| IS_ACTUAL | boolean | IS_ACTUAL |  |
| START_DATE | dateTime | START_DATE |  |
| END_DATE | dateTime | END_DATE |  |
| TARIFF_RATE_TYPE_CODE | string | TARIFF_RATE_TYPE_CODE |  |
| CURR_TARIFF_RATE_TYPE_CODE | string | CURR_TARIFF_RATE_TYPE_CODE |  |
| MIN_TARIFF_RATE | double | MIN_TARIFF_RATE |  |
| CALC_TYPE_CODE | string | CALC_TYPE_CODE |  |
| BONUS_YEAR_SALARY_CNT | double | BONUS_YEAR_SALARY_CNT |  |
| BONUS_QUARTER_SALARY_CNT | double | BONUS_QUARTER_SALARY_CNT |  |
| BONUS_MONTH_SALARY_CNT | double | BONUS_MONTH_SALARY_CNT |  |
| INIT_PAYMENT_PLAN_SUM | double | INIT_PAYMENT_PLAN_SUM |  |
| ACCRUAL_ORG_BASE_CODE | string | ACCRUAL_ORG_BASE_CODE |  |
| PAYMENT_PLAN_SUM | double | PAYMENT_PLAN_SUM |  |
| FTE_FACT | double | FTE_FACT |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| ACCRUAL_ORG_BASE_MEASURE_ID | string | ACCRUAL_ORG_BASE_MEASURE_ID |  |
| ACCRUAL_ORG_ADD_MEASURE_ID | string | ACCRUAL_ORG_ADD_MEASURE_ID |  |
| ACCRUAL_ORG_BASE_ID | string | ACCRUAL_ORG_BASE_ID |  |
| ACCRUAL_ORG_ADD_ID | string | ACCRUAL_ORG_ADD_ID |  |
| EMPLOYMENT_TYPE_ID | string | EMPLOYMENT_TYPE_ID |  |
| BONES_SIZE | double | BONES_SIZE |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| STATUS_KEY | string | STATUS_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| POSITION_KEY | string | POSITION_KEY |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | DIVISION_PERSON_ID | `dim_Person` | PERSON_KEY |
| from | DIVISION_PERSON_ID | `dim_Unit` | UNIT_KEY |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | EMPLOYMENT_TYPE_ID | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | OFFICE_ON_POSITION_KEY | `dim_Office` | OFFICE_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | POSITION_KEY | `dim_Position` | POSITION_CODE_KEY |
| from | ACCRUAL_ORG_NAME | `dim_TRS_categories` | TRS_CATEGORY |
| from | PERIOD | `dim_Date` | Date |

## Пов'язані міри

Усього: 43.
- ['PP.Роз''їзний характер роботи, %'](../measures/pp-roziznyi-kharakter-roboty.md)
- ['PP.Роз''їзний характер роботи, грн'](../measures/pp-roziznyi-kharakter-roboty-hrn.md)
- [GP.Виконання плану ФОП YTD (%)](../measures/gp-vykonannia-planu-fop-ytd.md)
- [GP.Доля команди з доплатою за роз’їзний характер роботи, %](../measures/gp-dolia-komandy-z-doplatoiu-za-roziznyi-kharakter-roboty.md)
- [GP.Доля команди з доплатою за шкідливі умови праці, %](../measures/gp-dolia-komandy-z-doplatoiu-za-shkidlyvi-umovy-pratsi.md)
- [GP.Доля команди з квартальню премією, %](../measures/gp-dolia-komandy-z-kvartalniu-premiieiu.md)
- [GP.Доля команди з навчанням, %](../measures/gp-dolia-komandy-z-navchanniam.md)
- [GP.Доля команди з премією за місяць, %](../measures/gp-dolia-komandy-z-premiieiu-za-misiats.md)
- [GP.Доля команди з річним бонусом, %](../measures/gp-dolia-komandy-z-richnym-bonusom.md)
- [GP.Доля команди з щомісячною премією, %](../measures/gp-dolia-komandy-z-shchomisiachnoiu-premiieiu.md)
- [GP.Доля команди із премією за внутрішнє тренерство, %](../measures/gp-dolia-komandy-iz-premiieiu-za-vnutrishnie-trenerstvo.md)
- [GP.Доля команди із премією за програмою «Приведи друга», %](../measures/gp-dolia-komandy-iz-premiieiu-za-prohramoiu-pryvedy-druha.md)
- [GP.Доля учасників команди із зміною зарплати (окладу), %](../measures/gp-dolia-uchasnykiv-komandy-iz-zminoiu-zarplaty-okladu.md)
- [GP.К-ть співробітників, що отримують виплати на оренду житла](../measures/gp-k-t-spivrobitnykiv-shcho-otrymuiut-vyplaty-na-orendu-zhytla.md)
- [GP.Опція по авто, %](../measures/gp-optsiia-po-avto.md)
- [GP.Різниця фіксованої винагороди (план).Максимальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-plan-maksymalnyi-riven.md)
- [GP.Різниця фіксованої винагороди (план).Мінімальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-plan-minimalnyi-riven.md)
- [GP.Середня зарплата (оклад)](../measures/gp-serednia-zarplata-oklad.md)
- [GP.Середні витрати на оренду житла](../measures/gp-seredni-vytraty-na-orendu-zhytla.md)
- [GP.Середній % зростання зарплати (окладу) за 12 міс](../measures/gp-serednii-zrostannia-zarplaty-okladu-za-12-mis.md)
- [GP.Середній розмір доплати за роз’їзний характер роботи](../measures/gp-serednii-rozmir-doplaty-za-roziznyi-kharakter-roboty.md)
- [GP.Середній розмір доплати за шкідливі умови праці](../measures/gp-serednii-rozmir-doplaty-za-shkidlyvi-umovy-pratsi.md)
- [GP.Середній розмір квартальної премії](../measures/gp-serednii-rozmir-kvartalnoi-premii.md)
- [GP.Середній розмір премії за внутрішнє тренерство](../measures/gp-serednii-rozmir-premii-za-vnutrishnie-trenerstvo.md)
- [GP.Середній розмір премії за місяць](../measures/gp-serednii-rozmir-premii-za-misiats.md)
- [GP.Середній розмір річного бонусу](../measures/gp-serednii-rozmir-richnoho-bonusu.md)
- [GP.Середній розмір щомісячної премії](../measures/gp-serednii-rozmir-shchomisiachnoi-premii.md)
- [GP.Середній цільовий розмір річної винагороди, до оподаткування](../measures/gp-serednii-tsilovyi-rozmir-richnoi-vynahorody-do-opodatkuvannia.md)
- [PP.Доплата за шкідливі умови праці, %](../measures/pp-doplata-za-shkidlyvi-umovy-pratsi.md)
- [PP.Доплата за шкідливі умови праці,грн](../measures/pp-doplata-za-shkidlyvi-umovy-pratsi-hrn.md)
- [PP.Квартальна премія](../measures/pp-kvartalna-premiia.md)
- [PP.Квартальна премія окладів](../measures/pp-kvartalna-premiia-okladiv.md)
- [PP.Оклад по годинах](../measures/pp-oklad-po-hodynakh.md)
- [PP.Оклад по днях](../measures/pp-oklad-po-dniakh.md)
- [PP.Оренда житла](../measures/pp-orenda-zhytla.md)
- [PP.Премія за місяць, %](../measures/pp-premiia-za-misiats.md)
- [PP.Премія за місяць, грн](../measures/pp-premiia-za-misiats-hrn.md)
- [PP.Розмір фіксованої винагороди плановий, за місяць ПОТОЧНИЙ](../measures/pp-rozmir-fiksovanoi-vynahorody-planovyi-za-misiats-potochnyi.md)
- [PP.Річний бонус](../measures/pp-richnyi-bonus.md)
- [PP.Річний бонус окладів](../measures/pp-richnyi-bonus-okladiv.md)
- [PP.Цільовий розмір річної винагороди, до оподаткування](../measures/pp-tsilovyi-rozmir-richnoi-vynahorody-do-opodatkuvannia.md)
- [PP.Щомісячна премія](../measures/pp-shchomisiachna-premiia.md)
- [PP.Щомісячна премія окладів](../measures/pp-shchomisiachna-premiia-okladiv.md)

## Нотатки

_порожньо_
