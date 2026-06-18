# AC.Дані.Перепрацювання (Viva)

*тека `Analytical Cases\Loss_Productivity\Main`*

## Бізнес-суть

Viva_Overworking → Перепрацювання (Viva); Viva_Overworking → Чи є ризик вигорання через перепрацювання?; Viva_Overworking → Перепрацювання Viva

<br>**Нові вимоги.**<br>Якщо Viva_Overworking >= 1 год, то Ризик <br>**Старі вимоги.**<br> Визначається за значенням Viva_Overworking в залежності від категорії працівника:  <br>Якщо для position_category_internal_sort in ( 5, 6, 7) поле  Viva_Overworking >= 0,5 год, то Ризик.  <br>Якщо для  position_category_internal_sort in ( 3, 2)поле Viva_Overworking >= 0,75 год, то Ризик.  <br>Якщо для position_category_internal_sort = 1 поле  Viva_Overworking >= 1 год, то Ризик.  <br>Категорія працівника визначається із t_spo_hr_position_category_matrix по ключу position_category_internal_sort.

**Вимоги:** `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Кейс-Втрати-Продуктивності-Працівників`, `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [AC.Switch.Перепрацювання (Viva)](../measures/ac-switch-perepratsiuvannia-viva-2.md)

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
VAR _res = SELECTEDVALUE('fact_Loss_of_Productivity'[Viva_Overworking])
RETURN COALESCE(_res, "—")
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Viva_Overworking`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Viva_Overworking]`

### Схема

```mermaid
graph LR
  M["AC.Дані.Перепрацювання (Viva)"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

## Нотатки

_порожньо_
