# AC.BR.Перепрацювання Viva

*тека `Analytical Cases\Burnout_Risk\Export`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Export` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SELECTEDVALUE('fact_Burnout_Indicators'[VIVA_OVERWORKING])
```

### Джерела даних


Колонки: `VIVA_OVERWORKING`

Power Query: `fact_Burnout_Indicators`

### Залежності (таблиці й колонки)

Таблиці: `fact_Burnout_Indicators`

Колонки: `fact_Burnout_Indicators[VIVA_OVERWORKING]`

### Схема

```mermaid
graph LR
  M["AC.BR.Перепрацювання Viva"]
  M --> fact_Burnout_Indicators["fact_Burnout_Indicators"]
```

---

## Бізнес-суть

VIVA_OVERWORKING → Перепрацювання (Viva); VIVA_OVERWORKING → Чи є ризик вигорання через перепрацювання?; VIVA_OVERWORKING → Перепрацювання Viva

<br>**Нові вимоги.**<br>Якщо Viva_Overworking >= 1 год, то Ризик <br>**Старі вимоги.**<br> Визначається за значенням Viva_Overworking в залежності від категорії працівника:  <br>Якщо для position_category_internal_sort in ( 5, 6, 7) поле  Viva_Overworking >= 0,5 год, то Ризик.  <br>Якщо для  position_category_internal_sort in ( 3, 2)поле Viva_Overworking >= 0,75 год, то Ризик.  <br>Якщо для position_category_internal_sort = 1 поле  Viva_Overworking >= 1 год, то Ризик.  <br>Категорія працівника визначається із t_spo_hr_position_category_matrix по ключу position_category_internal_sort.

**Вимоги:** `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Кейс-Втрати-Продуктивності-Працівників`, `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## На сторінках звіту

[Утримання працівників](../report/utrymannia-pratsivnykiv.md)

## Пов'язані міри

**Використовується в:** [AC.BR.Референтне значення.Viva](../measures/ac-br-referentne-znachennia-viva.md)

## Нотатки

_порожньо_
