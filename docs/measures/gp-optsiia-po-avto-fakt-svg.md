# GP.Опція по авто, % факт.SVG

*тека `Group_Profile\TRS`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
/* *********** 1. ОТРИМАННЯ ТА ПІДГОТОВКА ДАНИХ *********** */
VAR _MaxVal = MAXX( ALLSELECTED('fact_Employees_Attributes'[emloyee_vehicle_format]), [GP.Кількість співробітників всього, чол. - Integer] )

VAR _Data = 
    ADDCOLUMNS(
        VALUES('fact_Employees_Attributes'[emloyee_vehicle_format]),
        "@Val", [GP.Кількість співробітників всього, чол. - Integer]
    )

VAR _FilteredData = FILTER(_Data, NOT(ISBLANK('fact_Employees_Attributes'[emloyee_vehicle_format])) && [@Val] > 0)
VAR _CountItems = COUNTROWS(_FilteredData)

VAR _DataWithRank = 
    GENERATE(
        _FilteredData,
        VAR _CurrVal = [@Val]
        VAR _CurrCat = 'fact_Employees_Attributes'[emloyee_vehicle_format]
        VAR _Rank = 
            COUNTROWS(
                FILTER(
                    _FilteredData,
                    [@Val] > _CurrVal || ([@Val] = _CurrVal && 'fact_Employees_Attributes'[emloyee_vehicle_format] <= _CurrCat)
                )
            )
        RETURN ROW("@Rank", _Rank)
    )

/* *********** 2. НАЛАШТУВАННЯ *********** */
VAR _CanvasWidth = 650
VAR _CanvasHeight = COUNTROWS(_Data) * 30

VAR _BarHeight = 20         -- Робимо бари тоншими у формі пігулки
VAR _Gap = 8                -- Зменшуємо відступ між барами
VAR _TopMargin = 15         -- Відступ зверху
VAR _LeftMargin = 250       -- Збільшено! Тепер є багато місця для довгих назв зліва
VAR _RightMargin = 40
VAR _MaxBarWidth = _CanvasWidth - _LeftMargin - _RightMargin - 15

VAR _ColorBar = "#6EBE91"   -- Приглушений зелений
VAR _ColorTrack = "#F5F5F5" -- Світло-сірий фон
VAR _ColorText = "#003A5D"  -- Колір назв
VAR _ColorValue = "#1F4E79" -- Колір цифр
VAR _Radius = _BarHeight / 2 -- Ідеальне скруглення (8px)

/* *********** 3. ГЕНЕРАЦІЯ ЕЛЕМЕНТІВ *********** */
VAR _SVG_Bars = 
    CONCATENATEX(
        _DataWithRank,
        VAR _YPos = _TopMargin + ([@Rank] - 1) * (_BarHeight + _Gap)
        VAR _BarW = DIVIDE([@Val], _MaxVal, 0) * _MaxBarWidth
        VAR _Label = 'fact_Employees_Attributes'[emloyee_vehicle_format]
        VAR _ValueFormat = FORMAT([@Val], "#,0")
        
        RETURN
        "<g>" &
            -- Назва категорії (вирівнювання праворуч)
            "<text x='" & (_LeftMargin - 10) & "' y='" & (_YPos + _BarHeight/2 + 4) & "' 
                text-anchor='end' font-family='Segoe UI' font-size='12' fill='" & _ColorText & "'>" & _Label & "</text>" &
            
            -- Фон (сірий трек)
            "<rect x='" & _LeftMargin & "' y='" & _YPos & "' width='" & _MaxBarWidth & "' height='" & _BarHeight & "' fill='" & _ColorTrack & "' rx='" & _Radius & "' />" &
            
            -- Бар (факт)
            IF([@Val] > 0, 
                "<rect x='" & _LeftMargin & "' y='" & _YPos & "' width='" & _BarW & "' height='" & _BarHeight & "' fill='" & _ColorBar & "' rx='" & _Radius & "' />", 
                ""
            ) &
            
            -- Значення цифра
            "<text x='" & (_LeftMargin + _BarW + 5) & "' y='" & (_YPos + _BarHeight/2 + 4) & "' 
                text-anchor='start' font-family='Segoe UI' font-weight='bold' font-size='11' fill='" & _ColorValue & "'>" & _ValueFormat & "</text>" &
        "</g>",
        "",
        [@Rank], ASC
    )

/* *********** 4. ФІНАЛЬНИЙ РЕНДЕР *********** */
VAR _SVG = 
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 " & _CanvasWidth & " " & _CanvasHeight & "'>" & 
    _SVG_Bars & 
    "</svg>"

RETURN 
    IF(_CountItems > 0, _SVG, BLANK())
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Employees_Attributes`

Колонки: `emloyee_vehicle_format`

Power Query: `fact_Employees_Attributes`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employees_Attributes`

Колонки: `fact_Employees_Attributes[emloyee_vehicle_format]`

### Схема

```mermaid
graph LR
  M["GP.Опція по авто, % факт.SVG"]
  M --> fact_Employees_Attributes["fact_Employees_Attributes"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [GP.Кількість співробітників всього, чол. - Integer](../measures/gp-kilkist-spivrobitnykiv-vsoho-chol-integer.md)

## Нотатки

_порожньо_
