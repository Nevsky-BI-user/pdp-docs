# dim_Unit

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `dim_Unit` |
| Джерела | `DM.vw_R27_dim_Unit` |

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Індивідуальний-профіль-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Direction_PDP`, `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Допоміжні-вітрини-для-звіту/Вью-по-ієрархії-кадрових-підрозділів`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Допоміжні-вітрини-для-звіту/Таблиця-періодична-(попередні-12-міс)-для-розрахунку-метрики-Середній-дохід`, `Командний-профіль/Паспортна-частина-групового-профілю/Метрики-рекрутингу/ТЗ-на-розробку-вітрин-по-метрикам-рекрутингу`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Паспортна-частина-групового-профілю/Сторінка-Картка-команди`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`, `Командний-профіль/Сторінка-Навчання-і-розвиток/Блок-Розвиток-сторінки-Навчання-і-розвиток`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)`, `Командний-профіль/Сторінка-Плинність-та-Exits/Плинність-(вітрина)/Додаткові-вимоги-до-вітрини-Плинність`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди/Блок-Додаткові-інструменти`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| UNIT_KEY | string | UNIT_KEY |  |
| PERSONNEL_UNIT_CODE | string | PERSONNEL_UNIT_CODE |  |
| PERSONNEL_UNIT | string | PERSONNEL_UNIT |  |
| DIRECTION_CODE | string | DIRECTION_CODE |  |
| DIRECTION | string | DIRECTION |  |
| DIRECTION_SHORT | string | DIRECTION_SHORT |  |
| SUB_DIRECTION_CODE | string | SUB_DIRECTION_CODE |  |
| SUB_DIRECTION | string | SUB_DIRECTION |  |
| SUB_DIRECTION_LVL_3 | string | SUB_DIRECTION_LVL_3 |  |
| HAB_FOR_AGRO | string | HAB_FOR_AGRO |  |
| SUBDIVISION_LVL_1 | string | SUBDIVISION_LVL_1 |  |
| SUBDIVISION_LVL_2 | string | SUBDIVISION_LVL_2 |  |
| SUBDIVISION_LVL_3 | string | SUBDIVISION_LVL_3 |  |
| SUBDIVISION_LVL_4 | string | SUBDIVISION_LVL_4 |  |
| SUBDIVISION_LVL_5 | string | SUBDIVISION_LVL_5 |  |
| SUBDIVISION_LVL_6 | string | SUBDIVISION_LVL_6 |  |
| LEVEL_NUM | int64 | LEVEL_NUM |  |
| SUPPORT_UNIT | string | SUPPORT_UNIT |  |
| ORGANIZATION_KEY | string | ORGANIZATION_KEY |  |
| ORGANIZATION | string | ORGANIZATION |  |
| OGRANIZATION_DIRECTION | string | OGRANIZATION_DIRECTION |  |
| ORGANIZATION_SECTOR | string | ORGANIZATION_SECTOR |  |
| ORGANIZATION_SEGMENT | string | ORGANIZATION_SEGMENT |  |
| ORGANIZATION_CODE | string | ORGANIZATION_CODE |  |
| EDRPOU | string | EDRPOU |  |
| IS_GREEN | boolean | IS_GREEN |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | DIVISION_KEY | `fact_Employee_List` | UNIT_KEY |
| to | DIVISION_PERSON_ID | `fact_Metrics` | UNIT_KEY |
| to | UNIT_KEY | `fact_TRS` | UNIT_KEY |
| to | DIVISION_PERSON_ID | `fact_TRS_Plan` | UNIT_KEY |
| to | DIVISION_PERSON_ID | `fact_Vacation` | UNIT_KEY |
| to | DIVISION_PERSON_ID | `fact_Vacation_Reserve` | UNIT_KEY |
| to | unit_key | `fact_Sick_Leaves` | UNIT_KEY |
| to | UNIT_KEY | `fact_Monthly_Viva_Insights` | UNIT_KEY |
| to | DIVISION_PERSON_ID | `fact_Burnout_Indicators` | UNIT_KEY |
| to | DIVISION_PERSON_ID | `fact_Viva_Metrics` | UNIT_KEY |
| to | DIVISION_PERSON_ID | `fact_employee_seniority_by_month` | UNIT_KEY |
| to | DIVISION_PERSON_ID | `fact_Loss_of_Productivity` | UNIT_KEY |

## Пов'язані міри

Усього: **22**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 22

