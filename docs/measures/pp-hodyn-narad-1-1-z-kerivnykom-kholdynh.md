# PP.Годин нарад 1:1 з керівником (Холдинг)

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
	SUM( 'fact_Viva_Metrics'[MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR] ),
	CALCULATE(
		COUNTROWS('fact_Viva_Metrics'),
		NOT(ISBLANK('fact_Viva_Metrics'[MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR]))))

RETURN __val
```

### Джерела даних


Колонки: `MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR`

Power Query: `fact_Viva_Metrics`

### Залежності (таблиці й колонки)

Таблиці: `fact_Viva_Metrics`

Колонки: `fact_Viva_Metrics[MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR]`

### Схема

```mermaid
graph LR
  M["PP.Годин нарад 1:1 з керівником (Холдинг)"]
  M --> fact_Viva_Metrics["fact_Viva_Metrics"]
```

---

## Бізнес-суть

MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Годин нарад 1:1 з керівником за період від поточної точки до попередньої точки; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Годин нарад 1:1 з керівником працівника; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Годин нарад 1:1 з керівником кадровому підрозділу співробітника; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Годин нарад 1:1 з керівником по напряму співробітника; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Годин нарад 1:1 з керівником по Холдингу; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → meeting_with_manager_one_to_one_hour_direction; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → meeting_with_manager_one_to_one_hour_cnt; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → meeting_with_manager_one_to_one_hour_holding; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Годин нарад 1:1 з керівником працівника за 3 попередніх місяці; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Чи є ризик вигорання через недостатню взаємодію з керівником?; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Годин 1:1 за попередні 3 міс.; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Годин нарад 1:1 з керівником кадровому підрозділу; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Годин нарад 1:1 з керівником по напряму команди; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Годин нарад 1:1 з керівником; MEETING_WITH_MANAGER_ONE_TO_ONE_HOUR → Рівень coaching (1:1), год/міс

<br>Розрахункове значення.  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [DM.vw_R27_dim_Employee_Metric_Health_and_Wellbeing]    <br>Відбір по працівнику [person_key], періоду [PERIOD], документу прийому [DOC_JOB_APPLICATION_ID].  <br>Якщо дані по працівнику у вітрині відсутні, то показати надпис "Дані відсутні" (наприклад, якщо немає ліцензії та прцівник не користується teams or outlook Розрахункове значення.  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [DM.vw_R27_dim_Employee_Metric_Health_and_Wellbeing]    <b

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Сторінка-Ефективність-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Direction_PDP`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Holding_PDP`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту/Зміна-алгоритму-розрахунку-метрик-по-Viva-з-урахуванням-дати-завантаження-даних-до-DWH`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту/Змінити-період-розрахунку-середніх-значень-по-Віва`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту/Змінити-трешхолд-1%3A1-для-кейсу-Утримання-працівника`, `Кейс-Утримання-працівників/Деталізація-метрик-в-кейсі-Утримання-співробітника`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Взаємодія-Viva-та-залученість-команд`, `Командний-профіль/Сторінка-Ефективність`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md) · [Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовується в:** [PP.Годин нарад 1:1 з керівником (кадровий підрозділ)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-kadrovyi-pidrozdil.md), [PP.Годин нарад 1:1 з керівником (напрям)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-napriam.md), [PP.Годин нарад 1:1 з керівником (співробітник)](../measures/pp-hodyn-narad-1-1-z-kerivnykom-spivrobitnyk.md)

## Нотатки

_порожньо_
