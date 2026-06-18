# AC.Switch.Тренд оцінки результативності

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
SWITCH(
	SELECTEDVALUE('t_AC Burnout'[Burnout_Indicator]),
	"Оцінка", [AC.Чи є ризик вигорання по результатам оцінки результативності?],
	"Дані", [AC.Тренд оцінки результативності]
)
```

## Джерела


Колонки: `Burnout_Indicator`

## Бізнес-суть

Тренд оцінки результативності

Тренд оцінки результативності визначається порівнянням категорії працівника за останні два річні періоди.  <br>Якщо Last_Year_Performance_Str_Rate=Prev_Year_Performance_Str_Rate за за результатами двох останніх річних оцінок результативності, то Стабільний  <br>Якщо Last_Year_Performance_Str_Rate вище за Prev_Year_Performance_Str_Rate, то Зростання  <br>Якщо Last_Year_Performance_Str_Rate нижче за Prev_Year_Performance_Str_Rate, то Спадання.  <br>Якщо у працівника оцінка результативності присутня тільки за один період (рік), то ставити прочерк, наче дані відсутні.

**Вимоги:** `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## Залежності

Міри: [AC.Тренд оцінки результативності](../measures/ac-trend-otsinky-rezultatyvnosti.md), [AC.Чи є ризик вигорання по результатам оцінки результативності?](../measures/ac-chy-ie-ryzyk-vyhorannia-po-rezultatam-otsinky-rezultatyvnosti.md)

Таблиці: `t_AC Burnout`

Колонки: `t_AC Burnout[Burnout_Indicator]`

## Схема

```mermaid
graph LR
  M["AC.Switch.Тренд оцінки результативності"]
  M --> t_AC Burnout
```

## Нотатки

_порожньо_
