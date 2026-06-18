# fact_EXCEL_Group_Profile_General_Metric

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | `mhpsynapsedev01.sql.azuresynapse.net` |
| База | `mhpdwhdev01` |
| Power Query | `fact_EXCEL_Group_Profile_General_Metric` |
| Джерела | `DWH.t_SPO_HR_Group_Profile_General_Metric` |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| ID | string | ID |  |
| Line_Num | int64 | Line_Num |  |
| Record_Type | string | Record_Type |  |
| Direction_Name | string | Direction_Name |  |
| Staffing | double | Staffing |  |
| Hiring_Plan | double | Hiring_Plan |  |
| Internal_Middle_Level_Fill | double | Internal_Middle_Level_Fill |  |
| Internal_Senior_Level_Fill | double | Internal_Senior_Level_Fill |  |
| Referral_Hire | double | Referral_Hire |  |
| Offer_Acceptance_Rate | double | Offer_Acceptance_Rate |  |
| Regretted_Attrition_Rate | double | Regretted_Attrition_Rate |  |
| New_Hire_Turnover_Forecast | double | New_Hire_Turnover_Forecast |  |
| Talent_Pool | double | Talent_Pool |  |
| Created_on_Source_Dttm | dateTime | Created_on_Source_Dttm |  |
| TA_File_Name | string | TA_File_Name |  |
| is_Deleted | boolean | is_Deleted |  |
| Version | string | Version |  |
| Source_System_ID | int64 | Source_System_ID |  |
| Source_Table_ID | int64 | Source_Table_ID |  |
| Dimension_Check_Sum_SCD_Type_1 | int64 | Dimension_Check_Sum_SCD_Type_1 |  |
| Updated_By | string | Updated_By |  |
| Session_SID | int64 | Session_SID |  |
| Load_TimeStamp | dateTime | Load_TimeStamp |  |
| Update_TimeStamp | dateTime | Update_TimeStamp |  |
| eNPS | double | eNPS |  |
| Value_Knowledge | double | Value_Knowledge |  |
| Death_Incident_Production | double | Death_Incident_Production |  |
| Death_Incident_Total | double | Death_Incident_Total |  |

## Зв'язки

—

## Пов'язані міри

Усього: 9.
- [GP.eNPS (%)](../measures/gp-enps.md)
- [GP.Закриття позицій Middle внутрішніми кандидатами (%)](../measures/gp-zakryttia-pozytsii-middle-vnutrishnimy-kandydatamy.md)
- [GP.Закриття позицій Senior+ внутрішніми кандидатами (%)](../measures/gp-zakryttia-pozytsii-senior-vnutrishnimy-kandydatamy.md)
- [GP.Охоплення Middle|Senior+ наступниками (%)](../measures/gp-okhoplennia-middle-senior-nastupnykamy.md)
- [GP.Рівень втрати високорезультативних працівників (%)](../measures/gp-riven-vtraty-vysokorezultatyvnykh-pratsivnykiv.md)
- [GP.Рівень смертельних виробничих інцидентів за 2025р., шт.](../measures/gp-riven-smertelnykh-vyrobnychykh-intsydentiv-za-2025r-sht.md)
- [GP.Рівень смертельних не виробничих інцидентів за 2025р., шт.](../measures/gp-riven-smertelnykh-ne-vyrobnychykh-intsydentiv-za-2025r-sht.md)
- [GP.Співробітники, які розуміють та демонструють цінності компанії (%)](../measures/gp-spivrobitnyky-iaki-rozumiiut-ta-demonstruiut-tsinnosti-kompanii.md)
- [GP.Укомплектованість штату (%)](../measures/gp-ukomplektovanist-shtatu.md)

## Нотатки

_порожньо_
