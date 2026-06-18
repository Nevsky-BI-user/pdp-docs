# PP.Годин взаємодії у неробочий час (Холдинг)

*тека `Personal_Profile\Viva\Viva Collaboration`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Viva\Viva Collaboration` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR __val =
DIVIDE(
	SUM( 'fact_Viva_Metrics'[TOTAL_AFTER_HOUR] ),
	SUM( 'fact_Viva_Metrics'[WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION] )
)

RETURN __val
```

### Джерела даних


Колонки: `TOTAL_AFTER_HOUR`, `WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION`

Power Query: `fact_Viva_Metrics`

### Залежності (таблиці й колонки)

Таблиці: `fact_Viva_Metrics`

Колонки: `fact_Viva_Metrics[TOTAL_AFTER_HOUR]`, `fact_Viva_Metrics[WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION]`

### Схема

```mermaid
graph LR
  M["PP.Годин взаємодії у неробочий час (Холдинг)"]
  M --> fact_Viva_Metrics["fact_Viva_Metrics"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — VIVA › Viva
- [Group Profile](../report/group-profile.md) — Viva

## Пов'язані міри

**Використовується в:** [PP.Годин взаємодії у неробочий час (кадровий підрозділ)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-kadrovyi-pidrozdil.md), [PP.Годин взаємодії у неробочий час (напрям)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-napriam.md), [PP.Годин взаємодії у неробочий час (співробітник)](../measures/pp-hodyn-vzaiemodii-u-nerobochyi-chas-spivrobitnyk.md)

## Нотатки

_порожньо_
