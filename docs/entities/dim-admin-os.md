# dim_Admin_OS

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Admin_OS` |
| Джерела | `DM.vw_R27_dim_Employee_Access_List` |

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Індивідуальний-профіль-працівника`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| path_column | — | — | так |
| EMP_HIERARCHY_LEVEL | string | EMP_HIERARCHY_LEVEL |  |
| EMP_HEAD_ADMIN_ID_EMP_HEAD_ADMIN_DOC_JOB_APPLICATION_ID | string | EMP_HEAD_ADMIN_ID_EMP_HEAD_ADMIN_DOC_JOB_APPLICATION_ID |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| path_length | — | — | так |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| EMPLOYEE_EMAIL | string | EMPLOYEE_EMAIL |  |
| path_column_email | — | — | так |
| check_hierarchy_length | — | — | так |
| EMPLOYEE_ADMIN_ID | string | EMPLOYEE_ADMIN_ID |  |
| DOC_JOB_APPLICATION_ADMIN_ID | string | DOC_JOB_APPLICATION_ADMIN_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| ORDER_NUM | int64 | ORDER_NUM |  |
| ORGANIZATION | string | ORGANIZATION |  |
| PERSONNEL_UNIT | string | PERSONNEL_UNIT |  |
| DIRECTION | string | DIRECTION |  |
| SUB_DIRECTION | string | SUB_DIRECTION |  |
| HAB_FOR_AGRO | string | HAB_FOR_AGRO |  |
| SUBDIVISION_LVL_1 | string | SUBDIVISION_LVL_1 |  |
| SUBDIVISION_LVL_2 | string | SUBDIVISION_LVL_2 |  |
| SUBDIVISION_LVL_3 | string | SUBDIVISION_LVL_3 |  |
| SUBDIVISION_LVL_4 | string | SUBDIVISION_LVL_4 |  |
| SUBDIVISION_LVL_5 | string | SUBDIVISION_LVL_5 |  |
| SUBDIVISION_LVL_6 | string | SUBDIVISION_LVL_6 |  |
| N-1 | — | — | так |
| N-2 | — | — | так |
| N-3 | — | — | так |
| N-4 | — | — | так |
| N-5 | — | — | так |
| N-6 | — | — | так |
| N-7 | — | — | так |
| N-8 | — | — | так |
| EMPLOYEE_NAME | string | EMPLOYEE_NAME |  |
| ORDER_NUM_2 | int64 | ORDER_NUM_2 |  |
| SUBORDINATE_СNT | int64 | SUBORDINATE_СNT |  |
| URL_FOTO | string | URL_FOTO |  |
| FULL_NAME | — | — | так |
| IS_MAIN_POSITION | — | — | так |
| EMP_HEAD_FUNCTIONAL_ID_EMP_HEAD_FUNCTIONAL_DOC_JOB_APPLICATION_ID | string | EMP_HEAD_FUNCTIONAL_ID_EMP_HEAD_FUNCTIONAL_DOC_JOB_APPLICATION_ID |  |
| EMP_HRBP_ID_EMP_HRBP_DOC_JOB_APPLICATION_ID | string | EMP_HRBP_ID_EMP_HRBP_DOC_JOB_APPLICATION_ID |  |
| EMP_FINBP_ID_EMP_FINBP_DOC_JOB_APPLICATION_ID | string | EMP_FINBP_ID_EMP_FINBP_DOC_JOB_APPLICATION_ID |  |
| Position_category | — | — | так |
| EMP_STATUS_KEY | — | — | так |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| EMPLOYMENT_TYPE | string | EMPLOYMENT_TYPE |  |
| STATUS_NAME | string | STATUS_NAME |  |
| STATUS_KEY | string | STATUS_KEY |  |
| OFFICE_TYPE | string | OFFICE_TYPE |  |
| POSITION | string | POSITION |  |
| ROLL_NUMBER | string | ROLL_NUMBER |  |
| N-0 | — | — | так |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| DIVISION_POSITION_ID | string | DIVISION_POSITION_ID |  |
| HRBP_email | — | — | так |
| EMP_HIERARCHY_LEVEL_LIST | string | EMP_HIERARCHY_LEVEL_LIST |  |
| FULL_NAME_HRBP | — | — | так |
| FULL_NAME_ADMIN | — | — | так |
| FULL_NAME_FinBP | — | — | так |
| USER_ROLE | string | USER_ROLE |  |
| PARENT_USER_ACCESS_ID | string | PARENT_USER_ACCESS_ID |  |
| path_length_rls | — | — | так |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| EMP_DIVISION_PERSON_ID_JOB_TITLE_ID | string | EMP_DIVISION_PERSON_ID_JOB_TITLE_ID |  |
| IS_MANAGER | boolean | IS_MANAGER |  |
| FULL_NAME_short | — | — | так |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | USER_ACCESS_ID | `fact_Employee_List` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_TRS` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Vacation` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Vacation_Reserve` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Mobile_Limit` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Repayment_Credit` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_TRS_Plan` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Sick_Leaves` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Monthly_Viva_Insights` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Metrics` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Burnout_Indicators` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_employee_seniority_by_month` | USER_ACCESS_ID |
| from | DIVISION_POSITION_ID | `fact_Vacancy` | DIVISION_POSITION_id |
| to | USER_ACCESS_ID | `fact_Employee_OKR` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Loss_of_Productivity` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Employee_Performance` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Employee_Performance_Total` | USER_ACCESS_ID |
| from | USER_ACCESS_ID | `fact_Average_Income` | USER_ACCESS_ID |
| from | USER_ACCESS_ID | `fact_Employees_Attributes` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_Employee_History_Position` | USER_ACCESS_ID |

## Пов'язані міри

Усього: 217.
- ['PP.Мобільний зв''язок - Назва пакету'](../measures/pp-mobilnyi-zviazok-nazva-paketu.md)
- [5AC.Коефіцієнт абсентеїзму](../measures/5ac-koefitsiient-absenteizmu.md)
- [AC.Burnout_Risk.Панель фільтрів.Звільнені](../measures/ac-burnout-risk-panel-filtriv-zvilneni.md)
- [AC.Burnout_risk.Панель фільтрів.Працюючі](../measures/ac-burnout-risk-panel-filtriv-pratsiuiuchi.md)
- [AC.LP.Nav.My_lead_team](../measures/ac-lp-nav-my-lead-team.md)
- [AC.Loss_Productivity.Панель фільтрів](../measures/ac-loss-productivity-panel-filtriv.md)
- [AC.Nav.My_lead_team](../measures/ac-nav-my-lead-team.md)
- [AC.Відсоток днів відпустки в робочі дні](../measures/ac-vidsotok-dniv-vidpustky-v-robochi-dni.md)
- [AC.Доля співробітників з відпустками понад 10 днів](../measures/ac-dolia-spivrobitnykiv-z-vidpustkamy-ponad-10-dniv.md)
- [AC.Лідер за невикористаними днями відпустки](../measures/ac-lider-za-nevykorystanymy-dniamy-vidpustky.md)
- [AC.Лідер за часом без відпустки](../measures/ac-lider-za-chasom-bez-vidpustky.md)
- [AC.Середня кількість днів використаної відпустки](../measures/ac-serednia-kilkist-dniv-vykorystanoi-vidpustky.md)
- [AC.Середня кількість днів невикористаної відпустки](../measures/ac-serednia-kilkist-dniv-nevykorystanoi-vidpustky.md)
- [AC.Середня кількість лікарняних на співробітника](../measures/ac-serednia-kilkist-likarnianykh-na-spivrobitnyka.md)
- [AC.Середня тривалість відпустки співробітника, днів](../measures/ac-serednia-tryvalist-vidpustky-spivrobitnyka-dniv.md)
- [AC.Середня тривалість лікарняного на співробітника](../measures/ac-serednia-tryvalist-likarnianoho-na-spivrobitnyka.md)
- [Administrative_role_filter](../measures/administrative-role-filter.md)
- [Current_User_Admin_Hierarchy_Level](../measures/current-user-admin-hierarchy-level.md)
- [Current_User_HRBP_Hierarchy_Level](../measures/current-user-hrbp-hierarchy-level.md)
- [GP.FinBP](../measures/gp-finbp.md)
- [GP.HRBP](../measures/gp-hrbp.md)
- [GP.Nav.Панель фільтрів](../measures/gp-nav-panel-filtriv.md)
- [GP.NavigationButton2](../measures/gp-navigationbutton2.md)
- [GP.Start_Page_NavigationButton](../measures/gp-start-page-navigationbutton.md)
- [GP._Manager_ID](../measures/gp-manager-id.md)
- [GP.eNPS (%)](../measures/gp-enps.md)
- [GP.Виконання плану ФОП YTD (%)](../measures/gp-vykonannia-planu-fop-ytd.md)
- [GP.Доля команди з доплатою за роз’їзний характер роботи, %](../measures/gp-dolia-komandy-z-doplatoiu-za-roziznyi-kharakter-roboty.md)
- [GP.Доля команди з доплатою за роз’їзний характер роботи, % факт](../measures/gp-dolia-komandy-z-doplatoiu-za-roziznyi-kharakter-roboty-fakt.md)
- [GP.Доля команди з доплатою за шкідливі умови праці, %](../measures/gp-dolia-komandy-z-doplatoiu-za-shkidlyvi-umovy-pratsi.md)
- [GP.Доля команди з доплатою за шкідливі умови праці, % факт](../measures/gp-dolia-komandy-z-doplatoiu-za-shkidlyvi-umovy-pratsi-fakt.md)
- [GP.Доля команди з квартальною премією, % факт](../measures/gp-dolia-komandy-z-kvartalnoiu-premiieiu-fakt.md)
- [GP.Доля команди з квартальню премією, %](../measures/gp-dolia-komandy-z-kvartalniu-premiieiu.md)
- [GP.Доля команди з навчанням, %](../measures/gp-dolia-komandy-z-navchanniam.md)
- [GP.Доля команди з позикою на ноутбук (%) (діюча)](../measures/gp-dolia-komandy-z-pozykoiu-na-noutbuk-diiucha.md)
- [GP.Доля команди з премією за місяць, %](../measures/gp-dolia-komandy-z-premiieiu-za-misiats.md)
- [GP.Доля команди з премією за місяць, % факт](../measures/gp-dolia-komandy-z-premiieiu-za-misiats-fakt.md)
- [GP.Доля команди з річним бонусом, %](../measures/gp-dolia-komandy-z-richnym-bonusom.md)
- [GP.Доля команди з річними бонусами, % факт](../measures/gp-dolia-komandy-z-richnymy-bonusamy-fakt.md)
- [GP.Доля команди з соціальними виплатами, %](../measures/gp-dolia-komandy-z-sotsialnymy-vyplatamy.md)
- [GP.Доля команди з щомісячною премією, %](../measures/gp-dolia-komandy-z-shchomisiachnoiu-premiieiu.md)
- [GP.Доля команди з щомісячною премією, % факт](../measures/gp-dolia-komandy-z-shchomisiachnoiu-premiieiu-fakt.md)
- [GP.Доля команди із доплатою за наставництво, %](../measures/gp-dolia-komandy-iz-doplatoiu-za-nastavnytstvo.md)
- [GP.Доля команди із позиками](../measures/gp-dolia-komandy-iz-pozykamy.md)
- [GP.Доля команди із премією МХП Зірки, %](../measures/gp-dolia-komandy-iz-premiieiu-mkhp-zirky.md)
- [GP.Доля команди із премією за Банк ідей, %](../measures/gp-dolia-komandy-iz-premiieiu-za-bank-idei.md)
- [GP.Доля команди із премією за внутрішнє тренерство, %](../measures/gp-dolia-komandy-iz-premiieiu-za-vnutrishnie-trenerstvo.md)
- [GP.Доля команди із премією за збереження та розширення земельного банку, %](../measures/gp-dolia-komandy-iz-premiieiu-za-zberezhennia-ta-rozshyrennia-zemelnoho-banku.md)
- [GP.Доля команди із премією за програмою «Приведи друга», %](../measures/gp-dolia-komandy-iz-premiieiu-za-prohramoiu-pryvedy-druha.md)
- [GP.Доля команди із премією за сумісництво, факт](../measures/gp-dolia-komandy-iz-premiieiu-za-sumisnytstvo-fakt.md)
- [GP.Доля команди із проектним бонусом за стратегічні ІТ проєкти, %](../measures/gp-dolia-komandy-iz-proektnym-bonusom-za-stratehichni-it-proiekty.md)
- [GP.Доля команди із разовою премією за програмою визнання, %](../measures/gp-dolia-komandy-iz-razovoiu-premiieiu-za-prohramoiu-vyznannia.md)
- [GP.Доля команди із інвестиційним проєктним бонусом, %](../measures/gp-dolia-komandy-iz-investytsiinym-proiektnym-bonusom.md)
- [GP.Доля учасників команди із зміною зарплати (окладу), %](../measures/gp-dolia-uchasnykiv-komandy-iz-zminoiu-zarplaty-okladu.md)
- [GP.Закриття позицій Middle внутрішніми кандидатами (%)](../measures/gp-zakryttia-pozytsii-middle-vnutrishnimy-kandydatamy.md)
- [GP.Закриття позицій Senior+ внутрішніми кандидатами (%)](../measures/gp-zakryttia-pozytsii-senior-vnutrishnimy-kandydatamy.md)
- [GP.К-ть співробітників, що отримали позику на ноутбук (діюча)](../measures/gp-k-t-spivrobitnykiv-shcho-otrymaly-pozyku-na-noutbuk-diiucha.md)
- [GP.К-ть співробітників, що отримують виплати на мобільний зв’язок](../measures/gp-k-t-spivrobitnykiv-shcho-otrymuiut-vyplaty-na-mobilnyi-zviazok.md)
- [GP.К-ть співробітників, що отримують виплати на оренду житла](../measures/gp-k-t-spivrobitnykiv-shcho-otrymuiut-vyplaty-na-orendu-zhytla.md)
- [GP.Керівник](../measures/gp-kerivnyk.md)
- … і ще 157

## Нотатки

_порожньо_
