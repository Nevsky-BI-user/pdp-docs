# fact_Employee_List

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Employee_List` |
| Джерела | — |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| ORGANIZATION_KEY | string | ORGANIZATION_KEY |  |
| PERSON_KEY | string | PERSON_KEY |  |
| DIVISION_KEY | string | DIVISION_KEY |  |
| DIVISION_ACCOUNTING_KEY | string | DIVISION_ACCOUNTING_KEY |  |
| POSITION_KEY | string | POSITION_KEY |  |
| DISTRICT_KEY | string | DISTRICT_KEY |  |
| TARIFF_RATE_TYPE | string | TARIFF_RATE_TYPE |  |
| INDEXATION_BASE_MONTH_DATE | dateTime | INDEXATION_BASE_MONTH_DATE |  |
| PLAN_GO_WORK_DATE | dateTime | PLAN_GO_WORK_DATE |  |
| STAFFING_TABLE_NUM | string | STAFFING_TABLE_NUM |  |
| HIERARCHY_LEVEL | string | HIERARCHY_LEVEL |  |
| POSITION_CATEGORY_ORIGINAL | string | POSITION_CATEGORY_ORIGINAL |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| POSITION_CATEGORY_INTERNAL | string | POSITION_CATEGORY_INTERNAL |  |
| POSITION_CATEGORY_INTERNAL_SORT | int64 | POSITION_CATEGORY_INTERNAL_SORT |  |
| POSITION_COLLAR | string | POSITION_COLLAR |  |
| POSITION_AMT | double | POSITION_AMT |  |
| MIN_TARIFF_RATE | double | MIN_TARIFF_RATE |  |
| MAX_TARIFF_RATE | double | MAX_TARIFF_RATE |  |
| AVG_TARIFF_RATE | double | AVG_TARIFF_RATE |  |
| MIN_SALARY_RANGE | double | MIN_SALARY_RANGE |  |
| MAX_SALARY_RANGE | double | MAX_SALARY_RANGE |  |
| BONUS_YEAR_SALARY_CNT | double | BONUS_YEAR_SALARY_CNT |  |
| BONUS_QUARTER_SALARY_CNT | double | BONUS_QUARTER_SALARY_CNT |  |
| BONUS_MONTH_SALARY_CNT | double | BONUS_MONTH_SALARY_CNT |  |
| FTE_EMPLOYEE | double | FTE_EMPLOYEE |  |
| FTE_FACT | double | FTE_FACT |  |
| FTE_UNIT_POSITION | double | FTE_UNIT_POSITION |  |
| IS_MOBILIZED | int64 | IS_MOBILIZED |  |
| IS_MATERNITY_LEAVE | int64 | IS_MATERNITY_LEAVE |  |
| IS_OUTSOURCING | int64 | IS_OUTSOURCING |  |
| IS_FREE_POSITION | int64 | IS_FREE_POSITION |  |
| IS_MAIN_POSITION | int64 | IS_MAIN_POSITION |  |
| IS_ADAPTATION | int64 | IS_ADAPTATION |  |
| ADAPTATION_END_DATE | dateTime | ADAPTATION_END_DATE |  |
| WORK_DAYS_PER_MONTH | double | WORK_DAYS_PER_MONTH |  |
| NORM_HOUR | double | NORM_HOUR |  |
| WORKED_HOUR | double | WORKED_HOUR |  |
| ROLL_NUMBER | string | ROLL_NUMBER |  |
| IS_NEWLY_HIRED | int64 | IS_NEWLY_HIRED |  |
| IS_HIRED_BY_TRANSFER | int64 | IS_HIRED_BY_TRANSFER |  |
| FIRE_ARTICLE | string | FIRE_ARTICLE |  |
| FIRE_ARTICLE_SHORT | string | FIRE_ARTICLE_SHORT |  |
| IS_FIRED_BY_DECEASE | int64 | IS_FIRED_BY_DECEASE |  |
| CAUSE_OF_DEATH | string | CAUSE_OF_DEATH |  |
| EMP_HIRING_CONDITION_TYPE_CODE | string | EMP_HIRING_CONDITION_TYPE_CODE |  |
| JOB_PART_TIME_FTE | double | JOB_PART_TIME_FTE |  |
| IS_VACANCY | int64 | IS_VACANCY |  |
| EMPLOYMENT_STATUS_DATE | dateTime | EMPLOYMENT_STATUS_DATE |  |
| EMPLOYMENT_STATUS_CODE | string | EMPLOYMENT_STATUS_CODE |  |
| EMPLOYMENT_STATUS | string | EMPLOYMENT_STATUS |  |
| STATUS_KEY | string | STATUS_KEY |  |
| STATUS_CODE | string | STATUS_CODE |  |
| EMP_HEAD_ADMIN_ID | string | EMP_HEAD_ADMIN_ID |  |
| EMP_HEAD_FUNCTIONAL_ID | string | EMP_HEAD_FUNCTIONAL_ID |  |
| EMP_HRBP_ID | string | EMP_HRBP_ID |  |
| EMP_FINBP_ID | string | EMP_FINBP_ID |  |
| TENURE_ALT_BOX_KEY | string | TENURE_ALT_BOX_KEY |  |
| AGE | int64 | AGE |  |
| IS_YOUTH | int64 | IS_YOUTH |  |
| AGE_BOX_KEY | string | AGE_BOX_KEY |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| PERMANENT_TEMPORARY_ADVANCED_KEY | int64 | PERMANENT_TEMPORARY_ADVANCED_KEY |  |
| WORK_FORMAT_ON_POSITION_KEY | string | WORK_FORMAT_ON_POSITION_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| WORK_FORMAT_ON_EMPLOYEE_KEY | string | WORK_FORMAT_ON_EMPLOYEE_KEY |  |
| OFFICE_ON_EMPLOYEE_KEY | string | OFFICE_ON_EMPLOYEE_KEY |  |
| OFFICE_ON_PERSON_KEY | string | OFFICE_ON_PERSON_KEY |  |
| PERIODIC_EMPLOYEE_KEY | string | PERIODIC_EMPLOYEE_KEY |  |
| PERIODIC_UNIT_POSITION_KEY | string | PERIODIC_UNIT_POSITION_KEY |  |
| POSITION_SPECIFICATION | string | POSITION_SPECIFICATION |  |
| IS_RESERVED | int64 | IS_RESERVED |  |
| RESERVATION_START_DATE | dateTime | RESERVATION_START_DATE |  |
| RESERVATION_END_DATE | dateTime | RESERVATION_END_DATE |  |
| IS_BOUND_TO_MILITARY | int64 | IS_BOUND_TO_MILITARY |  |
| MILITARY_REGISTRATION | string | MILITARY_REGISTRATION |  |
| DEFERMENT_REASON | string | DEFERMENT_REASON |  |
| IS_AT_RISK | int64 | IS_AT_RISK |  |
| RESERVED_BY_ORGANIZATION | string | RESERVED_BY_ORGANIZATION |  |
| IS_GREEN | int64 | IS_GREEN |  |
| IS_MANAGER | int64 | IS_MANAGER |  |
| JOB_PERIOD_BEGIN | dateTime | JOB_PERIOD_BEGIN |  |
| JOB_PERIOD_END | dateTime | JOB_PERIOD_END |  |
| EMP_PERIOD_BEGIN | dateTime | EMP_PERIOD_BEGIN |  |
| EMP_PERIOD_END | dateTime | EMP_PERIOD_END |  |
| ID | string | ID |  |
| TA_LINE_NUM | int64 | TA_LINE_NUM |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| DISTRICT_ID | string | DISTRICT_ID |  |
| EMP_BIRTH_DATE | dateTime | EMP_BIRTH_DATE |  |
| EMP_RECEIPT_DATE | dateTime | EMP_RECEIPT_DATE |  |
| EMP_DEFINE_ATTR_DATE | dateTime | EMP_DEFINE_ATTR_DATE |  |
| FULL_NAME | string | FULL_NAME |  |
| DIRECTION | string | DIRECTION |  |
| SUB_DIRECTION | string | SUB_DIRECTION |  |
| POSITION | string | POSITION |  |
| PERSONNEL_UNIT | string | PERSONNEL_UNIT |  |
| DATE_OF_BIRTH | dateTime | DATE_OF_BIRTH |  |
| PHONE_WORK | string | PHONE_WORK |  |
| PHONE_PERSONAL | string | PHONE_PERSONAL |  |
| EMAIL | string | EMAIL |  |
| EMP_WORK_FORMAT | string | EMP_WORK_FORMAT |  |
| POSITION_WORK_FORMAT | string | POSITION_WORK_FORMAT |  |
| EMP_OFFICE_ADRESS | string | EMP_OFFICE_ADRESS |  |
| POSITION_OFFICE_ADRESS | string | POSITION_OFFICE_ADRESS |  |
| UNIVERSITY | string | UNIVERSITY |  |
| EDUCATION | string | EDUCATION |  |
| EDUCATION_LVL | string | EDUCATION_LVL |  |
| ORGANIZATION | string | ORGANIZATION |  |
| EMPLOYEE_ADMIN_NAME | string | EMPLOYEE_ADMIN_NAME |  |
| EMPLOYEE_FUNC_NAME | string | EMPLOYEE_FUNC_NAME |  |
| EMPLOYEE_HRBP_NAME | string | EMPLOYEE_HRBP_NAME |  |
| EMPLOYEE_FINBP_NAME | string | EMPLOYEE_FINBP_NAME |  |
| HAB_FOR_AGRO | string | HAB_FOR_AGRO |  |
| WORK_CONDITION | string | WORK_CONDITION |  |
| EMPLOYMENT_TYPE | string | EMPLOYMENT_TYPE |  |
| POSITION_JOB_SPECIFICATION | string | POSITION_JOB_SPECIFICATION |  |
| SUB_DIRECTION_LVL_3 | string | SUB_DIRECTION_LVL_3 |  |
| IS_VETERAN | int64 | IS_VETERAN |  |
| IS_VETERAN_NEWMAN | int64 | IS_VETERAN_NEWMAN |  |
| DISABILITY_GROUP | string | DISABILITY_GROUP |  |
| DISABILITY_VALIDITY | dateTime | DISABILITY_VALIDITY |  |
| TAX_CODE | string | TAX_CODE |  |
| CHILDREN_AMOUNT_UNDER_18 | int64 | CHILDREN_AMOUNT_UNDER_18 |  |
| MILITARY_REGISTRATION_UKR | string | MILITARY_REGISTRATION_UKR |  |
| STATUS_NAME | string | STATUS_NAME |  |
| CHILDREN_AMOUNT_UNDER_14 | int64 | CHILDREN_AMOUNT_UNDER_14 |  |
| WORKING_HOURS | string | WORKING_HOURS |  |
| PERMANENT_TEMPORARY_DETAILS_ID | int64 | PERMANENT_TEMPORARY_DETAILS_ID |  |
| EMP_HIRING_CONDITION_TYPE_NAME | string | EMP_HIRING_CONDITION_TYPE_NAME |  |
| DISABLED_TYPE | string | DISABLED_TYPE |  |
| WORK_DAYS_PER_MONTH_FACT | double | WORK_DAYS_PER_MONTH_FACT |  |
| FULL_NAME_short | — | — | так |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | PERSON_KEY | `dim_Person` | PERSON_KEY |
| from | POSITION_KEY | `dim_Position` | POSITION_CODE_KEY |
| from | DIVISION_KEY | `dim_Unit` | UNIT_KEY |
| from | ORGANIZATION_KEY | `dim_Organization` | ORGANIZATION_KEY |
| from | WORK_FORMAT_ON_EMPLOYEE_KEY | `dim_Work_Format` | WORK_FORMAT_KEY |
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | EMP_HEAD_FUNCTIONAL_ID | `dim_Employee_Special_FinBP` | ID |
| from | EMP_HEAD_ADMIN_ID | `dim_Employee_Special_Head_admin` | ID |
| from | EMP_HEAD_FUNCTIONAL_ID | `dim_Employee_Special_Head_functional` | ID |
| from | EMP_HRBP_ID | `dim_Employee_Special_HRBP` | ID |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | OFFICE_ON_POSITION_KEY | `dim_Office` | OFFICE_KEY |
| from | PERMANENT_TEMPORARY_DETAILS_ID | `dim_Permanent_Temporary` | PERMANENT_TEMPORARY_DETAILS_KEY |

## Пов'язані міри

Усього: **120**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 72

**Винагорода:** [PP.SVG.Позиція в окладній вилці](../measures/pp-svg-pozytsiia-v-okladnii-vyltsi.md) · [PP.Діти до 18 років](../measures/pp-dity-do-18-rokiv.md) · [PP.Квартальна премія](../measures/pp-kvartalna-premiia.md) · [PP.Квартальна премія окладів](../measures/pp-kvartalna-premiia-okladiv.md) · [PP.Річний бонус](../measures/pp-richnyi-bonus.md) · [PP.Річний бонус окладів](../measures/pp-richnyi-bonus-okladiv.md) · [PP.Цільовий розмір річної винагороди, до оподаткування](../measures/pp-tsilovyi-rozmir-richnoi-vynahorody-do-opodatkuvannia.md) · [PP.Щомісячна премія](../measures/pp-shchomisiachna-premiia.md) · [PP.Щомісячна премія окладів](../measures/pp-shchomisiachna-premiia-okladiv.md)

**Загальна інформація:** [PP.% доплати по суміщенню](../measures/pp-doplaty-po-sumishchenniu.md) · [PP.FinBP](../measures/pp-finbp.md) · [PP.HRBP](../measures/pp-hrbp.md) · [PP.ІПН](../measures/pp-ipn.md) · [PP.Агро Хаб](../measures/pp-ahro-khab.md) · [PP.Адміністративний керівник](../measures/pp-administratyvnyi-kerivnyk.md) · [PP.Адреса офісу (працівник)](../measures/pp-adresa-ofisu-pratsivnyk.md) · [PP.Адреса офісу (штат)](../measures/pp-adresa-ofisu-shtat.md) · [PP.Бронювання до](../measures/pp-broniuvannia-do.md) · [PP.ВНЗ](../measures/pp-vnz.md) · [PP.Ветеран-Новачок](../measures/pp-veteran-novachok.md) · [PP.Вид зайнятості](../measures/pp-vyd-zainiatosti.md) · [PP.Відношення до ВО](../measures/pp-vidnoshennia-do-vo.md) · [PP.Відстрочка від призову](../measures/pp-vidstrochka-vid-pryzovu.md) · [PP.Військова частина](../measures/pp-viiskova-chastyna.md) · [PP.Група інвалідності](../measures/pp-hrupa-invalidnosti.md) · [PP.Дійсність інвалідності до](../measures/pp-diisnist-invalidnosti-do.md) · [PP.Діти до 14 років](../measures/pp-dity-do-14-rokiv.md) · [PP.Діти до 18 років](../measures/pp-dity-do-18-rokiv.md) · [PP.Зайнятих ставок з відсутностями](../measures/pp-zainiatykh-stavok-z-vidsutnostiamy.md) · [PP.Зайнятих ставок по суміщенню](../measures/pp-zainiatykh-stavok-po-sumishchenniu.md) · [PP.Зайнятих ставок фактично](../measures/pp-zainiatykh-stavok-faktychno.md) · [PP.Категорія механізатора](../measures/pp-katehoriia-mekhanizatora.md) · [PP.Категорія посади](../measures/pp-katehoriia-posady.md) · [PP.Координатор для мобілізованих](../measures/pp-koordynator-dlia-mobilizovanykh.md) · [PP.На чиєму місці сидить](../measures/pp-na-chyiemu-mistsi-sydyt.md) · [PP.Надомний інвалід (квота)](../measures/pp-nadomnyi-invalid-kvota.md) · [PP.Напрям](../measures/pp-napriam.md) · [PP.Організація](../measures/pp-orhanizatsiia.md) · [PP.Освіта](../measures/pp-osvita.md) · [PP.Посада](../measures/pp-posada.md) · [PP.Посада зведена](../measures/pp-posada-zvedena.md) · [PP.Посада по суміщенню](../measures/pp-posada-po-sumishchenniu.md) · [PP.Пріоритетне місце роботи](../measures/pp-priorytetne-mistse-roboty.md) · [PP.Піднапрям](../measures/pp-pidnapriam.md) · [PP.Піднапрям рівень 2](../measures/pp-pidnapriam-riven-2.md) · [PP.Підрозділ кадровий](../measures/pp-pidrozdil-kadrovyi.md) · [PP.Підрозділ кадровий по суміщенню](../measures/pp-pidrozdil-kadrovyi-po-sumishchenniu.md) · [PP.Ризик мобілізації](../measures/pp-ryzyk-mobilizatsii.md) · [PP.Рівень в ієрархії](../measures/pp-riven-v-iierarkhii.md) · [PP.Спеціальність](../measures/pp-spetsialnist.md) · [PP.Статус Ветеран](../measures/pp-status-veteran.md) · [PP.Статус працівника](../measures/pp-status-pratsivnyka.md) · [PP.Строк договору до дати](../measures/pp-strok-dohovoru-do-daty.md) · [PP.Термін суміщення (міс.)](../measures/pp-termin-sumishchennia-mis.md) · [PP.Трудові умови](../measures/pp-trudovi-umovy.md) · [PP.Умови прийому](../measures/pp-umovy-pryiomu.md) · [PP.Уточнення по посаді](../measures/pp-utochnennia-po-posadi.md) · [PP.Уточнення по роботах](../measures/pp-utochnennia-po-robotakh.md) · [PP.Формат роботи (працівник)](../measures/pp-format-roboty-pratsivnyk.md) · [PP.Формат роботи (штат)](../measures/pp-format-roboty-shtat.md) · [PP.Функціональний керівник](../measures/pp-funktsionalnyi-kerivnyk.md)

**Здоров'я та благополуччя:** [PP.% днів відпустки в робочі дні](../measures/pp-dniv-vidpustky-v-robochi-dni.md) · [PP.Абсентеїзм](../measures/pp-absenteizm.md) · [PP.Дні відпустки](../measures/pp-dni-vidpustky.md) · [PP.Залишок відпустки](../measures/pp-zalyshok-vidpustky.md) · [PP.Кількість відпусток](../measures/pp-kilkist-vidpustok.md) · [PP.Кількість довгих відпусток](../measures/pp-kilkist-dovhykh-vidpustok.md) · [PP.Лікарняні](../measures/pp-likarniani.md) · [PP.Місяці без відпустки](../measures/pp-misiatsi-bez-vidpustky.md) · [PP.Середня тривалість відпустки](../measures/pp-serednia-tryvalist-vidpustky.md) · [PP.Середня тривалість лікарняного](../measures/pp-serednia-tryvalist-likarnianoho.md)

**Паспортна частина:** [PP.FinBP](../measures/pp-finbp.md) · [PP.HRBP](../measures/pp-hrbp.md) · [PP.Адміністративний керівник](../measures/pp-administratyvnyi-kerivnyk.md) · [PP.Адреса офісу (працівник)](../measures/pp-adresa-ofisu-pratsivnyk.md) · [PP.Вид зайнятості](../measures/pp-vyd-zainiatosti.md) · [PP.Дата народження](../measures/pp-data-narodzhennia.md) · [PP.Категорія посади](../measures/pp-katehoriia-posady.md) · [PP.Посада](../measures/pp-posada.md) · [PP.Підрозділ кадровий](../measures/pp-pidrozdil-kadrovyi.md) · [PP.Ризик.Вид відстрочки](../measures/pp-ryzyk-vyd-vidstrochky.md) · [PP.Формат роботи (працівник)](../measures/pp-format-roboty-pratsivnyk.md) · [PP.Формат роботи (штат)](../measures/pp-format-roboty-shtat.md) · [PP.Функціональний керівник](../measures/pp-funktsionalnyi-kerivnyk.md)

### [Group Profile](../report/group-profile.md) — 36

**Інші візуали:** [GP.Доля заброньованих чоловіків(%)](../measures/gp-dolia-zabronovanykh-cholovikiv.md) · [GP.Доля чоловіків під ризиком мобілізації(%)](../measures/gp-dolia-cholovikiv-pid-ryzykom-mobilizatsii.md) · [GP.Середня кількість днів невикористаної відпустки співробітником](../measures/gp-serednia-kilkist-dniv-nevykorystanoi-vidpustky-spivrobitnykom.md) · [Доля управлінських категорій серед всіх співробітників (%)](../measures/dolia-upravlinskykh-katehorii-sered-vsikh-spivrobitnykiv.md)

**Версія 1:** [GP.Доля чоловіків під ризиком мобілізації(%)](../measures/gp-dolia-cholovikiv-pid-ryzykom-mobilizatsii.md) · [GP.Середня кількість днів невикористаної відпустки співробітником](../measures/gp-serednia-kilkist-dniv-nevykorystanoi-vidpustky-spivrobitnykom.md)

**Версія 2 › Індикатори здоров'я команди:** [GP.Укомплектованість штату (%)](../measures/gp-ukomplektovanist-shtatu.md)

**Загальна інформація:** [GP.Доля Line (%)](../measures/gp-dolia-line.md) · [GP.Доля Middle managers (%)](../measures/gp-dolia-middle-managers.md) · [GP.Доля Senior managers (%)](../measures/gp-dolia-senior-managers.md) · [GP.Доля Specialists (%)](../measures/gp-dolia-specialists.md) · [GP.Доля Workers (%)](../measures/gp-dolia-workers.md) · [GP.Доля гібрид онлайн (%)](../measures/gp-dolia-hibryd-onlain.md) · [GP.Доля гібрид офлайн (%)](../measures/gp-dolia-hibryd-oflain.md) · [GP.Доля заброньованих чоловіків(%)](../measures/gp-dolia-zabronovanykh-cholovikiv.md) · [GP.Доля онлайн (%)](../measures/gp-dolia-onlain.md) · [GP.Доля операціоністів](../measures/gp-dolia-operatsionistiv.md) · [GP.Доля офлайн (%)](../measures/gp-dolia-oflain.md) · [GP.Доля польових (%)](../measures/gp-dolia-polovykh.md) · [GP.Доля студентів](../measures/gp-dolia-studentiv.md) · [GP.Доля чоловіків під ризиком мобілізації(%)](../measures/gp-dolia-cholovikiv-pid-ryzykom-mobilizatsii.md) · [GP.Кількість FTE по штату (план)](../measures/gp-kilkist-fte-po-shtatu-plan.md) · [GP.Кількість Ветеранів](../measures/gp-kilkist-veteraniv.md) · [GP.Кількість зайнятих FTE (факт)](../measures/gp-kilkist-zainiatykh-fte-fakt.md) · [GP.Кількість мобілізованих](../measures/gp-kilkist-mobilizovanykh.md) · [GP.Кількість основних працівників](../measures/gp-kilkist-osnovnykh-pratsivnykiv.md) · [GP.Кількість сезонних працівників](../measures/gp-kilkist-sezonnykh-pratsivnykiv.md) · [GP.Кількість співробітників у декретній відпустці](../measures/gp-kilkist-spivrobitnykiv-u-dekretnii-vidpusttsi.md) · [GP.Кількість студентів](../measures/gp-kilkist-studentiv.md) · [GP.Середній вік](../measures/gp-serednii-vik.md) · [GP.Укомплектованість штату (%)](../measures/gp-ukomplektovanist-shtatu.md)

**Здоров'я та благополуччя:** [5AC.Коефіцієнт абсентеїзму](../measures/5ac-koefitsiient-absenteizmu.md) · [AC.Відсоток днів відпустки в робочі дні](../measures/ac-vidsotok-dniv-vidpustky-v-robochi-dni.md) · [AC.Доля співробітників з відпустками понад 10 днів](../measures/ac-dolia-spivrobitnykiv-z-vidpustkamy-ponad-10-dniv.md) · [AC.Лідер за невикористаними днями відпустки](../measures/ac-lider-za-nevykorystanymy-dniamy-vidpustky.md) · [AC.Лідер за часом без відпустки](../measures/ac-lider-za-chasom-bez-vidpustky.md) · [AC.Середня кількість днів використаної відпустки](../measures/ac-serednia-kilkist-dniv-vykorystanoi-vidpustky.md) · [AC.Середня кількість днів невикористаної відпустки](../measures/ac-serednia-kilkist-dniv-nevykorystanoi-vidpustky.md) · [AC.Середня кількість лікарняних на співробітника](../measures/ac-serednia-kilkist-likarnianykh-na-spivrobitnyka.md) · [AC.Середня тривалість відпустки співробітника, днів](../measures/ac-serednia-tryvalist-vidpustky-spivrobitnyka-dniv.md) · [AC.Середня тривалість лікарняного на співробітника](../measures/ac-serednia-tryvalist-likarnianoho-na-spivrobitnyka.md)

### [Під ризиком мобілізації](../report/pid-ryzykom-mobilizatsii.md) — 2

**Інші візуали:** [GP.Кількість чоловіків БЕЗ ризику мобілізації(%)](../measures/gp-kilkist-cholovikiv-bez-ryzyku-mobilizatsii.md) · [GP.Кількість чоловіків під ризиком мобілізації(%)](../measures/gp-kilkist-cholovikiv-pid-ryzykom-mobilizatsii.md)

### Поза звітом / службові — 10

[PP.min_tariff_rate](../measures/pp-min-tariff-rate.md) · [PP.Електронна пошта](../measures/pp-elektronna-poshta.md) · [PP.Максимум вилки](../measures/pp-maksymum-vylky.md) · [PP.Мінімум вилки](../measures/pp-minimum-vylky.md) · [PP.Офіс (штат)](../measures/pp-ofis-shtat.md) · [PP.Позиція в окладній вилці](../measures/pp-pozytsiia-v-okladnii-vyltsi.md) · [PP.Робочий телефон](../measures/pp-robochyi-telefon.md) · [PP.Робочі години](../measures/pp-robochi-hodyny.md) · [PP.Середина вилки](../measures/pp-seredyna-vylky.md) · [PP.Тривалість довгих відпусток](../measures/pp-tryvalist-dovhykh-vidpustok.md)

## Нотатки

_порожньо_
