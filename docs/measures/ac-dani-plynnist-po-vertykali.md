# AC.Дані.Плинність % по вертикалі

*тека `Analytical Cases\Loss_Productivity\Main`*

## Бізнес-суть

Turnover → Плинність % по вертикалі; Turnover → Плинність (%)

Плинність по кадровому підрозділу Щоб порахувати плинність по структурі, яка містить в собі кілька кадрових підрозділів, потрібно показник Fired_Unit_Cnt по кожному підрозділу (не людині) зсумувати та поділити на суму Employee_Unit_Average по кожному підрозділу (не людині). Щоб визначити Fired_Unit_Cnt  та  Employee_Unit_Average по підрозділу, треба взяти їх значення по одному із працівників цього підрозділу, бо плинність по людині рахується по її підрозділу

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`, `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`, `Командний-профіль/Паспортна-частина-групового-профілю/Сторінка-Картка-команди`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Плинність % по вертикалі](../measures/ac-switch-plynnist-po-vertykali.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Loss_Productivity\Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _res = SELECTEDVALUE('fact_Loss_of_Productivity'[Turnover])
RETURN COALESCE(_res, "—")
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Turnover`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Turnover]`

### Схема

```mermaid
graph LR
  M["AC.Дані.Плинність % по вертикалі"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

## Нотатки

_порожньо_
