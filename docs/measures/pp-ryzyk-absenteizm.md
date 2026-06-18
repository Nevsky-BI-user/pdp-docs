# PP.Ризик.Абсентеїзм

*тека `Personal_Profile\Паспорт\Ризики`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Ризики` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _v = [PP.Абсентеїзм]
RETURN
	IF(ISBLANK(_v), "Дані відсутні", FORMAT(_v, "0.0%"))
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["PP.Ризик.Абсентеїзм"]
```

---

## Бізнес-суть

Абсентеїзм

Sick_Leave_Day_Without_Pregnancy/(FTE_weighted_work_day_for_absenteeism+Sick_Leave_Day_Without_Pregnancy)

**Вимоги:** `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

**Використовує:** [PP.Абсентеїзм](../measures/pp-absenteizm.md)

## Нотатки

_порожньо_
