# AC.Switch.Ризик

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
	"Оцінка", [AC.Чи є ризик?],
	"Дані", [AC.Ризик]
)
```

## Джерела


Колонки: `Burnout_Indicator`

## Бізнес-суть

Ризик

**Вимоги:** `Кейс-Утримання-працівників/Опис-джерел-для-сторінки-%22Кейс-звільнення-(вигорання)%22`

## Залежності

Міри: [AC.Ризик](../measures/ac-ryzyk.md), [AC.Чи є ризик?](../measures/ac-chy-ie-ryzyk.md)

Таблиці: `t_AC Burnout`

Колонки: `t_AC Burnout[Burnout_Indicator]`

## Схема

```mermaid
graph LR
  M["AC.Switch.Ризик"]
  M --> t_AC Burnout
```

## Нотатки

_порожньо_
