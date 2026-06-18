# PP.Ширина мережі (Холдинг, 3м)

*тека `Personal_Profile\Viva\Viva Networks`*

## Бізнес-суть

NETWORK_OUTSIDE_ORGANIZATION → Ширина мережі контактів по  <br>співробітнику; NETWORK_OUTSIDE_ORGANIZATION → Ширина мережі контактів по кадровому підрозділу співробітника; NETWORK_OUTSIDE_ORGANIZATION → Ширина мережі контактів по напряму співробітника; NETWORK_OUTSIDE_ORGANIZATION → Ширина мережі контактів по Холдингу; NETWORK_OUTSIDE_ORGANIZATION → Ширина мережі контактів; NETWORK_OUTSIDE_ORGANIZATION → network_outside_organization_direction; NETWORK_OUTSIDE_ORGANIZATION → network_outside_organization_holding; NETWORK_OUTSIDE_ORGANIZATION → Ширина мережі контактів по  <br>співробітнику за попередні три місяці; NETWORK_OUTSIDE_ORGANIZATION → Ширина мережі контактів по співробітнику за попередні три місяці; NETWORK_OUTSIDE_ORGANIZATION → Ширина мережі контактів по кадровому підрозділу (Команді); NETWORK_OUTSIDE_ORGANIZATION → Ширина мережі контактів по напряму команди

Розрахункове значення.  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [DM.vw_R27_dim_Employee_Metric_Health_and_Wellbeing]   <br>Відбір по працівнику [person_key], періоду [PERIOD], документу прийому.  <br>Потрібно значення NETWORK_OUTSIDE_ORGANIZATION поділити на три (розраховано в таблиці).<br>Якщо дані по працівнику у вітрині відсутні, то показати надпис "Дані відсутні" (наприклад, якщо немає ліцензії та прцівник не користується teams or outlook Розрахункове значення.  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової табли

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Сторінка-Ефективність-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Direction_PDP`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Holding_PDP`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту/Зміна-алгоритму-розрахунку-метрик-по-Viva-з-урахуванням-дати-завантаження-даних-до-DWH`, `Командний-профіль/Сторінка-Взаємодія-Viva-та-залученість-команд`, `Командний-профіль/Сторінка-Ефективність`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md) · [Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [PP.Ширина мережі (співробітник, 3м)](../measures/pp-shyryna-merezhi-spivrobitnyk-3m.md)

**Використовується в:** [PP.Ширина мережі (кадровий підрозділ, 3м)](../measures/pp-shyryna-merezhi-kadrovyi-pidrozdil-3m.md), [PP.Ширина мережі (напрям, 3м)](../measures/pp-shyryna-merezhi-napriam-3m.md), [PP.Ширина мережі (співробітник, 3м)](../measures/pp-shyryna-merezhi-spivrobitnyk-3m.md)

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Viva\Viva Networks` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
// VAR __val =
// CALCULATE(
//     [PP.Ширина мережі (співробітник, 3м)],
//     REMOVEFILTERS(fact_Metrics))

VAR __val =
DIVIDE(
		SUM('fact_Viva_Metrics'[NETWORK_OUTSIDE_ORGANIZATION]),
		CALCULATE(COUNTROWS('fact_Viva_Metrics'), NOT ISBLANK('fact_Viva_Metrics'[NETWORK_OUTSIDE_ORGANIZATION])))

RETURN __val
```

### Джерела даних


Колонки: `NETWORK_OUTSIDE_ORGANIZATION`

Power Query: `fact_Viva_Metrics`

### Залежності (таблиці й колонки)

Таблиці: `fact_Viva_Metrics`

Колонки: `fact_Viva_Metrics[NETWORK_OUTSIDE_ORGANIZATION]`

### Схема

```mermaid
graph LR
  M["PP.Ширина мережі (Холдинг, 3м)"]
  M --> fact_Viva_Metrics["fact_Viva_Metrics"]
```

## Нотатки

_порожньо_
