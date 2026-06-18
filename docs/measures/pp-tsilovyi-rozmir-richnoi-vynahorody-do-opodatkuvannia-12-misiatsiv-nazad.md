# PP.Цільовий розмір річної винагороди, до оподаткування (12 місяців назад)

*тека `Personal_Profile\TRS`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _CurrMonthStart =  DATE ( YEAR ( TODAY() ), MONTH ( TODAY() ), 1 )
VAR _PrevYearSameMonthStart =  EDATE ( _CurrMonthStart, -12 )
VAR _Fixed =
	CALCULATE (
		SUMX(
			'fact_TRS',
			'fact_TRS'[payments_plan_UAH]
		),
		'fact_TRS'[CATEGORY_OF_ACCRUAL_SORT] = 1,
		'fact_TRS'[wage_rate_type] <> "СДЕЛЬНАЯ",
		TREATAS ( { _PrevYearSameMonthStart }, 'dim_Date'[Date] )
	)
VAR _Variable =
	CALCULATE (
		AVERAGEX(
			'fact_TRS',
			('fact_TRS'[bonus_month_salary_cnt] * 12 + 'fact_TRS'[bonus_quarter_salary_cnt] * 4 + 'fact_TRS'[bonus_year_salary_cnt])  * 'fact_TRS'[wage_rate]
		),
		TREATAS ( { _PrevYearSameMonthStart }, 'dim_Date'[Date] )
	)
RETURN _Fixed * 12 + _Variable
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_TRS_PDP`

Колонки: `CATEGORY_OF_ACCRUAL_SORT`, `Date`, `bonus_month_salary_cnt`, `bonus_quarter_salary_cnt`, `bonus_year_salary_cnt`, `payments_plan_UAH`, `wage_rate`, `wage_rate_type`

Power Query: `dim_Date`

### Залежності (таблиці й колонки)

Таблиці: `dim_Date`, `fact_TRS`

Колонки: `dim_Date[Date]`, `fact_TRS[CATEGORY_OF_ACCRUAL_SORT]`, `fact_TRS[bonus_month_salary_cnt]`, `fact_TRS[bonus_quarter_salary_cnt]`, `fact_TRS[bonus_year_salary_cnt]`, `fact_TRS[payments_plan_UAH]`, `fact_TRS[wage_rate]`, `fact_TRS[wage_rate_type]`

### Схема

```mermaid
graph LR
  M["PP.Цільовий розмір річної винагороди, до оподаткування (12 місяців назад)"]
  M --> dim_Date["dim_Date"]
  M --> fact_TRS["fact_TRS"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [GP.Виконання плану ФОП YTD (%)](../measures/gp-vykonannia-planu-fop-ytd.md), [GP.Середнє зростання цільової річної винагороди, до оподаткування](../measures/gp-serednie-zrostannia-tsilovoi-richnoi-vynahorody-do-opodatkuvannia.md), [PP.Зростання цільової річної винагороди, до оподаткування (за останні 12 міс.)](../measures/pp-zrostannia-tsilovoi-richnoi-vynahorody-do-opodatkuvannia-za-ostanni-12-mis.md)

## Нотатки

_порожньо_
