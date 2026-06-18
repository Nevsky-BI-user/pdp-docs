# AC.Switch.Кількість місяців без якісної відпустки за ост. 3 роки

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
	"Оцінка", [AC.Чи є ризик вигорання через відсутність відпусток?],
	"Дані", COALESCE([AC.Кількість місяців без якісної відпустки], 0)
)
```

## Джерела


Колонки: `Burnout_Indicator`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Міри: [AC.Кількість місяців без якісної відпустки](../measures/ac-kilkist-misiatsiv-bez-iakisnoi-vidpustky.md), [AC.Чи є ризик вигорання через відсутність відпусток?](../measures/ac-chy-ie-ryzyk-vyhorannia-cherez-vidsutnist-vidpustok.md)

Таблиці: `t_AC Burnout`

Колонки: `t_AC Burnout[Burnout_Indicator]`

## Схема

```mermaid
graph LR
  M["AC.Switch.Кількість місяців без якісної відпустки за ост. 3 роки"]
  M --> t_AC Burnout
```

## Нотатки

_порожньо_
