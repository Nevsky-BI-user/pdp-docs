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
| to | USER_ACCESS_ID | `fact_360_Assessment` | USER_ACCESS_ID |
| to | USER_ACCESS_ID | `fact_360_Behavior_Indicator` | USER_ACCESS_ID |

## Пов'язані міри

Усього: **217**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 55

**Navigation:** [GP.Start_Page_NavigationButton](../measures/gp-start-page-navigationbutton.md)

**VIVA › Viva:** [PP.Годин взаємодії з керівником (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії з керівником (напрям)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-napriam.md) · [PP.Годин взаємодії з керівником (співробітник)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-spivrobitnyk.md) · [PP.Годин взаємодії по нарадах (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-po-naradakh-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії по нарадах (напрям)](../measures/pp-hodyn-vzaiemodii-po-naradakh-napriam.md) · [PP.Годин взаємодії по нарадах (співробітник)](../measures/pp-hodyn-vzaiemodii-po-naradakh-spivrobitnyk.md) · [PP.Годин взаємодії у неробочий час (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії у неробочий час (напрям)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-napriam.md) · [PP.Годин взаємодії у неробочий час (співробітник)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-spivrobitnyk.md) · [PP.Годин для фокусної роботи (кадровий підрозділ)](../measures/pp-hodyn-dlia-fokusnoi-roboty-kadrovyi-pidrozdil.md) · [PP.Годин для фокусної роботи (напрям)](../measures/pp-hodyn-dlia-fokusnoi-roboty-napriam.md) · [PP.Годин для фокусної роботи (співробітник)](../measures/pp-hodyn-dlia-fokusnoi-roboty-spivrobitnyk.md) · [PP.Годин загальної взаємодії (кадровий підрозділ)](../measures/pp-hodyn-zahalnoi-vzaiemodii-kadrovyi-pidrozdil.md) · [PP.Годин загальної взаємодії (напрям)](../measures/pp-hodyn-zahalnoi-vzaiemodii-napriam.md) · [PP.Годин загальної взаємодії (співробітник)](../measures/pp-hodyn-zahalnoi-vzaiemodii-spivrobitnyk.md) · [PP.Годин керівника на взаємодію із безпосередніми підлеглими (кадровий підрозділ)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-kadrovyi-pidrozdil.md) · [PP.Годин керівника на взаємодію із безпосередніми підлеглими (напрям)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-napriam.md) · [PP.Годин керівника на взаємодію із безпосередніми підлеглими (співробітник)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-spivrobitnyk.md) · [PP.Годин нарад 1:1 з керівником (кадровий підрозділ)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-kadrovyi-pidrozdil.md) · [PP.Годин нарад 1:1 з керівником (напрям)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-napriam.md) · [PP.Годин нарад 1:1 з керівником (співробітник)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-spivrobitnyk.md) · [PP.Довжина (границі) робочого дня (кадровий підрозділ)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-kadrovyi-pidrozdil.md) · [PP.Довжина (границі) робочого дня (напрям)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-napriam.md) · [PP.Довжина (границі) робочого дня (співробітник)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-spivrobitnyk.md) · [PP.Доля Conflicting meeting hours (кадровий підрозділ)](../measures/pp-dolia-conflicting-meeting-hours-kadrovyi-pidrozdil.md) · [PP.Доля Conflicting meeting hours (напрям)](../measures/pp-dolia-conflicting-meeting-hours-napriam.md) · [PP.Доля Conflicting meeting hours (співробітник)](../measures/pp-dolia-conflicting-meeting-hours-spivrobitnyk.md) · [PP.Розмір мережі (кадровий підрозділ, 3м)](../measures/pp-rozmir-merezhi-kadrovyi-pidrozdil-3m.md) · [PP.Розмір мережі (напрям, 3м)](../measures/pp-rozmir-merezhi-napriam-3m.md) · [PP.Розмір мережі (співробітник, 3м)](../measures/pp-rozmir-merezhi-spivrobitnyk-3m.md) · [PP.Ширина мережі (кадровий підрозділ, 3м)](../measures/pp-shyryna-merezhi-kadrovyi-pidrozdil-3m.md) · [PP.Ширина мережі (напрям, 3м)](../measures/pp-shyryna-merezhi-napriam-3m.md) · [PP.Ширина мережі (співробітник, 3м)](../measures/pp-shyryna-merezhi-spivrobitnyk-3m.md)

**Винагорода:** [PP.Дата доступності позики на ноутбук](../measures/pp-data-dostupnosti-pozyky-na-noutbuk.md) · [PP.Тип опції по авто](../measures/pp-typ-optsii-po-avto.md)

**Загальна інформація:** [PP.Підрозділ 1](../measures/pp-pidrozdil-1.md) · [PP.Підрозділ 2](../measures/pp-pidrozdil-2.md) · [PP.Підрозділ 3](../measures/pp-pidrozdil-3.md) · [PP.Підрозділ 4](../measures/pp-pidrozdil-4.md) · [PP.Підрозділ 5](../measures/pp-pidrozdil-5.md) · [PP.Рівень в ієрархії](../measures/pp-riven-v-iierarkhii.md)

**Паспортна частина:** [PP.OKR.SVG.Last2Periods](../measures/pp-okr-svg-last2periods.md) · [PP.PIB](../measures/pp-pib.md) · [PP.Ризик.Вид відстрочки](../measures/pp-ryzyk-vyd-vidstrochky.md) · [PP.Ризик.Втрата продуктивності](../measures/pp-ryzyk-vtrata-produktyvnosti.md)

**Результативність та оцінка › OKR.детально:** [PP.KR.Ключовий результат НЕ досягнуто](../measures/pp-kr-kliuchovyi-rezultat-ne-dosiahnuto.md) · [PP.KR.Ключовий результат досягнуто](../measures/pp-kr-kliuchovyi-rezultat-dosiahnuto.md) · [PP.OKR.Ціль виконана](../measures/pp-okr-tsil-vykonana.md) · [PP.OKR.Ціль не виконана](../measures/pp-okr-tsil-ne-vykonana.md) · [PP.SVG.OKR.Детально](../measures/pp-svg-okr-detalno.md) · [PP.Частка KR за наявністю змін](../measures/pp-chastka-kr-za-naiavnistiu-zmin.md) · [PP.Частка OKR за кросфункційністю](../measures/pp-chastka-okr-za-krosfunktsiinistiu.md) · [PP.Частка OKR за наявністю змін](../measures/pp-chastka-okr-za-naiavnistiu-zmin.md) · [PP.Частка OKR за типом цілі](../measures/pp-chastka-okr-za-typom-tsili.md)

### [Group Profile](../report/group-profile.md) — 139

**Інші візуали:** [GP.FinBP](../measures/gp-finbp.md) · [GP.HRBP](../measures/gp-hrbp.md) · [GP.eNPS (%)](../measures/gp-enps.md) · [GP.Доля команди з доплатою за шкідливі умови праці, %](../measures/gp-dolia-komandy-z-doplatoiu-za-shkidlyvi-umovy-pratsi.md) · [GP.Керівник](../measures/gp-kerivnyk.md) · [GP.Команда](../measures/gp-komanda.md) · [GP.Напрям](../measures/gp-napriam.md) · [GP.Піднапрям](../measures/gp-pidnapriam.md) · [GP.Середня заробітна плата](../measures/gp-serednia-zarobitna-plata.md) · [GP.Середня кількість днів невикористаної відпустки співробітником](../measures/gp-serednia-kilkist-dniv-nevykorystanoi-vidpustky-spivrobitnykom.md) · [GP.Середній розмір доплати за шкідливі умови праці](../measures/gp-serednii-rozmir-doplaty-za-shkidlyvi-umovy-pratsi.md) · [GP.Середній стаж в команді, років](../measures/gp-serednii-stazh-v-komandi-rokiv.md) · [user_photo](../measures/user-photo.md) · [Доля керівників серед всіх співробітників (%)](../measures/dolia-kerivnykiv-sered-vsikh-spivrobitnykiv.md)

**Navigation:** [GP.NavigationButton2](../measures/gp-navigationbutton2.md)

**TRS:** [GP.Доля команди з доплатою за роз’їзний характер роботи, %](../measures/gp-dolia-komandy-z-doplatoiu-za-roziznyi-kharakter-roboty.md) · [GP.Доля команди з доплатою за роз’їзний характер роботи, % факт](../measures/gp-dolia-komandy-z-doplatoiu-za-roziznyi-kharakter-roboty-fakt.md) · [GP.Доля команди з доплатою за шкідливі умови праці, %](../measures/gp-dolia-komandy-z-doplatoiu-za-shkidlyvi-umovy-pratsi.md) · [GP.Доля команди з доплатою за шкідливі умови праці, % факт](../measures/gp-dolia-komandy-z-doplatoiu-za-shkidlyvi-umovy-pratsi-fakt.md) · [GP.Доля команди з квартальною премією, % факт](../measures/gp-dolia-komandy-z-kvartalnoiu-premiieiu-fakt.md) · [GP.Доля команди з квартальню премією, %](../measures/gp-dolia-komandy-z-kvartalniu-premiieiu.md) · [GP.Доля команди з навчанням, %](../measures/gp-dolia-komandy-z-navchanniam.md) · [GP.Доля команди з позикою на ноутбук (%) (діюча)](../measures/gp-dolia-komandy-z-pozykoiu-na-noutbuk-diiucha.md) · [GP.Доля команди з премією за місяць, %](../measures/gp-dolia-komandy-z-premiieiu-za-misiats.md) · [GP.Доля команди з премією за місяць, % факт](../measures/gp-dolia-komandy-z-premiieiu-za-misiats-fakt.md) · [GP.Доля команди з річним бонусом, %](../measures/gp-dolia-komandy-z-richnym-bonusom.md) · [GP.Доля команди з річними бонусами, % факт](../measures/gp-dolia-komandy-z-richnymy-bonusamy-fakt.md) · [GP.Доля команди з соціальними виплатами, %](../measures/gp-dolia-komandy-z-sotsialnymy-vyplatamy.md) · [GP.Доля команди з щомісячною премією, %](../measures/gp-dolia-komandy-z-shchomisiachnoiu-premiieiu.md) · [GP.Доля команди з щомісячною премією, % факт](../measures/gp-dolia-komandy-z-shchomisiachnoiu-premiieiu-fakt.md) · [GP.Доля команди із доплатою за наставництво, %](../measures/gp-dolia-komandy-iz-doplatoiu-za-nastavnytstvo.md) · [GP.Доля команди із позиками](../measures/gp-dolia-komandy-iz-pozykamy.md) · [GP.Доля команди із премією МХП Зірки, %](../measures/gp-dolia-komandy-iz-premiieiu-mkhp-zirky.md) · [GP.Доля команди із премією за Банк ідей, %](../measures/gp-dolia-komandy-iz-premiieiu-za-bank-idei.md) · [GP.Доля команди із премією за внутрішнє тренерство, %](../measures/gp-dolia-komandy-iz-premiieiu-za-vnutrishnie-trenerstvo.md) · [GP.Доля команди із премією за збереження та розширення земельного банку, %](../measures/gp-dolia-komandy-iz-premiieiu-za-zberezhennia-ta-rozshyrennia-zemelnoho-banku.md) · [GP.Доля команди із премією за програмою «Приведи друга», %](../measures/gp-dolia-komandy-iz-premiieiu-za-prohramoiu-pryvedy-druha.md) · [GP.Доля команди із премією за сумісництво, факт](../measures/gp-dolia-komandy-iz-premiieiu-za-sumisnytstvo-fakt.md) · [GP.Доля команди із проектним бонусом за стратегічні ІТ проєкти, %](../measures/gp-dolia-komandy-iz-proektnym-bonusom-za-stratehichni-it-proiekty.md) · [GP.Доля команди із разовою премією за програмою визнання, %](../measures/gp-dolia-komandy-iz-razovoiu-premiieiu-za-prohramoiu-vyznannia.md) · [GP.Доля команди із інвестиційним проєктним бонусом, %](../measures/gp-dolia-komandy-iz-investytsiinym-proiektnym-bonusom.md) · [GP.Доля учасників команди із зміною зарплати (окладу), %](../measures/gp-dolia-uchasnykiv-komandy-iz-zminoiu-zarplaty-okladu.md) · [GP.К-ть співробітників, що отримали позику на ноутбук (діюча)](../measures/gp-k-t-spivrobitnykiv-shcho-otrymaly-pozyku-na-noutbuk-diiucha.md) · [GP.К-ть співробітників, що отримують виплати на мобільний зв’язок](../measures/gp-k-t-spivrobitnykiv-shcho-otrymuiut-vyplaty-na-mobilnyi-zviazok.md) · [GP.К-ть співробітників, що отримують виплати на оренду житла](../measures/gp-k-t-spivrobitnykiv-shcho-otrymuiut-vyplaty-na-orendu-zhytla.md) · [GP.Розподіл у вилці.SVG](../measures/gp-rozpodil-u-vyltsi-svg.md) · [GP.Різниця фіксованої винагороди (план).Максимальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-plan-maksymalnyi-riven.md) · [GP.Різниця фіксованої винагороди (план).Мінімальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-plan-minimalnyi-riven.md) · [GP.Різниця фіксованої винагороди (факт).Максимальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-fakt-maksymalnyi-riven.md) · [GP.Різниця фіксованої винагороди (факт).Мінімальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-fakt-minimalnyi-riven.md) · [GP.Середня зарплата (оклад)](../measures/gp-serednia-zarplata-oklad.md) · [GP.Середнє зростання цільової річної винагороди, до оподаткування](../measures/gp-serednie-zrostannia-tsilovoi-richnoi-vynahorody-do-opodatkuvannia.md) · [GP.Середні витрати на мобільний зв’язок](../measures/gp-seredni-vytraty-na-mobilnyi-zviazok.md) · [GP.Середні витрати на оренду житла](../measures/gp-seredni-vytraty-na-orendu-zhytla.md) · [GP.Середній % зростання зарплати (окладу) за 12 міс](../measures/gp-serednii-zrostannia-zarplaty-okladu-za-12-mis.md) · [GP.Середній дохід без річного бонуса (за ост. 12 міс)](../measures/gp-serednii-dokhid-bez-richnoho-bonusa-za-ost-12-mis.md) · [GP.Середній дохід з річним бонусом (за ост. 12 міс)](../measures/gp-serednii-dokhid-z-richnym-bonusom-za-ost-12-mis.md) · [GP.Середній розмір доплат за суміщення, факт](../measures/gp-serednii-rozmir-doplat-za-sumishchennia-fakt.md) · [GP.Середній розмір доплати за наставництво](../measures/gp-serednii-rozmir-doplaty-za-nastavnytstvo.md) · [GP.Середній розмір доплати за роз’їзний характер роботи](../measures/gp-serednii-rozmir-doplaty-za-roziznyi-kharakter-roboty.md) · [GP.Середній розмір доплати за роз’їзний характер роботи, факт](../measures/gp-serednii-rozmir-doplaty-za-roziznyi-kharakter-roboty-fakt.md) · [GP.Середній розмір доплати за шкідливі умови праці](../measures/gp-serednii-rozmir-doplaty-za-shkidlyvi-umovy-pratsi.md) · [GP.Середній розмір доплати за шкідливі умови праці, факт](../measures/gp-serednii-rozmir-doplaty-za-shkidlyvi-umovy-pratsi-fakt.md) · [GP.Середній розмір квартальної премії](../measures/gp-serednii-rozmir-kvartalnoi-premii.md) · [GP.Середній розмір квартальної премії, факт](../measures/gp-serednii-rozmir-kvartalnoi-premii-fakt.md) · [GP.Середній розмір позики](../measures/gp-serednii-rozmir-pozyky.md) · [GP.Середній розмір премії МХП Зірки](../measures/gp-serednii-rozmir-premii-mkhp-zirky.md) · [GP.Середній розмір премії за Банк ідей](../measures/gp-serednii-rozmir-premii-za-bank-idei.md) · [GP.Середній розмір премії за внутрішнє тренерство](../measures/gp-serednii-rozmir-premii-za-vnutrishnie-trenerstvo.md) · [GP.Середній розмір премії за збереження та розширення земельного банку](../measures/gp-serednii-rozmir-premii-za-zberezhennia-ta-rozshyrennia-zemelnoho-banku.md) · [GP.Середній розмір премії за місяць](../measures/gp-serednii-rozmir-premii-za-misiats.md) · [GP.Середній розмір премії за місяць, факт](../measures/gp-serednii-rozmir-premii-za-misiats-fakt.md) · [GP.Середній розмір премії за програмою «Приведи друга»](../measures/gp-serednii-rozmir-premii-za-prohramoiu-pryvedy-druha.md) · [GP.Середній розмір проектного бонус за стратегічні ІТ проєкти](../measures/gp-serednii-rozmir-proektnoho-bonus-za-stratehichni-it-proiekty.md) · [GP.Середній розмір разової премії за програмою визнання](../measures/gp-serednii-rozmir-razovoi-premii-za-prohramoiu-vyznannia.md) · [GP.Середній розмір річного бонусу](../measures/gp-serednii-rozmir-richnoho-bonusu.md) · [GP.Середній розмір річного бонусу, факт](../measures/gp-serednii-rozmir-richnoho-bonusu-fakt.md) · [GP.Середній розмір соціальної підтримки](../measures/gp-serednii-rozmir-sotsialnoi-pidtrymky.md) · [GP.Середній розмір щомісячної премії](../measures/gp-serednii-rozmir-shchomisiachnoi-premii.md) · [GP.Середній розмір щомісячної премії, факт](../measures/gp-serednii-rozmir-shchomisiachnoi-premii-fakt.md) · [GP.Середній розмір інвестиційного проєктного бонусу](../measures/gp-serednii-rozmir-investytsiinoho-proiektnoho-bonusu.md) · [GP.Середній цільовий розмір річної винагороди, до оподаткування](../measures/gp-serednii-tsilovyi-rozmir-richnoi-vynahorody-do-opodatkuvannia.md)

**Viva:** [PP.Годин взаємодії з керівником (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії з керівником (напрям)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-napriam.md) · [PP.Годин взаємодії по нарадах (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-po-naradakh-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії по нарадах (напрям)](../measures/pp-hodyn-vzaiemodii-po-naradakh-napriam.md) · [PP.Годин взаємодії у неробочий час (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії у неробочий час (напрям)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-napriam.md) · [PP.Годин для фокусної роботи (кадровий підрозділ)](../measures/pp-hodyn-dlia-fokusnoi-roboty-kadrovyi-pidrozdil.md) · [PP.Годин для фокусної роботи (напрям)](../measures/pp-hodyn-dlia-fokusnoi-roboty-napriam.md) · [PP.Годин загальної взаємодії (кадровий підрозділ)](../measures/pp-hodyn-zahalnoi-vzaiemodii-kadrovyi-pidrozdil.md) · [PP.Годин загальної взаємодії (напрям)](../measures/pp-hodyn-zahalnoi-vzaiemodii-napriam.md) · [PP.Годин керівника на взаємодію із безпосередніми підлеглими (кадровий підрозділ)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-kadrovyi-pidrozdil.md) · [PP.Годин керівника на взаємодію із безпосередніми підлеглими (напрям)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-napriam.md) · [PP.Годин нарад 1:1 з керівником (кадровий підрозділ)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-kadrovyi-pidrozdil.md) · [PP.Годин нарад 1:1 з керівником (напрям)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-napriam.md) · [PP.Довжина (границі) робочого дня (кадровий підрозділ)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-kadrovyi-pidrozdil.md) · [PP.Довжина (границі) робочого дня (напрям)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-napriam.md) · [PP.Доля Conflicting meeting hours (кадровий підрозділ)](../measures/pp-dolia-conflicting-meeting-hours-kadrovyi-pidrozdil.md) · [PP.Доля Conflicting meeting hours (напрям)](../measures/pp-dolia-conflicting-meeting-hours-napriam.md) · [PP.Розмір мережі (кадровий підрозділ, 3м)](../measures/pp-rozmir-merezhi-kadrovyi-pidrozdil-3m.md) · [PP.Розмір мережі (напрям, 3м)](../measures/pp-rozmir-merezhi-napriam-3m.md) · [PP.Ширина мережі (кадровий підрозділ, 3м)](../measures/pp-shyryna-merezhi-kadrovyi-pidrozdil-3m.md) · [PP.Ширина мережі (напрям, 3м)](../measures/pp-shyryna-merezhi-napriam-3m.md)

**Версія 1:** [GP.eNPS (%)](../measures/gp-enps.md) · [GP.Середня заробітна плата](../measures/gp-serednia-zarobitna-plata.md) · [GP.Середня кількість днів невикористаної відпустки співробітником](../measures/gp-serednia-kilkist-dniv-nevykorystanoi-vidpustky-spivrobitnykom.md) · [GP.Середній стаж в команді, років](../measures/gp-serednii-stazh-v-komandi-rokiv.md)

**Версія 2 › Індикатори здоров'я команди:** [GP.eNPS (%)](../measures/gp-enps.md) · [GP.Закриття позицій Middle внутрішніми кандидатами (%)](../measures/gp-zakryttia-pozytsii-middle-vnutrishnimy-kandydatamy.md) · [GP.Закриття позицій Senior+ внутрішніми кандидатами (%)](../measures/gp-zakryttia-pozytsii-senior-vnutrishnimy-kandydatamy.md) · [GP.Охоплення Middle|Senior+ наступниками (%)](../measures/gp-okhoplennia-middle-senior-nastupnykamy.md) · [GP.Продуктивність.Середня оцінка команди.Значення](../measures/gp-produktyvnist-serednia-otsinka-komandy-znachennia.md) · [GP.Співробітники, які розуміють та демонструють цінності компанії (%)](../measures/gp-spivrobitnyky-iaki-rozumiiut-ta-demonstruiut-tsinnosti-kompanii.md) · [GP.Укомплектованість штату (%)](../measures/gp-ukomplektovanist-shtatu.md)

**Версія 2 › Ризики та фокуси уваги:** [GP.Ризик втрати працівників (%)](../measures/gp-ryzyk-vtraty-pratsivnykiv.md) · [GP.Ризик втрати продуктивності (%)](../measures/gp-ryzyk-vtraty-produktyvnosti.md) · [GP.Рівень coaching (1:1), год/міс](../measures/gp-riven-coaching-1-1-hod-mis.md) · [GP.Рівень втрати високорезультативних працівників (%)](../measures/gp-riven-vtraty-vysokorezultatyvnykh-pratsivnykiv.md) · [GP.Рівень смертельних виробничих інцидентів за 2025р., шт.](../measures/gp-riven-smertelnykh-vyrobnychykh-intsydentiv-za-2025r-sht.md) · [GP.Рівень смертельних не виробничих інцидентів за 2025р., шт.](../measures/gp-riven-smertelnykh-ne-vyrobnychykh-intsydentiv-za-2025r-sht.md)

**Загальна інформація:** [GP.FinBP](../measures/gp-finbp.md) · [GP.HRBP](../measures/gp-hrbp.md) · [GP.Керівник](../measures/gp-kerivnyk.md) · [GP.Команда](../measures/gp-komanda.md) · [GP.Кількість Ветеранів](../measures/gp-kilkist-veteraniv.md) · [GP.Кількість мобілізованих](../measures/gp-kilkist-mobilizovanykh.md) · [GP.Кількість співробітників у декретній відпустці](../measures/gp-kilkist-spivrobitnykiv-u-dekretnii-vidpusttsi.md) · [GP.Напрям](../measures/gp-napriam.md) · [GP.Піднапрям](../measures/gp-pidnapriam.md) · [GP.Рівень команди в ієрархії](../measures/gp-riven-komandy-v-iierarkhii.md) · [GP.Середній стаж в команді, років](../measures/gp-serednii-stazh-v-komandi-rokiv.md) · [GP.Укомплектованість штату (%)](../measures/gp-ukomplektovanist-shtatu.md)

**Здоров'я та благополуччя:** [5AC.Коефіцієнт абсентеїзму](../measures/5ac-koefitsiient-absenteizmu.md) · [AC.Відсоток днів відпустки в робочі дні](../measures/ac-vidsotok-dniv-vidpustky-v-robochi-dni.md) · [AC.Доля співробітників з відпустками понад 10 днів](../measures/ac-dolia-spivrobitnykiv-z-vidpustkamy-ponad-10-dniv.md) · [AC.Лідер за невикористаними днями відпустки](../measures/ac-lider-za-nevykorystanymy-dniamy-vidpustky.md) · [AC.Лідер за часом без відпустки](../measures/ac-lider-za-chasom-bez-vidpustky.md) · [AC.Середня кількість днів використаної відпустки](../measures/ac-serednia-kilkist-dniv-vykorystanoi-vidpustky.md) · [AC.Середня кількість днів невикористаної відпустки](../measures/ac-serednia-kilkist-dniv-nevykorystanoi-vidpustky.md) · [AC.Середня кількість лікарняних на співробітника](../measures/ac-serednia-kilkist-likarnianykh-na-spivrobitnyka.md) · [AC.Середня тривалість відпустки співробітника, днів](../measures/ac-serednia-tryvalist-vidpustky-spivrobitnyka-dniv.md) · [AC.Середня тривалість лікарняного на співробітника](../measures/ac-serednia-tryvalist-likarnianoho-na-spivrobitnyka.md)

**Результативність та оцінка › Оцінка ОКР:** [GP.Результативність.Оцінка OKR.Загальна кількість KR.CY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-kr-cy.md) · [GP.Результативність.Оцінка OKR.Загальна кількість KR.PY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-kr-py.md) · [GP.Результативність.Оцінка OKR.Загальна кількість OKR.CY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-okr-cy.md) · [GP.Результативність.Оцінка OKR.Загальна кількість OKR.PY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-okr-py.md) · [GP.Результативність.Оцінка OKR.Кількість співробітників з OKR.CY](../measures/gp-rezultatyvnist-otsinka-okr-kilkist-spivrobitnykiv-z-okr-cy.md) · [GP.Результативність.Оцінка OKR.Середня кількість KR.PY](../measures/gp-rezultatyvnist-otsinka-okr-serednia-kilkist-kr-py.md) · [GP.Результативність.Оцінка OKR.Середня кількість OKR.CY](../measures/gp-rezultatyvnist-otsinka-okr-serednia-kilkist-okr-cy.md) · [GP.Результативність.Оцінка OKR.Середня кількість OKR.PY](../measures/gp-rezultatyvnist-otsinka-okr-serednia-kilkist-okr-py.md)

**Результативність та оцінка › Оцінка результативності › Оцінка керівника та самооцінка:** [GP.Результативність.Оцінка результативності.К-ть працівників.Total](../measures/gp-rezultatyvnist-otsinka-rezultatyvnosti-k-t-pratsivnykiv-total.md)

**Результативність та оцінка › Оцінка результативності › Результативність.Детально:** [GP.Результативність.Оцінка результативності.К-ть працівників](../measures/gp-rezultatyvnist-otsinka-rezultatyvnosti-k-t-pratsivnykiv.md)

**Результативність та оцінка › Траекторія результативності:** [GP.Результативність.Оцінка результативності.Середня оцінка.Total](../measures/gp-rezultatyvnist-otsinka-rezultatyvnosti-serednia-otsinka-total.md)

### [Підсказка "Макc винагорода (план)"](../report/pidskazka-makc-vynahoroda-plan.md) — 1

**Інші візуали:** [GP.Різниця фіксованої винагороди (план).Максимальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-plan-maksymalnyi-riven.md)

### [Підсказка "Мін винагорода (план)"](../report/pidskazka-min-vynahoroda-plan.md) — 1

**Інші візуали:** [GP.Різниця фіксованої винагороди (план).Мінімальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-plan-minimalnyi-riven.md)

### [Підсказка "Макс винагорода (факт)"](../report/pidskazka-maks-vynahoroda-fakt.md) — 1

**Інші візуали:** [GP.Різниця фіксованої винагороди (факт).Максимальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-fakt-maksymalnyi-riven.md)

### [Підсказка "Мін винагорода (факт)"](../report/pidskazka-min-vynahoroda-fakt.md) — 1

**Інші візуали:** [GP.Різниця фіксованої винагороди (факт).Мінімальний рівень](../measures/gp-riznytsia-fiksovanoi-vynahorody-fakt-minimalnyi-riven.md)

### [Утримання працівників](../report/utrymannia-pratsivnykiv.md) — 3

**Navigation group:** [GP.NavigationButton2](../measures/gp-navigationbutton2.md)

**Таблиці › Звільнені:** [AC.Burnout_Risk.Панель фільтрів.Звільнені](../measures/ac-burnout-risk-panel-filtriv-zvilneni.md)

**Таблиці › Працюючі:** [AC.Burnout_risk.Панель фільтрів.Працюючі](../measures/ac-burnout-risk-panel-filtriv-pratsiuiuchi.md)

### [Продуктивність працівників](../report/produktyvnist-pratsivnykiv.md) — 2

**Інші візуали:** [AC.Loss_Productivity.Панель фільтрів](../measures/ac-loss-productivity-panel-filtriv.md)

**Navigation group:** [GP.NavigationButton2](../measures/gp-navigationbutton2.md)

### Поза звітом / службові — 42

['PP.Мобільний зв''язок - Назва пакету'](../measures/pp-mobilnyi-zviazok-nazva-paketu.md) · [AC.LP.Nav.My_lead_team](../measures/ac-lp-nav-my-lead-team.md) · [AC.Nav.My_lead_team](../measures/ac-nav-my-lead-team.md) · [Administrative_role_filter](../measures/administrative-role-filter.md) · [Current_User_Admin_Hierarchy_Level](../measures/current-user-admin-hierarchy-level.md) · [Current_User_HRBP_Hierarchy_Level](../measures/current-user-hrbp-hierarchy-level.md) · [GP.Nav.Панель фільтрів](../measures/gp-nav-panel-filtriv.md) · [GP._Manager_ID](../measures/gp-manager-id.md) · [GP.Виконання плану ФОП YTD (%)](../measures/gp-vykonannia-planu-fop-ytd.md) · [GP.Кількість співробітників всього, чол.](../measures/gp-kilkist-spivrobitnykiv-vsoho-chol.md) · [GP.Кількість співробітників всього, чол. - Integer](../measures/gp-kilkist-spivrobitnykiv-vsoho-chol-integer.md) · [GP.ОКР.Кількість співробітників (Останній період оцінки)](../measures/gp-okr-kilkist-spivrobitnykiv-ostannii-period-otsinky.md) · [GP.ОКР.Оцінка керівника.Значення](../measures/gp-okr-otsinka-kerivnyka-znachennia.md) · [GP.ОКР.Середня оцінка команди.Значення](../measures/gp-okr-serednia-otsinka-komandy-znachennia.md) · [GP.Опція по авто, %](../measures/gp-optsiia-po-avto.md) · [GP.Оцінка результативності попередній рік](../measures/gp-otsinka-rezultatyvnosti-poperednii-rik.md) · [GP.Оцінка результативності поточний рік](../measures/gp-otsinka-rezultatyvnosti-potochnyi-rik.md) · [GP.Продуктивність.Кількість співробітників (Останній період оцінки)](../measures/gp-produktyvnist-kilkist-spivrobitnykiv-ostannii-period-otsinky.md) · [GP.Продуктивність.Оцінка керівника.Значення](../measures/gp-produktyvnist-otsinka-kerivnyka-znachennia.md) · [GP.Результативність.Оцінка OKR.Кількість співробітників з OKR.PY](../measures/gp-rezultatyvnist-otsinka-okr-kilkist-spivrobitnykiv-z-okr-py.md) · [GP.Результативність.Оцінка OKR.Фільтр деталізації KR](../measures/gp-rezultatyvnist-otsinka-okr-filtr-detalizatsii-kr.md) · [GP.Результативність.Оцінка OKR.Фільтр деталізації OKR](../measures/gp-rezultatyvnist-otsinka-okr-filtr-detalizatsii-okr.md) · [GP.Результативність.Оцінка результативності.Середня оцінка](../measures/gp-rezultatyvnist-otsinka-rezultatyvnosti-serednia-otsinka.md) · [GP.Розподіл у вилці](../measures/gp-rozpodil-u-vyltsi.md) · [PP.Nav.My_lead_team](../measures/pp-nav-my-lead-team.md) · [PP.Nav.Застосувати вибір](../measures/pp-nav-zastosuvaty-vybir.md) · [PP.Nav.Панель фільтрів](../measures/pp-nav-panel-filtriv.md) · [PP.OKR.Current_user.Загальна  оцінка OKR](../measures/pp-okr-current-user-zahalna-otsinka-okr.md) · [PP.OKR.Current_user.Загальна колірна оцінка OKR](../measures/pp-okr-current-user-zahalna-kolirna-otsinka-okr.md) · [PP.OKR.Current_user.Коефіцієнт індивідуального бонусу](../measures/pp-okr-current-user-koefitsiient-indyvidualnoho-bonusu.md) · [PP.OKR.Current_user.Статус плану](../measures/pp-okr-current-user-status-planu.md) · [PP.OKR.IsCurrentEmployee](../measures/pp-okr-iscurrentemployee.md) · [PP.OKR.SVG.IsCurrentEmployee](../measures/pp-okr-svg-iscurrentemployee.md) · [PP.Частка OKR за статусом](../measures/pp-chastka-okr-za-statusom.md) · [User_Admin_Hierarchy_Level](../measures/user-admin-hierarchy-level.md) · [User_HRBP_Hierarchy_Level](../measures/user-hrbp-hierarchy-level.md) · [User_role_filter](../measures/user-role-filter.md) · [current_user_name](../measures/current-user-name.md) · [current_user_photo_](../measures/current-user-photo.md) · [filtered_users_check](../measures/filtered-users-check.md) · [test_measure](../measures/test-measure.md) · [text.My_lead_team](../measures/text-my-lead-team.md)

## Нотатки

_порожньо_
