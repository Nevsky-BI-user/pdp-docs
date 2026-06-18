# AC.Дані.Доля днів польових робіт (%)

*тека `Analytical Cases\Loss_Productivity\Main`*

## Бізнес-суть

Fieldwork_Share → Доля днів польових робіт (%)

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Доля днів польових робіт (%)](../measures/ac-switch-dolia-dniv-polovykh-robit.md)

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
VAR _res = SELECTEDVALUE('fact_Loss_of_Productivity'[Fieldwork_Share])
RETURN COALESCE(_res, "—")
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Fieldwork_Share`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Fieldwork_Share]`

### Схема

```mermaid
graph LR
  M["AC.Дані.Доля днів польових робіт (%)"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

## Нотатки

_порожньо_
