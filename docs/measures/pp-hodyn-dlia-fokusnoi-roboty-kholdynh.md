# PP.Годин для фокусної роботи (Холдинг)

*тека `Personal_Profile\Viva\Viva Collaboration`*

## Бізнес-суть

UNINTERRUPTED_HOUR → Годин для фокусної роботи  <br>співробітника; UNINTERRUPTED_HOUR → Годин для фокусної роботи  <br>по кадровому підрозділу співробітника; UNINTERRUPTED_HOUR → Годин для фокусної роботи  <br>по напряму співробітника; UNINTERRUPTED_HOUR → Годин для фокусної роботи  <br>по Холдингу; UNINTERRUPTED_HOUR → uninterrupted_hour_direction; UNINTERRUPTED_HOUR → uninterrupted_hour_holding; UNINTERRUPTED_HOUR → Годин для фокусної роботи  <br>співробітника за 3 попередніх місяці; UNINTERRUPTED_HOUR → Годин для фокусної роботи співробітника за 3 попередніх місяці; UNINTERRUPTED_HOUR → Годин для фокусної роботи  <br>по кадровому підрозділу; UNINTERRUPTED_HOUR → Годин для фокусної роботи  <br>по напряму команди

Розрахункове значення.  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [DM.vw_R27_dim_Employee_Metric_Health_and_Wellbeing]   <br>Відбір по працівнику [person_key], періоду [PERIOD], документу прийому [DOC_JOB_APPLICATION_ID].  <br>Розраховується як середньоденне значення за попередній місяць. Потрібно значення uninterrupted_hour поділити на кількість робочих днів в тому місяці. Якщо працівник пропрацював менше місяця, то рахувати за фактично відпрацьований період.  <br>Якщо дані по працівнику у вітрині відсутні, то показати надпис "Дані відсутні" (наприк

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Сторінка-Ефективність-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Direction_PDP`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Holding_PDP`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту/Зміна-алгоритму-розрахунку-метрик-по-Viva-з-урахуванням-дати-завантаження-даних-до-DWH`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту/Змінити-період-розрахунку-середніх-значень-по-Віва`, `Командний-профіль/Сторінка-Взаємодія-Viva-та-залученість-команд`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md) · [Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовується в:** [PP.Годин для фокусної роботи (кадровий підрозділ)](../measures/pp-hodyn-dlia-fokusnoi-roboty-kadrovyi-pidrozdil.md), [PP.Годин для фокусної роботи (напрям)](../measures/pp-hodyn-dlia-fokusnoi-roboty-napriam.md), [PP.Годин для фокусної роботи (співробітник)](../measures/pp-hodyn-dlia-fokusnoi-roboty-spivrobitnyk.md)

---

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
	SUM( 'fact_Viva_Metrics'[UNINTERRUPTED_HOUR]),
	SUM( 'fact_Viva_Metrics'[WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION])
)

RETURN __val
```

### Джерела даних


Колонки: `UNINTERRUPTED_HOUR`, `WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION`

Power Query: `fact_Viva_Metrics`

### Залежності (таблиці й колонки)

Таблиці: `fact_Viva_Metrics`

Колонки: `fact_Viva_Metrics[UNINTERRUPTED_HOUR]`, `fact_Viva_Metrics[WORKDAY_WITHOUT_SICKLEAVE_AND_VACATION]`

### Схема

```mermaid
graph LR
  M["PP.Годин для фокусної роботи (Холдинг)"]
  M --> fact_Viva_Metrics["fact_Viva_Metrics"]
```

## Нотатки

_порожньо_
