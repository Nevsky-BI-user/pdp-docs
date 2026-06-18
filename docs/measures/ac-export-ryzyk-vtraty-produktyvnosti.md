# AC.Export.Ризик втрати продуктивності

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Loss_Productivity\Export` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
SELECTEDVALUE('fact_Loss_of_Productivity'[Total_Risk_Productive_Name])
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Total_Risk_Productive_Name`

Power Query: `fact_Loss_of_Productivity`

## Бізнес-суть

Total_Risk_Productive_Name → Ризик втрати продуктивності

**Вимоги:** `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника/Редизайн-паспортної-частини`, `Кейс-Втрати-Продуктивності-Працівників`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Total_Risk_Productive_Name]`

## Схема

```mermaid
graph LR
  M["AC.Export.Ризик втрати продуктивності"]
  M --> fact_Loss_of_Productivity
```

## Нотатки

_порожньо_
