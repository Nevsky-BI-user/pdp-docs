# fact_Loss_of_Productivity

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_Loss_of_Productivity` |
| Джерела | `DM.vw_R27_fact_Loss_of_Productivity` |

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`, `Кейс-Втрати-Продуктивності-Працівників/Деталізація-метрик-в-кейсі-Продуктивність`, `Командний-профіль/Сторінка-Ефективність`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| PERIOD | dateTime | PERIOD |  |
| USER_ACCESS_ID | string | USER_ACCESS_ID |  |
| EMPLOYEE_ID | string | EMPLOYEE_ID |  |
| EMPLOYEE_NAME | string | EMPLOYEE_NAME |  |
| ORGANIZATION_ID | string | ORGANIZATION_ID |  |
| DOC_JOB_APPLICATION_ID | string | DOC_JOB_APPLICATION_ID |  |
| JOB_TITLE_ID | string | JOB_TITLE_ID |  |
| DIRECTION_CODE | string | DIRECTION_CODE |  |
| WORK_FORMAT_ON_EMPLOYEE_KEY | string | WORK_FORMAT_ON_EMPLOYEE_KEY |  |
| IS_MAIN_POSITION | int64 | IS_MAIN_POSITION |  |
| OKR_LAST_YEAR_RATE | double | OKR_LAST_YEAR_RATE |  |
| PERFORMANCE_RATE_TREND | string | PERFORMANCE_RATE_TREND |  |
| SUPERVISOR_INDICATOR | string | SUPERVISOR_INDICATOR |  |
| BONUS_QUARTER_SALARY_CNT | double | BONUS_QUARTER_SALARY_CNT |  |
| BONUS_MONTH_SALARY_CNT | double | BONUS_MONTH_SALARY_CNT |  |
| Person_Name | string | Person_Name |  |
| Person_group_Name | string | Person_group_Name |  |
| Net_Office_Time_Last_Month | double | Net_Office_Time_Last_Month |  |
| Net_Office_Time_AVG_3month | double | Net_Office_Time_AVG_3month |  |
| Net_Office_Time_Norm_Deviation | double | Net_Office_Time_Norm_Deviation |  |
| Trend_Net_Office_Time_Pct | double | Trend_Net_Office_Time_Pct |  |
| Net_Office_Time_Trend_Pct | double | Net_Office_Time_Trend_Pct |  |
| COLLABORATION_SPAN | double | COLLABORATION_SPAN |  |
| Collab_Span_Norm_Last_Month | double | Collab_Span_Norm_Last_Month |  |
| Collab_Span_Norm | double | Collab_Span_Norm |  |
| Collab_Span_Norm_AVG_3month | double | Collab_Span_Norm_AVG_3month |  |
| Collab_Span_Trend | double | Collab_Span_Trend |  |
| Collab_Span_Trend_Pct | double | Collab_Span_Trend_Pct |  |
| COLLABORATION_HOUR | double | COLLABORATION_HOUR |  |
| Collab_Hour_by_Span_Value | double | Collab_Hour_by_Span_Value |  |
| Collab_Hour_by_Span | double | Collab_Hour_by_Span |  |
| Award_Norm_LAST_3_Month | double | Award_Norm_LAST_3_Month |  |
| Award_Norm_Pct | double | Award_Norm_Pct |  |
| Award_Norm | double | Award_Norm |  |
| Award_Norm_LAST_Month | double | Award_Norm_LAST_Month |  |
| Award_Trend | double | Award_Trend |  |
| Award_Trend_Pct | double | Award_Trend_Pct |  |
| OKR_Pct | double | OKR_Pct |  |
| Trend_Rate_Pct | double | Trend_Rate_Pct |  |
| MANAGER_COACHING_ONE_TO_ONE_HOUR | double | MANAGER_COACHING_ONE_TO_ONE_HOUR |  |
| MANAGER_COACHING_PER_ONE_EMPLOYEE | double | MANAGER_COACHING_PER_ONE_EMPLOYEE |  |
| NORM_WORKS_HOUR_MONTH | int64 | NORM_WORKS_HOUR_MONTH |  |
| Fieldwork_Share | double | Fieldwork_Share |  |
| Fieldwork_Share_by_Norm | double | Fieldwork_Share_by_Norm |  |
| TOTAL_AFTER_HOURS | double | TOTAL_AFTER_HOURS |  |
| VIVA_OVERWORKING | double | VIVA_OVERWORKING |  |
| After Hours | double | After Hours |  |
| Percentage_Of_Unproductive_Employees | double | Percentage_Of_Unproductive_Employees |  |
| Unproductive_Subordinate_Pct | double | Unproductive_Subordinate_Pct |  |
| Turnover | double | Turnover |  |
| Vertical_Employee_Turnover | double | Vertical_Employee_Turnover |  |
| Total_Risk_Productive_without_manager | double | Total_Risk_Productive_without_manager |  |
| Total_Risk_Productive | double | Total_Risk_Productive |  |
| Total_Risk_Productive_Name | string | Total_Risk_Productive_Name |  |
| DIVISION_PERSON_ID | string | DIVISION_PERSON_ID |  |
| STATUS_KEY | string | STATUS_KEY |  |
| POSITION_CATEGORY_DETAIL | string | POSITION_CATEGORY_DETAIL |  |
| EMPLOYMENT_TYPE_KEY | string | EMPLOYMENT_TYPE_KEY |  |
| OFFICE_ON_POSITION_KEY | string | OFFICE_ON_POSITION_KEY |  |
| HIERARCHY_LEVEL | int64 | HIERARCHY_LEVEL |  |
| ORDER_NUM_BY_RISK | int64 | ORDER_NUM_BY_RISK |  |
| Employee_Admin_ID | string | Employee_Admin_ID |  |
| Employee_HRBP_ID | string | Employee_HRBP_ID |  |
| LOAD_TIMESTAMP | dateTime | LOAD_TIMESTAMP |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| from | STATUS_KEY | `dim_Employee_Status` | STATUS_KEY |
| from | USER_ACCESS_ID | `dim_Admin_OS` | USER_ACCESS_ID |
| from | EMPLOYMENT_TYPE_KEY | `dim_Employment_Type` | EMPLOYMENT_TYPE_KEY |
| from | ORGANIZATION_ID | `dim_Organization` | ORGANIZATION_KEY |
| from | EMPLOYEE_ID | `dim_Person` | PERSON_KEY |
| from | POSITION_CATEGORY_DETAIL | `dim_Position_Category` | Position_Category_Detail |
| from | DIVISION_PERSON_ID | `dim_Unit` | UNIT_KEY |
| from | WORK_FORMAT_ON_EMPLOYEE_KEY | `dim_Work_Format` | WORK_FORMAT_KEY |
| from | OFFICE_ON_POSITION_KEY | `dim_Office` | OFFICE_KEY |
| from | JOB_TITLE_ID | `dim_Position` | POSITION_CODE_KEY |
| from | Total_Risk_Productive_Name | `dim_LP_risks` | RISK_TYPE |

