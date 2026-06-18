# PP.РЦД

*тека `Personal_Profile\Життєвий цикл` · формат `#,0`*

!!! abstract "Джерела даних"
    `DM.vw_R27_fact_Employee_History_Position`

## Бізнес-суть

ANNUAL_TARGET_INCOME → Відсоток приросту річного цільового доходу (РЦД)

Відсоток приросту = ((РЦД в поточній точці/РЦД в попередній точці)-1)*100%. Округлення до цілих.  <br>Якщо це найперша точка на графіку, то приріст = 0%.  <br>Якщо дані про РЦД відсутні, то проставити лейбл "Дані відсутні".

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md) · [TT:Життєвий цикл](../report/tt-zhyttievyi-tsykl.md)

## Пов'язані міри

**Використовується в:** [PP.Y_axis_rcd](../measures/pp-y-axis-rcd.md), [PP.min_Y_axis_rcd](../measures/pp-min-y-axis-rcd.md), [PP.Колір шапки тултіпу](../measures/pp-kolir-shapky-tultipu.md), [PP.Поточний РЦД](../measures/pp-potochnyi-rtsd.md), [PP.Приріст РЦД](../measures/pp-pryrist-rtsd.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Життєвий цикл` |
| formatString | `#,0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SUM('fact_Employee_History_Position'[ANNUAL_TARGET_INCOME])
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Employee_History_Position`

Колонки: `ANNUAL_TARGET_INCOME`

Power Query: `fact_Employee_History_Position`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_History_Position`

Колонки: `fact_Employee_History_Position[ANNUAL_TARGET_INCOME]`

### Схема

```mermaid
graph LR
  M["PP.РЦД"]
  M --> fact_Employee_History_Position["fact_Employee_History_Position"]
```

## Нотатки

_порожньо_
