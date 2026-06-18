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

### Опис із ТЗ

Якщо по працівнику  або по зведеній посаді не прописано формат авто, то проставити лейбл "Дані відсутні"

??? note "Поля-джерела та пов'язані бізнес-метрики (3)"
    | Поле | Бізнес-метрики |
    |---|---|
    | `emloyee_vehicle_format` | Тип опції по авто по працівнику · Тип опції по авто по працівнику (факт) · Опція по авто факт |

**Вимоги (ТЗ):**

- [Індивідуальний профіль працівника › Сторінка Винагорода працівника](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%86%D0%BD%D0%B4%D0%B8%D0%B2%D1%96%D0%B4%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0/%D0%A1%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0%20%D0%92%D0%B8%D0%BD%D0%B0%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0)
- [Індивідуальний профіль працівника › Сторінка Винагорода працівника › Доопрацювання сторінки ТРС](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%86%D0%BD%D0%B4%D0%B8%D0%B2%D1%96%D0%B4%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0/%D0%A1%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0%20%D0%92%D0%B8%D0%BD%D0%B0%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%B0%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0/%D0%94%D0%BE%D0%BE%D0%BF%D1%80%D0%B0%D1%86%D1%8E%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F%20%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8%20%D0%A2%D0%A0%D0%A1)
- [Командний профіль › Сторінка TRS команди › Доопрацювання сторінки TRS](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%9A%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C/%D0%A1%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0%20TRS%20%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8/%D0%94%D0%BE%D0%BE%D0%BF%D1%80%D0%B0%D1%86%D1%8E%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F%20%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8%20TRS)
- [Командний профіль › Сторінка Моя команда › ТЗ. Деталізація метрик групового профілю звіту](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%9A%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C/%D0%A1%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0%20%D0%9C%D0%BE%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B0/%D0%A2%D0%97.%20%D0%94%D0%B5%D1%82%D0%B0%D0%BB%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%8F%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%20%D0%B3%D1%80%D1%83%D0%BF%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8E%20%D0%B7%D0%B2%D1%96%D1%82%D1%83)

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [GP.Кількість співробітників всього, чол. - Integer](../measures/gp-kilkist-spivrobitnykiv-vsoho-chol-integer.md)

## Нотатки

_порожньо_
