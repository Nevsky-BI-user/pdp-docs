# fact_OKR_Key_Results

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_OKR_Key_Results` |
| Джерела | `DM.R27_fact_OKR_Key_Results` |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| EMPLOYEE_NAME | string | EMPLOYEE_NAME |  |
| INIT_DOC_JOB_APPLICATION_ID | string | INIT_DOC_JOB_APPLICATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| INIT_DIVISION_PERSON_ID | string | INIT_DIVISION_PERSON_ID |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| OKR_OBJECTIVE_ID | string | OKR_OBJECTIVE_ID |  |
| FORM_TEMPLATE_NAME | string | FORM_TEMPLATE_NAME |  |
| KR_WEIGHT | double | KR_WEIGHT |  |
| KR_AVG_RATE | double | KR_AVG_RATE |  |
| KR_COLOR_RATE | double | KR_COLOR_RATE |  |
| IS_POSSIBLE_SUPER_GREEN_KR | string | IS_POSSIBLE_SUPER_GREEN_KR |  |
| KR_DESCRIPTION | string | KR_DESCRIPTION |  |
| KR_METRIC_DESCRIPTION | string | KR_METRIC_DESCRIPTION |  |
| KR_CHANGE | string | KR_CHANGE |  |
| KR_FACT_VALUE | string | KR_FACT_VALUE |  |
| KR_EXEC_DATE | dateTime | KR_EXEC_DATE |  |
| LOAD_TIMESTAMP | dateTime | LOAD_TIMESTAMP |  |
| OKR_DESCRIPTION | — | — | так |
| CALC_PERFORMANCE_DESC_RATE | string | CALC_PERFORMANCE_DESC_RATE |  |
| CALC_PERFORMANCE_DESC_RATE_ORDER | string | CALC_PERFORMANCE_DESC_RATE_ORDER |  |
| KR_DESCRIPTION_WRAPPED | string | KR_DESCRIPTION_WRAPPED |  |
| KR_METRIC_DESCRIPTION_WRAPPED | string | KR_METRIC_DESCRIPTION_WRAPPED |  |
| KR_FACT_VALUE_WRAPPED | string | KR_FACT_VALUE_WRAPPED |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | OKR_OBJECTIVE_ID | `fact_OKR_Goals` | OKR_OBJECTIVE_ID |

## Пов'язані міри

Усього: **11**. Згруповано за сторінками звіту та блоками візуальних елементів, де ці міри використовуються.

### [Personal Profile](../report/personal-profile.md) — 4

**Результативність та оцінка › OKR.детально:** [PP.KR.Ключовий результат НЕ досягнуто](../measures/pp-kr-kliuchovyi-rezultat-ne-dosiahnuto.md) · [PP.KR.Ключовий результат досягнуто](../measures/pp-kr-kliuchovyi-rezultat-dosiahnuto.md) · [PP.OKR.Ціль виконана](../measures/pp-okr-tsil-vykonana.md) · [PP.OKR.Ціль не виконана](../measures/pp-okr-tsil-ne-vykonana.md)

### [Group Profile](../report/group-profile.md) — 3

**Результативність та оцінка › Оцінка ОКР:** [GP.Результативність.Оцінка OKR.Загальна кількість KR.CY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-kr-cy.md) · [GP.Результативність.Оцінка OKR.Загальна кількість KR.PY](../measures/gp-rezultatyvnist-otsinka-okr-zahalna-kilkist-kr-py.md) · [GP.Результативність.Оцінка OKR.Середня кількість KR.PY](../measures/gp-rezultatyvnist-otsinka-okr-serednia-kilkist-kr-py.md)

### Поза звітом / службові — 4

[GP.Результативність.Оцінка OKR.Фільтр деталізації KR](../measures/gp-rezultatyvnist-otsinka-okr-filtr-detalizatsii-kr.md) · [PP.OKR.Вага KR](../measures/pp-okr-vaha-kr.md) · [PP.OKR.Значення KR](../measures/pp-okr-znachennia-kr.md) · [PP.OKR.Колірна оцінка KR](../measures/pp-okr-kolirna-otsinka-kr.md)

## Нотатки

_порожньо_
