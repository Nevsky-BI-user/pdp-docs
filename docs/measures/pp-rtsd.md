# PP.РЦД

*тека `Personal_Profile\Життєвий цикл` · формат `#,0`*

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

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Життєвий цикл
- [TT:Життєвий цикл](../report/tt-zhyttievyi-tsykl.md)

## Пов'язані міри

**Використовується в:** [PP.Y_axis_rcd](../measures/pp-y-axis-rcd.md), [PP.min_Y_axis_rcd](../measures/pp-min-y-axis-rcd.md), [PP.Колір шапки тултіпу](../measures/pp-kolir-shapky-tultipu.md), [PP.Поточний РЦД](../measures/pp-potochnyi-rtsd.md), [PP.Приріст РЦД](../measures/pp-pryrist-rtsd.md)

## Нотатки

_порожньо_
