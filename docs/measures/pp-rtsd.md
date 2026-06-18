# PP.РЦД

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Життєвий цикл` |
| formatString | `#,0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
SUM('fact_Employee_History_Position'[ANNUAL_TARGET_INCOME])
```

## Джерела

Вихідні таблиці: `DM.vw_R27_fact_Employee_History_Position`

Колонки: `ANNUAL_TARGET_INCOME`

Power Query: `fact_Employee_History_Position`

## Бізнес-суть

ANNUAL_TARGET_INCOME → Відсоток приросту річного цільового доходу (РЦД)

Відсоток приросту = ((РЦД в поточній точці/РЦД в попередній точці)-1)*100%. Округлення до цілих.  <br>Якщо це найперша точка на графіку, то приріст = 0%.  <br>Якщо дані про РЦД відсутні, то проставити лейбл "Дані відсутні".

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`

## Залежності

Таблиці: `fact_Employee_History_Position`

Колонки: `fact_Employee_History_Position[ANNUAL_TARGET_INCOME]`

## Схема

```mermaid
graph LR
  M["PP.РЦД"]
  M --> fact_Employee_History_Position
```

## Нотатки

_порожньо_
