# fact_360_Assessment

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_360_Assessment` |
| Джерела | `DM.vw_R27_fact_360_Assessment` |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| Employee_ID | string | Employee_ID |  |
| EMPLOYEE_NAME | string | EMPLOYEE_NAME |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| IS_MAIN_POSITION | int64 | IS_MAIN_POSITION |  |
| WORK_FORMAT_ON_EMPLOYEE_KEY | string | WORK_FORMAT_ON_EMPLOYEE_KEY |  |
| STATUS_KEY | string | STATUS_KEY |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| Form_Template_ID | string | Form_Template_ID |  |
| Form_Template_Name | string | Form_Template_Name |  |
| Competency_ID | string | Competency_ID |  |
| Competency_Name | string | Competency_Name |  |
| Category_Name | string | Category_Name |  |
| Manager_Assessment | double | Manager_Assessment |  |
| Subordinate_Assessment | double | Subordinate_Assessment |  |
| Peer_Assessment | double | Peer_Assessment |  |
| Cross_Peer_Assessment | double | Cross_Peer_Assessment |  |
| Self_Assessment | double | Self_Assessment |  |
| HR_Assessment | double | HR_Assessment |  |
| Competency_Rate | double | Competency_Rate |  |
| Competency_Total | double | Competency_Total |  |
| Category_average | double | Category_average |  |
| Total_Assessment_Rate | double | Total_Assessment_Rate |  |
| Competency_Comment | string | Competency_Comment |  |
| Form_Create_Date | dateTime | Form_Create_Date |  |
| End_Fact_Date | dateTime | End_Fact_Date |  |
| Form_Last_Modify_Date | dateTime | Form_Last_Modify_Date |  |
| Assessment_Year | string | Assessment_Year |  |
| Employee_Category | string | Employee_Category |  |
| Form_Employee_ID | string | Form_Employee_ID |  |
| Form_Code | string | Form_Code |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |

## Пов'язані міри

Усього: **15**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 10

**Результативність та оцінка › Оцінка компет.Детально:** [PP.SVG.Оцінка компетенцій.Компетенція](../measures/pp-svg-otsinka-kompetentsii-kompetentsiia.md) · [PP.SVG.Оцінка компетенцій.Хітмап по блоках](../measures/pp-svg-otsinka-kompetentsii-khitmap-po-blokakh.md) · [PP.SVG.Приховані можливості](../measures/pp-svg-prykhovani-mozhlyvosti.md) · [PP.SVG.Сліпі плями](../measures/pp-svg-slipi-pliamy.md) · [PP.Оцінка компетенцій.Оцінка керівника](../measures/pp-otsinka-kompetentsii-otsinka-kerivnyka.md) · [PP.Оцінка компетенцій.Оцінка колег](../measures/pp-otsinka-kompetentsii-otsinka-koleh.md) · [PP.Оцінка компетенцій.Оцінка крос-колег](../measures/pp-otsinka-kompetentsii-otsinka-kros-koleh.md) · [PP.Оцінка компетенцій.Оцінка підлеглих](../measures/pp-otsinka-kompetentsii-otsinka-pidlehlykh.md) · [PP.Оцінка компетенцій.Самооцінка](../measures/pp-otsinka-kompetentsii-samootsinka.md)

**Результативність та оцінка › Оцінка компетенцій:** [PP.SVG.Оцінка компетенцій.Загальна](../measures/pp-svg-otsinka-kompetentsii-zahalna.md)

### Поза звітом / службові — 5

[Competency Comment (SVG)](../measures/competency-comment-svg.md) · [PP.SVG.Оцінка компетенцій.Загальна по блоках](../measures/pp-svg-otsinka-kompetentsii-zahalna-po-blokakh.md) · [PP.Оцінка компетенцій.Експертна оцінка](../measures/pp-otsinka-kompetentsii-ekspertna-otsinka.md) · [PP.Оцінка компетенцій.Загальна](../measures/pp-otsinka-kompetentsii-zahalna.md) · [PP.Оцінка компетенцій.Оцінка 360](../measures/pp-otsinka-kompetentsii-otsinka-360.md)

## Нотатки

_порожньо_
