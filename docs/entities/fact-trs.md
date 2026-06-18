# fact_TRS

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_TRS` |
| Джерела | `DM.vw_R27_fact_TRS_PDP` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Деталізація-на-сторінці-Винагорода`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Доопрацювання-сторінки-ТРС`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)/ТЗ.-Метрика-Небажана-плинність-(regretted-atrition-ratio)`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| PERIOD | dateTime | PERIOD |  |
| PAYMENTS_FACT_UAH | double | PAYMENTS_FACT_UAH |  |
| IS_MOBILIZED | string | IS_MOBILIZED |  |
| BUDGET_CODE | string | BUDGET_CODE |  |
| OBJECT_CODE | string | OBJECT_CODE |  |
| BUDGET_COST_ITEM | string | BUDGET_COST_ITEM |  |
| ACCRUAL_TYPES_KEY | string | ACCRUAL_TYPES_KEY |  |
| ACCRUAL_TYPE_NAME | string | ACCRUAL_TYPE_NAME |  |
| CATEGORY_OF_ACCRUAL_SORT | int64 | CATEGORY_OF_ACCRUAL_SORT |  |
| TRS_CATEGORY | string | TRS_CATEGORY |  |
| ORGANIZATION_KEY | string | ORGANIZATION_KEY |  |
| PERSON_KEY | string | PERSON_KEY |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| EMP_HEAD_ADMIN_ID | string | EMP_HEAD_ADMIN_ID |  |
| TAX_PIT_ID | string | TAX_PIT_ID |  |
| COST_CENTRE_KEY | string | COST_CENTRE_KEY |  |
| UNIT_KEY | string | UNIT_KEY |  |
| DIVISION_KEY | string | DIVISION_KEY |  |
| POSITION_KEY | string | POSITION_KEY |  |
| STATUS_KEY | string | STATUS_KEY |  |
| PAYMENTS_PLAN_UAH | double | PAYMENTS_PLAN_UAH |  |
| IS_PAYMENTS_PLAN | int64 | IS_PAYMENTS_PLAN |  |
| WAGE_RATE | double | WAGE_RATE |  |
| WAGE_RATE_TYPE | string | WAGE_RATE_TYPE |  |
| BONUS_YEAR_SALARY_CNT | double | BONUS_YEAR_SALARY_CNT |  |
| BONUS_QUARTER_SALARY_CNT | double | BONUS_QUARTER_SALARY_CNT |  |
| BONUS_MONTH_SALARY_CNT | double | BONUS_MONTH_SALARY_CNT |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| SUBCATEGORY_OF_ACCRUAL_TYPE | string | SUBCATEGORY_OF_ACCRUAL_TYPE |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | PERSON_KEY | `dim_Person` | PERSON_KEY |
| from | UNIT_KEY | `dim_Unit` | UNIT_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | POSITION_KEY | `dim_Position` | POSITION_CODE_KEY |
| from | ACCRUAL_TYPE_NAME | `dim_TRS_categories` | TRS_CATEGORY |
| from | PERIOD | `dim_Date` | Date |

## Пов'язані міри

