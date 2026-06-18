# PP.Годин керівника на взаємодію із безпосередніми підлеглими (Холдинг)

*тека `Personal_Profile\Viva\Viva management & Coaching`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Viva\Viva management & Coaching` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR __val =
DIVIDE(
	SUM( 'fact_Viva_Metrics'[MANAGER_COACHING_ONE_TO_ONE_HOUR] ),
	CALCULATE(
		COUNTROWS('fact_Viva_Metrics'),
		NOT(ISBLANK('fact_Viva_Metrics'[MANAGER_COACHING_ONE_TO_ONE_HOUR]))))

RETURN __val
```

### Джерела даних


Колонки: `MANAGER_COACHING_ONE_TO_ONE_HOUR`

Power Query: `fact_Viva_Metrics`

### Залежності (таблиці й колонки)

Таблиці: `fact_Viva_Metrics`

Колонки: `fact_Viva_Metrics[MANAGER_COACHING_ONE_TO_ONE_HOUR]`

### Схема

```mermaid
graph LR
  M["PP.Годин керівника на взаємодію із безпосередніми підлеглими (Холдинг)"]
  M --> fact_Viva_Metrics["fact_Viva_Metrics"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

[Personal Profile](../report/personal-profile.md) · [Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовується в:** [PP.Годин керівника на взаємодію із безпосередніми підлеглими (кадровий підрозділ)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-kadrovyi-pidrozdil.md), [PP.Годин керівника на взаємодію із безпосередніми підлеглими (напрям)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-napriam.md), [PP.Годин керівника на взаємодію із безпосередніми підлеглими (співробітник)](../measures/pp-hodyn-kerivnyka-na-vzaiemodiiu-iz-bezposerednimy-pidlehlymy-spivrobitnyk.md)

## Нотатки

_порожньо_
