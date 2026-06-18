# PP.OKR.SVG.Last2Periods

*тека `Personal_Profile\Паспорт\OKR`*

## Бізнес-суть

Calc_Performance_Desc_Rate → Колірна оцінка ОКР; Calc_Performance_Desc_Rate → Загальна колірна оцінка ОКР; Calc_Performance_Desc_Rate → Загальна колірна оцінка OKR; Calc_Performance_Desc_Rate → Ціль виконана; Calc_Performance_Desc_Rate → Ціль не виконана; Calc_Performance_Desc_Rate → Колірна оцінка OKR за останній період; Calc_Performance_Desc_Rate → Колірна оцінка OKR за передостанній період; Calc_Performance_Desc_Rate → Загальний колір ОКР; Calc_Performance_Desc_Rate → Колірна оцінка OKR; Calc_Performance_Str_Rate → Загальна оцінка ОКР; Calc_Performance_Str_Rate → Загальна оцінка OKR; Calc_Performance_Str_Rate → Оцінка OKR; PLAN_YEAR → Рік ОКР; PLAN_YEAR → Значення останнього року оцінки ОКР; PLAN_YEAR → Значення передостаннього  року оцінки ОКР

Останнє НЕ пусте актуальне значення на дату (date) поточного запису Якщо поле Calc_Performance_Desc_Rate має значення Супер зелений, або Жовто-зелений, або Зелений, або Жовтий, або Жовто-червоний Якщо поле Calc_Performance_Desc_Rate має значення Червоний Останнє доступне значення станом на дату поточного запису, релевантне відповідній оцінці результативності. Значення останнього року оцінки ОКР визначати в залежності від того, які дані доступні на поточний момент. Наприклад, протягом 2025 року в оцінку брати коефіцієнт індивідуального бонусу працівника за 2023-2024 роки, бо за 2025 рік оцінки 

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника/Редизайн-паспортної-частини`, `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди/Створити-блок-Виконання-OKR`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\OKR` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _fontFamily = "Segoe UI"
VAR _employee_id = SELECTEDVALUE('dim_Admin_OS'[EMPLOYEE_ID])

// ─── Дані ───
// Значення стовпця (висота + підпис) = Calc_Performance_Str_Rate (оцінка).
// Бонус (Ind_Bonus_Rate) не використовується. Вікно — останні 2 РОКИ;
// усередині року окремий стовпець на кожну унікальну оцінку (без усереднення).

// 1) Грань періодів співробітника: рік × оцінка. SUMMARIZE — лише наявні комбінації.
VAR _periodsAll =
	CALCULATETABLE(
		SUMMARIZE(
			'fact_OKR_Goals',
			'fact_OKR_Goals'[PLAN_YEAR],
			'fact_OKR_Goals'[Calc_Performance_Str_Rate]
		),
		'fact_OKR_Goals'[EMPLOYEE_ID] = _employee_id
	)

// 2) Числове значення оцінки + категорія (колір) на грань періоду.
//    @value: оцінка — це сама групувальна колонка рядка; VALUE() → число,
//            IFERROR відсікає порожні/нечислові у BLANK.
//    @cat:   EMPLOYEE_ID повторюється, бо context transition переносить у фільтр
//            лише рік + оцінку, не EMPLOYEE_ID.
VAR _periodsData =
	ADDCOLUMNS(
		_periodsAll,
		"@value", IFERROR(VALUE('fact_OKR_Goals'[Calc_Performance_Str_Rate]), BLANK()),
		"@cat",
			CALCULATE(
				SELECTEDVALUE('fact_OKR_Goals'[Calc_Performance_Desc_Rate]),
				'fact_OKR_Goals'[EMPLOYEE_ID] = _employee_id
			)
	)

// 3) Лише періоди з валідною оцінкою
VAR _periodsNonBlank = FILTER(_periodsData, NOT ISBLANK([@value]))

// 4) Останні 2 РОКИ серед наявних (відбір по роках, не по оцінках).
//    Роки унікальні → у TOPN ничиї немає → рівно 2 роки.
VAR _last2Years =
	TOPN(
		2,
		DISTINCT(SELECTCOLUMNS(_periodsNonBlank, "@y", 'fact_OKR_Goals'[PLAN_YEAR])),
		[@y],
		DESC
	)

// 5) Усі періоди цих 2 років
VAR _scoped =
	FILTER(
		_periodsNonBlank,
		'fact_OKR_Goals'[PLAN_YEAR] IN _last2Years
	)