Усього: 59.
- [GP.Виконання плану ФОП YTD (%)](../measures/gp-vykonannia-planu-fop-ytd.md)
- [GP.Доля команди з доплатою за роз’їзний характер роботи, % факт](../measures/gp-dolia-komandy-z-doplatoiu-za-roziznyi-kharakter-roboty-fakt.md)
- [GP.Доля команди з доплатою за шкідливі умови праці, % факт](../measures/gp-dolia-komandy-z-doplatoiu-za-shkidlyvi-umovy-pratsi-fakt.md)
- [GP.Доля команди з квартальною премією, % факт](../measures/gp-dolia-komandy-z-kvartalnoiu-premiieiu-fakt.md)
- [GP.Доля команди з премією за місяць, % факт](../measures/gp-dolia-komandy-z-premiieiu-za-misiats-fakt.md)
- [GP.Доля команди з річними бонусами, % факт](../measures/gp-dolia-komandy-z-richnymy-bonusamy-fakt.md)
- [GP.Доля команди з соціальними виплатами, %](../measures/gp-dolia-komandy-z-sotsialnymy-vyplatamy.md)
- [GP.Доля команди з щомісячною премією, % факт](../measures/gp-dolia-komandy-z-shchomisiachnoiu-premiieiu-fakt.md)
- [GP.Доля команди із доплатою за наставництво, %](../measures/gp-dolia-komandy-iz-doplatoiu-za-nastavnytstvo.md)
- [GP.Доля команди із премією МХП Зірки, %](../measures/gp-dolia-komandy-iz-premiieiu-mkhp-zirky.md)
- [GP.Доля команди із премією за Банк ідей, %](../measures/gp-dolia-komandy-iz-premiieiu-za-bank-idei.md)
- [GP.Доля команди із премією за збереження та розширення земельного банку, %](../measures/gp-dolia-komandy-iz-premiieiu-za-zberezhennia-ta-rozshyrennia-zemelnoho-banku.md)
- [GP.Доля команди із премією за програмою «Приведи друга», %](../measures/gp-dolia-komandy-iz-premiieiu-za-prohramoiu-pryvedy-druha.md)
- [GP.Доля команди із премією за сумісництво, факт](../measures/gp-dolia-komandy-iz-premiieiu-za-sumisnytstvo-fakt.md)
- [GP.Доля команди із проектним бонусом за стратегічні ІТ проєкти, %](../measures/gp-dolia-komandy-iz-proektnym-bonusom-za-stratehichni-it-proiekty.md)
- [GP.Доля команди із разовою премією за програмою визнання, %](../measures/gp-dolia-komandy-iz-razovoiu-premiieiu-za-prohramoiu-vyznannia.md)
- [GP.Доля команди із інвестиційним проєктним бонусом, %](../measures/gp-dolia-komandy-iz-investytsiinym-proiektnym-bonusom.md)
- [GP.Доля учасників команди із зміною зарплати (окладу), %](../measures/gp-dolia-uchasnykiv-komandy-iz-zminoiu-zarplaty-okladu.md)
- [GP.Різниця фіксованої винагороди (факт).Максимальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-fakt-maksymalnyi-riven.md)
- [GP.Різниця фіксованої винагороди (факт).Мінімальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-fakt-minimalnyi-riven.md)
- [GP.Середня заробітна плата](../measures/gp-serednia-zarobitna-plata.md)
- [GP.Середній % зростання зарплати (окладу) за 12 міс](../measures/gp-serednii-zrostannia-zarplaty-okladu-za-12-mis.md)
- [GP.Середній розмір доплат за суміщення, факт](../measures/gp-serednii-rozmir-doplat-za-sumishchennia-fakt.md)
- [GP.Середній розмір доплати за наставництво](../measures/gp-serednii-rozmir-doplaty-za-nastavnytstvo.md)
- [GP.Середній розмір доплати за роз’їзний характер роботи, факт](../measures/gp-serednii-rozmir-doplaty-za-roziznyi-kharakter-roboty-fakt.md)
- [GP.Середній розмір доплати за шкідливі умови праці, факт](../measures/gp-serednii-rozmir-doplaty-za-shkidlyvi-umovy-pratsi-fakt.md)
- [GP.Середній розмір квартальної премії, факт](../measures/gp-serednii-rozmir-kvartalnoi-premii-fakt.md)
- [GP.Середній розмір премії МХП Зірки](../measures/gp-serednii-rozmir-premii-mkhp-zirky.md)
- [GP.Середній розмір премії за Банк ідей](../measures/gp-serednii-rozmir-premii-za-bank-idei.md)
- [GP.Середній розмір премії за збереження та розширення земельного банку](../measures/gp-serednii-rozmir-premii-za-zberezhennia-ta-rozshyrennia-zemelnoho-banku.md)
- [GP.Середній розмір премії за місяць, факт](../measures/gp-serednii-rozmir-premii-za-misiats-fakt.md)
- [GP.Середній розмір премії за програмою «Приведи друга»](../measures/gp-serednii-rozmir-premii-za-prohramoiu-pryvedy-druha.md)
- [GP.Середній розмір проектного бонус за стратегічні ІТ проєкти](../measures/gp-serednii-rozmir-proektnoho-bonus-za-stratehichni-it-proiekty.md)
- [GP.Середній розмір разової премії за програмою визнання](../measures/gp-serednii-rozmir-razovoi-premii-za-prohramoiu-vyznannia.md)
- [GP.Середній розмір річного бонусу, факт](../measures/gp-serednii-rozmir-richnoho-bonusu-fakt.md)
- [GP.Середній розмір соціальної підтримки](../measures/gp-serednii-rozmir-sotsialnoi-pidtrymky.md)
- [GP.Середній розмір щомісячної премії, факт](../measures/gp-serednii-rozmir-shchomisiachnoi-premii-fakt.md)
- [GP.Середній розмір інвестиційного проєктного бонусу](../measures/gp-serednii-rozmir-investytsiinoho-proiektnoho-bonusu.md)
- [PP.Інвестиційний проєктний бонус](../measures/pp-investytsiinyi-proiektnyi-bonus.md)
- [PP.Інші доплати](../measures/pp-inshi-doplaty.md)
- [PP.Бейдж.Зірка МХП](../measures/pp-beidzh-zirka-mkhp.md)
- [PP.Доплата за наставництво](../measures/pp-doplata-za-nastavnytstvo.md)
- [PP.Доплати за суміщення](../measures/pp-doplaty-za-sumishchennia.md)
- [PP.Квартальні премії факт](../measures/pp-kvartalni-premii-fakt.md)
- [PP.Наставництво](../measures/pp-nastavnytstvo.md)
- [PP.Премія МХП Зірки](../measures/pp-premiia-mkhp-zirky.md)
- [PP.Премія за Банк ідей](../measures/pp-premiia-za-bank-idei.md)
- [PP.Премія за внутрішнє тренерство](../measures/pp-premiia-za-vnutrishnie-trenerstvo.md)
- [PP.Премія за збереження та розширення земельного банку](../measures/pp-premiia-za-zberezhennia-ta-rozshyrennia-zemelnoho-banku.md)
- [PP.Премія за програмою «Приведи друга»](../measures/pp-premiia-za-prohramoiu-pryvedy-druha.md)
- [PP.Проектний бонус за стратегічні ІТ проєкти](../measures/pp-proektnyi-bonus-za-stratehichni-it-proiekty.md)
- [PP.Разова премія за програмою визнання](../measures/pp-razova-premiia-za-prohramoiu-vyznannia.md)
- [PP.Розмір фіксованої винагороди плановий, за місяць СТАНОМ НА РІК НАЗАД](../measures/pp-rozmir-fiksovanoi-vynahorody-planovyi-za-misiats-stanom-na-rik-nazad.md)
- [PP.Річні бонуси](../measures/pp-richni-bonusy.md)
- [PP.Соціальна підтримка](../measures/pp-sotsialna-pidtrymka.md)
- [PP.Цільовий розмір річної винагороди, до оподаткування (12 місяців назад)](../measures/pp-tsilovyi-rozmir-richnoi-vynahorody-do-opodatkuvannia-12-misiatsiv-nazad.md)
- [PP.Щоквартальні премії в середньому за квартал](../measures/pp-shchokvartalni-premii-v-serednomu-za-kvartal.md)
- [PP.Щомісячні премії накопичувально](../measures/pp-shchomisiachni-premii-nakopychuvalno.md)
- [PP.Щомісячні премії середньомісячно](../measures/pp-shchomisiachni-premii-serednomisiachno.md)

## Нотатки

_порожньо_