**VIVA › Viva:** [PP.Годин взаємодії з керівником (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії з керівником (напрям)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-napriam.md) · [PP.Годин взаємодії по нарадах (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-po-naradakh-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії по нарадах (напрям)](../measures/pp-hodyn-vzaiemodii-po-naradakh-napriam.md) · [PP.Годин взаємодії у неробочий час (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії у неробочий час (напрям)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-napriam.md) · [PP.Годин для фокусної роботи (кадровий підрозділ)](../measures/pp-hodyn-dlia-fokusnoi-roboty-kadrovyi-pidrozdil.md) · [PP.Годин для фокусної роботи (напрям)](../measures/pp-hodyn-dlia-fokusnoi-roboty-napriam.md) · [PP.Годин загальної взаємодії (кадровий підрозділ)](../measures/pp-hodyn-zahalnoi-vzaiemodii-kadrovyi-pidrozdil.md) · [PP.Годин загальної взаємодії (напрям)](../measures/pp-hodyn-zahalnoi-vzaiemodii-napriam.md) · [PP.Годин керівника на взаємодію із безпосередніми підлеглими (кадровий підрозділ)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-kadrovyi-pidrozdil.md) · [PP.Годин керівника на взаємодію із безпосередніми підлеглими (напрям)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-napriam.md) · [PP.Годин нарад 1:1 з керівником (кадровий підрозділ)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-kadrovyi-pidrozdil.md) · [PP.Годин нарад 1:1 з керівником (напрям)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-napriam.md) · [PP.Довжина (границі) робочого дня (кадровий підрозділ)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-kadrovyi-pidrozdil.md) · [PP.Довжина (границі) робочого дня (напрям)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-napriam.md) · [PP.Доля Conflicting meeting hours (кадровий підрозділ)](../measures/pp-dolia-conflicting-meeting-hours-kadrovyi-pidrozdil.md) · [PP.Доля Conflicting meeting hours (напрям)](../measures/pp-dolia-conflicting-meeting-hours-napriam.md) · [PP.Розмір мережі (кадровий підрозділ, 3м)](../measures/pp-rozmir-merezhi-kadrovyi-pidrozdil-3m.md) · [PP.Розмір мережі (напрям, 3м)](../measures/pp-rozmir-merezhi-napriam-3m.md) · [PP.Ширина мережі (кадровий підрозділ, 3м)](../measures/pp-shyryna-merezhi-kadrovyi-pidrozdil-3m.md) · [PP.Ширина мережі (напрям, 3м)](../measures/pp-shyryna-merezhi-napriam-3m.md)

### [Group Profile](../report/group-profile.md) — 22

**Viva:** [PP.Годин взаємодії з керівником (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії з керівником (напрям)](../measures/pp-hodyn-vzaiemodii-z-kerivnykom-napriam.md) · [PP.Годин взаємодії по нарадах (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-po-naradakh-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії по нарадах (напрям)](../measures/pp-hodyn-vzaiemodii-po-naradakh-napriam.md) · [PP.Годин взаємодії у неробочий час (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-kadrovyi-pidrozdil.md) · [PP.Годин взаємодії у неробочий час (напрям)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-napriam.md) · [PP.Годин для фокусної роботи (кадровий підрозділ)](../measures/pp-hodyn-dlia-fokusnoi-roboty-kadrovyi-pidrozdil.md) · [PP.Годин для фокусної роботи (напрям)](../measures/pp-hodyn-dlia-fokusnoi-roboty-napriam.md) · [PP.Годин загальної взаємодії (кадровий підрозділ)](../measures/pp-hodyn-zahalnoi-vzaiemodii-kadrovyi-pidrozdil.md) · [PP.Годин загальної взаємодії (напрям)](../measures/pp-hodyn-zahalnoi-vzaiemodii-napriam.md) · [PP.Годин керівника на взаємодію із безпосередніми підлеглими (кадровий підрозділ)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-kadrovyi-pidrozdil.md) · [PP.Годин керівника на взаємодію із безпосередніми підлеглими (напрям)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-napriam.md) · [PP.Годин нарад 1:1 з керівником (кадровий підрозділ)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-kadrovyi-pidrozdil.md) · [PP.Годин нарад 1:1 з керівником (напрям)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-napriam.md) · [PP.Довжина (границі) робочого дня (кадровий підрозділ)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-kadrovyi-pidrozdil.md) · [PP.Довжина (границі) робочого дня (напрям)](../measures/pp-dovzhyna-hranytsi-robochoho-dnia-napriam.md) · [PP.Доля Conflicting meeting hours (кадровий підрозділ)](../measures/pp-dolia-conflicting-meeting-hours-kadrovyi-pidrozdil.md) · [PP.Доля Conflicting meeting hours (напрям)](../measures/pp-dolia-conflicting-meeting-hours-napriam.md) · [PP.Розмір мережі (кадровий підрозділ, 3м)](../measures/pp-rozmir-merezhi-kadrovyi-pidrozdil-3m.md) · [PP.Розмір мережі (напрям, 3м)](../measures/pp-rozmir-merezhi-napriam-3m.md) · [PP.Ширина мережі (кадровий підрозділ, 3м)](../measures/pp-shyryna-merezhi-kadrovyi-pidrozdil-3m.md) · [PP.Ширина мережі (напрям, 3м)](../measures/pp-shyryna-merezhi-napriam-3m.md)

## Нотатки

_порожньо_