// 6) Композитний індекс позиції стовпця: ключ "рік|оцінка".
//    Рік уже не унікальний → RANKX лише за роком накладав би стовпці.
//    Порядок усередині року довільний; між роками — старіший лівіше.
VAR _data =
	ADDCOLUMNS(
		_scoped,
		"@i",
			RANKX(
				_scoped,
				FORMAT('fact_OKR_Goals'[PLAN_YEAR], "0000") & "|" & 'fact_OKR_Goals'[Calc_Performance_Str_Rate],
				,
				ASC,
				Dense
			) - 1
	)

VAR _maxScore = MAXX(_data, [@value])
VAR _MaxValue = MAX(_maxScore, 100)

VAR _W = 100
VAR _H = 80
VAR _MarginX = 10
VAR _BarCount = COUNTROWS(_data)
VAR _Avail = _W - 2 * _MarginX
VAR _ColWidth = DIVIDE(_Avail, MAX(_BarCount, 1))
VAR _BarWidth = MIN(14, _ColWidth * 0.58)
VAR _StartX = _MarginX + (_Avail - _ColWidth * _BarCount) / 2
VAR _Rx = _BarWidth / 2
VAR _ValueY = 9
VAR _BarTop = 19
VAR _BarBot = 67
VAR _BarMaxH = _BarBot - _BarTop
VAR _YearY = 76

VAR _Cols = CONCATENATEX(
	_data,
	VAR _val = [@value]
	VAR _cat = [@cat]
	VAR _yr  = 'fact_OKR_Goals'[PLAN_YEAR]
	VAR _fill = SWITCH(_cat,
		"Супер зелений", "#009051",
		"Суперзелений",  "#009051",
		"Зелений",       "#02BD3D",
		"Жовто-зелений", "#A6CE39",
		"Жовтий",        "#FFE521",
		"Жовто-червоний","#FF7E0D",
		"Червоний",      "#F23711",
		"#A0AEC0"
	)
	VAR _x  = _StartX + [@i] * _ColWidth
	VAR _cx = _x + (_ColWidth / 2)
	VAR _bx = _cx - (_BarWidth / 2)
	VAR _h  = MIN(DIVIDE(_val, _MaxValue, 0), 1) * _BarMaxH
	VAR _y  = _BarBot - _h
	VAR _valueLabel =
		"<text x='" & _cx & "' y='" & _ValueY & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:6px; fill:" & _fill & "; font-weight:700;'>" &
			SUBSTITUTE(FORMAT(_val, "0.0"), ".", ",") &
		"</text>"
	VAR _bar =
		"<rect x='" & FORMAT(_bx, "0.0") & "' y='" & FORMAT(_y, "0.0") & "' width='" & FORMAT(_BarWidth, "0.0") & "' height='" & FORMAT(_h, "0.0") & "' rx='" & FORMAT(_Rx, "0.0") & "' fill='" & _fill & "'/>"
	VAR _yearLabel =
		"<text x='" & _cx & "' y='" & _YearY & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:4.5px; fill:#94A3B8; font-weight:500;'>" &
			FORMAT(_yr, "0") &
		"</text>"
	RETURN _valueLabel & _bar & _yearLabel,
	"",
	[@i], ASC
)

VAR _Empty =
	"<text x='" & _W/2 & "' y='" & _H/2 & "' text-anchor='middle' style='font-family:" & _fontFamily & "; font-size:11px; fill:#A0AEC0; font-style:italic;'>Дані відсутні</text>"

VAR _Body = IF(_BarCount = 0, _Empty, _Cols)

VAR _SVG =
	"<div style='width:100%;height:100%;overflow:hidden;display:flex;align-items:center;justify-content:center;'><svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 " & _W & " " & _H & "' preserveAspectRatio='xMidYMid meet' overflow='hidden' style='display:block; max-width:100%; max-height:100%; overflow:hidden;'>" &
		_Body &
	"</svg></div>"

RETURN  _SVG
```

### Джерела даних

Вихідні таблиці: `DM.R27_fact_OKR_Goals`, `DM.vw_R27_dim_Employee_Access_List`

Колонки: `Calc_Performance_Desc_Rate`, `Calc_Performance_Str_Rate`, `EMPLOYEE_ID`, `PLAN_YEAR`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_OKR_Goals`

Колонки: `dim_Admin_OS[EMPLOYEE_ID]`, `fact_OKR_Goals[Calc_Performance_Desc_Rate]`, `fact_OKR_Goals[Calc_Performance_Str_Rate]`, `fact_OKR_Goals[EMPLOYEE_ID]`, `fact_OKR_Goals[PLAN_YEAR]`

### Схема

```mermaid
graph LR
  M["PP.OKR.SVG.Last2Periods"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_OKR_Goals["fact_OKR_Goals"]
```

## Нотатки

_порожньо_
