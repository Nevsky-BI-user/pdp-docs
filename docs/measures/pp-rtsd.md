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

**Бізнес-назва:** Відсоток приросту річного цільового доходу (РЦД)

### Опис із ТЗ

Відсоток приросту = ((РЦД в поточній точці/РЦД в попередній точці)-1)*100%. Округлення до цілих.   Якщо це найперша точка на графіку, то приріст = 0%.   Якщо дані про РЦД відсутні, то проставити лейбл "Дані відсутні".

??? note "Поля-джерела та пов'язані бізнес-метрики (1)"
    | Поле | Бізнес-метрики |
    |---|---|
    | `ANNUAL_TARGET_INCOME` | Відсоток приросту річного цільового доходу (РЦД) |

**Вимоги (ТЗ):**

- [Індивідуальний профіль працівника › Історія по посадам › Реліз 1. Історія по посадам](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%86%D0%BD%D0%B4%D0%B8%D0%B2%D1%96%D0%B4%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0/%D0%86%D1%81%D1%82%D0%BE%D1%80%D1%96%D1%8F%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D0%B0%D0%B4%D0%B0%D0%BC/%D0%A0%D0%B5%D0%BB%D1%96%D0%B7%201.%20%D0%86%D1%81%D1%82%D0%BE%D1%80%D1%96%D1%8F%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D0%B0%D0%B4%D0%B0%D0%BC)

## На сторінках звіту

[Personal Profile](../report/personal-profile.md) · [TT:Життєвий цикл](../report/tt-zhyttievyi-tsykl.md)

## Пов'язані міри

**Використовується в:** [PP.Y_axis_rcd](../measures/pp-y-axis-rcd.md), [PP.min_Y_axis_rcd](../measures/pp-min-y-axis-rcd.md), [PP.Колір шапки тултіпу](../measures/pp-kolir-shapky-tultipu.md), [PP.Поточний РЦД](../measures/pp-potochnyi-rtsd.md), [PP.Приріст РЦД](../measures/pp-pryrist-rtsd.md)

## Нотатки

_порожньо_
