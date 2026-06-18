# AC.Switch.Тренд оцінки результативності

*тека `Analytical Cases\Burnout_Risk\Main`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Burnout_Risk\Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SWITCH(
	SELECTEDVALUE('t_AC Burnout'[Burnout_Indicator]),
	"Оцінка", [AC.Чи є ризик вигорання по результатам оцінки результативності?],
	"Дані", [AC.Тренд оцінки результативності]
)
```

### Джерела даних


Колонки: `Burnout_Indicator`

### Залежності (таблиці й колонки)

Таблиці: `t_AC Burnout`

Колонки: `t_AC Burnout[Burnout_Indicator]`

### Схема

```mermaid
graph LR
  M["AC.Switch.Тренд оцінки результативності"]
  M --> t_AC_Burnout["t_AC Burnout"]
```

---

## Бізнес-суть

**Бізнес-назва:** Тренд оцінки результативності

### Опис із ТЗ

Тренд оцінки результативності визначається порівнянням категорії працівника за останні два річні періоди.   Якщо `Last_Year_Performance_Str_Rate`=`Prev_Year_Performance_Str_Rate` за за результатами двох останніх річних оцінок результативності, то Стабільний   Якщо `Last_Year_Performance_Str_Rate` вище за `Prev_Year_Performance_Str_Rate`, то Зростання   Якщо `Last_Year_Performance_Str_Rate` нижче за `Prev_Year_Performance_Str_Rate`, то Спадання.   Якщо у працівника оцінка результативності присутня тільки за один період (рік), то ставити прочерк, наче дані відсутні.

Тренд оцінки результативності визначається порівнянням категорії працівника за останні два річні періоди.   Якщо `Last_Year_Performance_Str_Rate`=`Prev_Year_Performance_Str_Rate` за результатами двох останніх річних оцінок результативності, то Стабільний   Якщо `Last_Year_Performance_Str_Rate` вище за `Prev_Year_Performance_Str_Rate`, то Зростання   Якщо `Last_Year_Performance_Str_Rate` нижче за `Prev_Year_Performance_Str_Rate`, то Спадання.   Якщо у працівника оцінка результативності присутня тільки за один період (рік), то ставити прочерк, наче дані відсутні.

Тренд оцінки результативності визначається порівнянням категорії працівника за останні два річні періоди.   Якщо `Last_Year_Performance_Str_Rate`=`Prev_Year_Performance_Str_Rate` за за результатами двох останніх річних оцінок результативності, то **Стабільний**.  Якщо `Last_Year_Performance_Str_Rate` вище за `Prev_Year_Performance_Str_Rate`, то **Зростання**.  Якщо `Last_Year_Performance_Str_Rate` нижче за `Prev_Year_Performance_Str_Rate`, то **Спадання**. Але, якщо `Last_Year_Performance_Str_Rate` = А, а `Prev_Year_Performance_Str_Rate` = ТОП А, це має бути не спадання, а **Стабільний**.  Якщо у працівника оцінка результативності присутня тільки за один період (рік), то ставити прочерк, наче дані відсутні.

**Вимоги (ТЗ):**

- [Допоміжні вітрини для звіту › Таблиця для розрахунку агрегованих метрик по звіту](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%94%D0%BE%D0%BF%D0%BE%D0%BC%D1%96%D0%B6%D0%BD%D1%96%20%D0%B2%D1%96%D1%82%D1%80%D0%B8%D0%BD%D0%B8%20%D0%B4%D0%BB%D1%8F%20%D0%B7%D0%B2%D1%96%D1%82%D1%83/%D0%A2%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D1%8F%20%D0%B4%D0%BB%D1%8F%20%D1%80%D0%BE%D0%B7%D1%80%D0%B0%D1%85%D1%83%D0%BD%D0%BA%D1%83%20%D0%B0%D0%B3%D1%80%D0%B5%D0%B3%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%85%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%20%D0%BF%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83)
- [Допоміжні вітрини для звіту › Таблиця для розрахунку агрегованих метрик по звіту › Змінити логіку визначення тренду оцінки результативності](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%94%D0%BE%D0%BF%D0%BE%D0%BC%D1%96%D0%B6%D0%BD%D1%96%20%D0%B2%D1%96%D1%82%D1%80%D0%B8%D0%BD%D0%B8%20%D0%B4%D0%BB%D1%8F%20%D0%B7%D0%B2%D1%96%D1%82%D1%83/%D0%A2%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D1%8F%20%D0%B4%D0%BB%D1%8F%20%D1%80%D0%BE%D0%B7%D1%80%D0%B0%D1%85%D1%83%D0%BD%D0%BA%D1%83%20%D0%B0%D0%B3%D1%80%D0%B5%D0%B3%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%85%20%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%20%D0%BF%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83/%D0%97%D0%BC%D1%96%D0%BD%D0%B8%D1%82%D0%B8%20%D0%BB%D0%BE%D0%B3%D1%96%D0%BA%D1%83%20%D0%B2%D0%B8%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%BD%D1%8F%20%D1%82%D1%80%D0%B5%D0%BD%D0%B4%D1%83%20%D0%BE%D1%86%D1%96%D0%BD%D0%BA%D0%B8%20%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%BE%D1%81%D1%82%D1%96)
- [Кейс Утримання працівників › Опис джерел для сторінки %22Кейс звільнення (вигорання)%22](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%9A%D0%B5%D0%B9%D1%81%20%D0%A3%D1%82%D1%80%D0%B8%D0%BC%D0%B0%D0%BD%D0%BD%D1%8F%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D1%96%D0%B2/%D0%9E%D0%BF%D0%B8%D1%81%20%D0%B4%D0%B6%D0%B5%D1%80%D0%B5%D0%BB%20%D0%B4%D0%BB%D1%8F%20%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B8%20%2522%D0%9A%D0%B5%D0%B9%D1%81%20%D0%B7%D0%B2%D1%96%D0%BB%D1%8C%D0%BD%D0%B5%D0%BD%D0%BD%D1%8F%20%28%D0%B2%D0%B8%D0%B3%D0%BE%D1%80%D0%B0%D0%BD%D0%BD%D1%8F%29%2522)

## На сторінках звіту

[Утримання працівників](../report/utrymannia-pratsivnykiv.md)

## Пов'язані міри

**Використовує:** [AC.Тренд оцінки результативності](../measures/ac-trend-otsinky-rezultatyvnosti.md), [AC.Чи є ризик вигорання по результатам оцінки результативності?](../measures/ac-chy-ie-ryzyk-vyhorannia-po-rezultatam-otsinky-rezultatyvnosti.md)

## Нотатки

_порожньо_