## Пов'язані міри

Усього: 65.
- [AC.Export.1:1 в сер. на 1 підлеглого, год.](../measures/ac-export-1-1-v-ser-na-1-pidlehloho-hod.md)
- [AC.Export.Інтервал взаємодії (Viva), год. в день](../measures/ac-export-interval-vzaiemodii-viva-hod-v-den.md)
- [AC.Export.Інтервал взаємодії Тренд (%)](../measures/ac-export-interval-vzaiemodii-trend.md)
- [AC.Export.Агрегований % непродуктинвих підлеглих для керівників](../measures/ac-export-ahrehovanyi-neproduktynvykh-pidlehlykh-dlia-kerivnykiv.md)
- [AC.Export.Доля взаємодії (Viva) в інтервалі (%)](../measures/ac-export-dolia-vzaiemodii-viva-v-intervali.md)
- [AC.Export.Доля днів польових робіт (%)](../measures/ac-export-dolia-dniv-polovykh-robit.md)
- [AC.Export.Перепрацювання (Viva)](../measures/ac-export-perepratsiuvannia-viva.md)
- [AC.Export.Плинність % по вертикалі](../measures/ac-export-plynnist-po-vertykali.md)
- [AC.Export.Результативність по KPI (%)](../measures/ac-export-rezultatyvnist-po-kpi.md)
- [AC.Export.Ризик втрати продуктивності](../measures/ac-export-ryzyk-vtraty-produktyvnosti.md)
- [AC.Export.Тренд OKR (%)](../measures/ac-export-trend-okr.md)
- [AC.Export.Тренд Оцінки рез-ті (%)](../measures/ac-export-trend-otsinky-rez-ti.md)
- [AC.Export.Тренд Результативності по KPI (%)](../measures/ac-export-trend-rezultatyvnosti-po-kpi.md)
- [AC.Export.Чистий час в офісі Тренд (%)](../measures/ac-export-chystyi-chas-v-ofisi-trend.md)
- [AC.Export.Чистий час в офісі, год.](../measures/ac-export-chystyi-chas-v-ofisi-hod.md)
- [AC.LP.Nav.My_lead_team](../measures/ac-lp-nav-my-lead-team.md)
- [AC.LP.Стаж на посаді (останній)](../measures/ac-lp-stazh-na-posadi-ostannii.md)
- [AC.Loss_Productivity.Застосувати вибір](../measures/ac-loss-productivity-zastosuvaty-vybir.md)
- [AC.Loss_Productivity.Панель фільтрів](../measures/ac-loss-productivity-panel-filtriv.md)
- [AC.Switch.1:1 в сер. на 1 підлеглого, год.](../measures/ac-switch-1-1-v-ser-na-1-pidlehloho-hod.md)
- [AC.Switch.Інтервал взаємодії (Viva), год. в день](../measures/ac-switch-interval-vzaiemodii-viva-hod-v-den.md)
- [AC.Switch.Інтервал взаємодії Тренд (%)](../measures/ac-switch-interval-vzaiemodii-trend.md)
- [AC.Switch.Агрегований % непродуктинвих підлеглих для керівників](../measures/ac-switch-ahrehovanyi-neproduktynvykh-pidlehlykh-dlia-kerivnykiv.md)
- [AC.Switch.Доля взаємодії (Viva) в інтервалі (%)](../measures/ac-switch-dolia-vzaiemodii-viva-v-intervali.md)
- [AC.Switch.Доля днів польових робіт (%)](../measures/ac-switch-dolia-dniv-polovykh-robit.md)
- [AC.Switch.Перепрацювання (Viva)](../measures/ac-switch-perepratsiuvannia-viva-2.md)
- [AC.Switch.Плинність % по вертикалі](../measures/ac-switch-plynnist-po-vertykali.md)
- [AC.Switch.Результативність по KPI (%)](../measures/ac-switch-rezultatyvnist-po-kpi.md)
- [AC.Switch.Тренд OKR (%)](../measures/ac-switch-trend-okr.md)
- [AC.Switch.Тренд Оцінки рез-ті (%)](../measures/ac-switch-trend-otsinky-rez-ti.md)
- [AC.Switch.Тренд Результативності по KPI (%)](../measures/ac-switch-trend-rezultatyvnosti-po-kpi.md)
- [AC.Switch.Чистий час в офісі Тренд (%)](../measures/ac-switch-chystyi-chas-v-ofisi-trend.md)
- [AC.Switch.Чистий час в офісі, год.](../measures/ac-switch-chystyi-chas-v-ofisi-hod.md)
- [AC.Дані.1:1 в сер. на 1 підлеглого, год.](../measures/ac-dani-1-1-v-ser-na-1-pidlehloho-hod.md)
- [AC.Дані.Інтервал взаємодії (Viva), год. в день](../measures/ac-dani-interval-vzaiemodii-viva-hod-v-den.md)
- [AC.Дані.Інтервал взаємодії Тренд (%)](../measures/ac-dani-interval-vzaiemodii-trend.md)
- [AC.Дані.Агрегований % непродуктинвих підлеглих для керівників](../measures/ac-dani-ahrehovanyi-neproduktynvykh-pidlehlykh-dlia-kerivnykiv.md)
- [AC.Дані.Доля взаємодії (Viva) в інтервалі (%)](../measures/ac-dani-dolia-vzaiemodii-viva-v-intervali.md)
- [AC.Дані.Доля днів польових робіт (%)](../measures/ac-dani-dolia-dniv-polovykh-robit.md)
- [AC.Дані.Перепрацювання (Viva)](../measures/ac-dani-perepratsiuvannia-viva.md)
- [AC.Дані.Плинність % по вертикалі](../measures/ac-dani-plynnist-po-vertykali.md)
- [AC.Дані.Результативність по KPI (%)](../measures/ac-dani-rezultatyvnist-po-kpi.md)
- [AC.Дані.Ризик втрати продуктивності](../measures/ac-dani-ryzyk-vtraty-produktyvnosti.md)
- [AC.Дані.Тренд OKR (%)](../measures/ac-dani-trend-okr.md)
- [AC.Дані.Тренд Оцінки рез-ті (%)](../measures/ac-dani-trend-otsinky-rez-ti.md)
- [AC.Дані.Тренд Результативності по KPI (%)](../measures/ac-dani-trend-rezultatyvnosti-po-kpi.md)
- [AC.Дані.Чистий час в офісі Тренд (%)](../measures/ac-dani-chystyi-chas-v-ofisi-trend.md)
- [AC.Дані.Чистий час в офісі, год.](../measures/ac-dani-chystyi-chas-v-ofisi-hod.md)
- [AC.Оцінка.1:1 в сер. на 1 підлеглого, год.](../measures/ac-otsinka-1-1-v-ser-na-1-pidlehloho-hod.md)
- [AC.Оцінка.Інтервал взаємодії (Viva), год. в день](../measures/ac-otsinka-interval-vzaiemodii-viva-hod-v-den.md)
- [AC.Оцінка.Інтервал взаємодії Тренд (%)](../measures/ac-otsinka-interval-vzaiemodii-trend.md)
- [AC.Оцінка.Агрегований % непродуктинвих підлеглих для керівників](../measures/ac-otsinka-ahrehovanyi-neproduktynvykh-pidlehlykh-dlia-kerivnykiv.md)
- [AC.Оцінка.Доля взаємодії (Viva) в інтервалі (%)](../measures/ac-otsinka-dolia-vzaiemodii-viva-v-intervali.md)
- [AC.Оцінка.Доля днів польових робіт (%)](../measures/ac-otsinka-dolia-dniv-polovykh-robit.md)
- [AC.Оцінка.Перепрацювання (Viva)](../measures/ac-otsinka-perepratsiuvannia-viva.md)
- [AC.Оцінка.Плинність % по вертикалі](../measures/ac-otsinka-plynnist-po-vertykali.md)
- [AC.Оцінка.Результативність по KPI (%)](../measures/ac-otsinka-rezultatyvnist-po-kpi.md)
- [AC.Оцінка.Ризик втрати продуктивності](../measures/ac-otsinka-ryzyk-vtraty-produktyvnosti.md)
- [AC.Оцінка.Тренд OKR (%)](../measures/ac-otsinka-trend-okr.md)
- [AC.Оцінка.Тренд Оцінки рез-ті (%)](../measures/ac-otsinka-trend-otsinky-rez-ti.md)
- … і ще 5

## Нотатки

_порожньо_
