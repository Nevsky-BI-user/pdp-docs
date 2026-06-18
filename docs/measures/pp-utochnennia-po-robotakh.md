# PP.Уточнення по роботах

*тека `Personal_Profile\Загальна інформація`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
IF(
	SELECTEDVALUE('fact_Employee_List'[POSITION_JOB_SPECIFICATION]) = "",
	"-")
```

### Джерела даних


Колонки: `POSITION_JOB_SPECIFICATION`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[POSITION_JOB_SPECIFICATION]`

### Схема

```mermaid
graph LR
  M["PP.Уточнення по роботах"]
  M --> fact_Employee_List["fact_Employee_List"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Загальна інформація

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
