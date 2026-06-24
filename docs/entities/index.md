# Бізнес-сутності

Усього: **{len(entities)}**.

| Таблиця | Джерела |
|---|---|
| [CG_Event_Types](./cg-event-types.md) | — |
| [_Measures](./measures.md) | — |
| [dim_Admin_OS](./dim-admin-os.md) | `DM.vw_R27_dim_Employee_Access_List` |
| [dim_Date](./dim-date.md) | — |
| [dim_Divisions_Hierarchy](./dim-divisions-hierarchy.md) | `DM.vw_R27_dim_Divisions_Hierarchy` |
| [dim_Employee_Special_FinBP](./dim-employee-special-finbp.md) | `DM.vw_R27_dim_Employee_Special_Head_FinBP` |
| [dim_Employee_Special_HRBP](./dim-employee-special-hrbp.md) | `DM.vw_R27_dim_Employee_Special_Head_HRBP` |
| [dim_Employee_Special_Head_admin](./dim-employee-special-head-admin.md) | `DM.vw_R27_dim_Employee_Special_Head_Admin` |
| [dim_Employee_Special_Head_functional](./dim-employee-special-head-functional.md) | `DM.vw_R27_dim_Employee_Special_Head_Functional` |
| [dim_Employee_Status](./dim-employee-status.md) | `DM.vw_R27_dim_Employee_Status` |
| [dim_Employment_Type](./dim-employment-type.md) | `DM.vw_R27_dim_Employment_Type` |
| [dim_LP_risks](./dim-lp-risks.md) | — |
| [dim_OKR_Evalution](./dim-okr-evalution.md) | — |
| [dim_Office](./dim-office.md) | `DM.vw_R27_dim_Office` |
| [dim_Organization](./dim-organization.md) | `DM.vw_R27_dim_Organization` |
| [dim_Performance_Evalution](./dim-performance-evalution.md) | — |
| [dim_Permanent_Temporary](./dim-permanent-temporary.md) | `DM.vw_R27_dim_Permanent_Temporary` |
| [dim_Person](./dim-person.md) | `DM.vw_R27_dim_Person_PDP` |
| [dim_Position](./dim-position.md) | `DM.vw_R27_dim_Position` |
| [dim_Position_Category](./dim-position-category.md) | `DWH.t_SPO_HR_Position_Category_Matrix` |
| [dim_TRS_categories](./dim-trs-categories.md) | `DM.vw_R27_fact_TRS_Plan_PDP` |
| [dim_Unit](./dim-unit.md) | `DM.vw_R27_dim_Unit` |
| [dim_Work_Format](./dim-work-format.md) | `DM.vw_R27_dim_Work_Format` |
| [dim__HRBP_OS](./dim-hrbp-os.md) | — |
| [fact_360_Assessment](./fact-360-assessment.md) | `DM.vw_R27_fact_360_Assessment` |
| [fact_360_Behavior_Indicator](./fact-360-behavior-indicator.md) | `DM.vw_R27_fact_360_Behavior_Indicator` |
| [fact_Average_Income](./fact-average-income.md) | `DM.vw_R27_fact_Average_Income` |
| [fact_Burnout_Indicators](./fact-burnout-indicators.md) | — |
| [fact_EXCEL_Group_Profile_General_Metric](./fact-excel-group-profile-general-metric.md) | `DWH.t_SPO_HR_Group_Profile_General_Metric` |
| [fact_Employee_History_Position](./fact-employee-history-position.md) | `DM.vw_R27_fact_Employee_History_Position` |
| [fact_Employee_List](./fact-employee-list.md) | — |
| [fact_Employee_OKR](./fact-employee-okr.md) | `DM.R27_fact_OKR_Goals` |
| [fact_Employee_Performance](./fact-employee-performance.md) | `DM.vw_R27_fact_Employee_Performance_PBI` |
| [fact_Employee_Performance_Total](./fact-employee-performance-total.md) | `DM.vw_R27_fact_Employee_Performance_General_PBI` |
| [fact_Employees_Attributes](./fact-employees-attributes.md) | `DM.vw_R27_fact_Employees_Attributes` |
| [fact_Gaussian_Curve_OKR](./fact-gaussian-curve-okr.md) | `DM.R27_fact_OKR_Goals` |
| [fact_Gaussian_Curve_Performance](./fact-gaussian-curve-performance.md) | `DM.R27_fact_Employee_Performance` |
| [fact_Loss_of_Productivity](./fact-loss-of-productivity.md) | `DM.vw_R27_fact_Loss_of_Productivity` |
| [fact_Metrics](./fact-metrics.md) | — |
| [fact_Mobile_Limit](./fact-mobile-limit.md) | `DM.vw_R27_fact_Mobile_Limit_PDP` |
| [fact_Monthly_Viva_Insights](./fact-monthly-viva-insights.md) | `DM.vw_R27_fact_Monthly_Viva_Insights_PDP` |
| [fact_OKR_Goals](./fact-okr-goals.md) | `DM.R27_fact_OKR_Goals` |
| [fact_OKR_Key_Results](./fact-okr-key-results.md) | `DM.R27_fact_OKR_Key_Results` |
| [fact_OKR_SVG](./fact-okr-svg.md) | — |
| [fact_Repayment_Credit](./fact-repayment-credit.md) | `DM.vw_R27_fact_Repayment_Credit_PDP` |
| [fact_Sick_Leaves](./fact-sick-leaves.md) | `DM.vw_R27_fact_Sick_Leaves_PDP` |
| [fact_TRS](./fact-trs.md) | `DM.vw_R27_fact_TRS_PDP` |
| [fact_TRS_Plan](./fact-trs-plan.md) | `DM.vw_R27_fact_TRS_Plan_PDP` |
| [fact_TRS_plan_fact](./fact-trs-plan-fact.md) | `DM.vw_R27_fact_TRS_plan_fact` |
| [fact_Vacancy](./fact-vacancy.md) | `DM.vw_R27_dim_Position`, `DM.vw_R27_fact_Employee_List` |
| [fact_Vacation](./fact-vacation.md) | `DM.vw_R27_fact_Vacation_Fact_PDP` |
| [fact_Vacation_Reserve](./fact-vacation-reserve.md) | `DM.vw_R27_fact_Vacation_Reserve_PDP` |
| [fact_Viva_Metrics](./fact-viva-metrics.md) | — |
| [fact_employee_seniority_by_month](./fact-employee-seniority-by-month.md) | `DM.vw_R27_fact_employee_seniority_by_month_PDP` |
| [p_AC.Loss_Productivity](./p-ac-loss-productivity.md) | — |
| [t_360_Assessment](./t-360-assessment.md) | — |
| [t_AC Burnout](./t-ac-burnout.md) | — |
| [t_FlagDim](./t-flagdim.md) | — |
| [t_HierarchyTypes](./t-hierarchytypes.md) | — |
| [t_IS_FIRED](./t-is-fired.md) | — |
| [t_Loss_Productivity_Metrics_by_Persona](./t-loss-productivity-metrics-by-persona.md) | `DWH.t_SPO_HR_Person_Matrix_with_Coefficient` |
| [t_Participant_Categories](./t-participant-categories.md) | — |
| [t_user_roles](./t-user-roles.md) | — |
