# PP.Розмір мережі (Холдинг, 3м)

*тека `Personal_Profile\Viva\Viva Networks`*

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
//     CALCULATE( 
//         [PP.Розмір мережі (співробітник, 3м)], 
//         REMOVEFILTERS( fact_Metrics )
//     ) 

VAR __val =
DIVIDE(
		SUM('fact_Viva_Metrics'[INTERNAL_NETWORK_SIZE]),
		CALCULATE(COUNTROWS('fact_Viva_Metrics'), NOT ISBLANK('fact_Viva_Metrics'[INTERNAL_NETWORK_SIZE])))

RETURN __val
```

### Джерела даних


Колонки: `INTERNAL_NETWORK_SIZE`

Power Query: `fact_Viva_Metrics`

### Залежності (таблиці й колонки)

Таблиці: `fact_Viva_Metrics`

Колонки: `fact_Viva_Metrics[INTERNAL_NETWORK_SIZE]`

### Схема

```mermaid
graph LR
  M["PP.Розмір мережі (Холдинг, 3м)"]
  M --> fact_Viva_Metrics["fact_Viva_Metrics"]
```

---

## Бізнес-суть

INTERNAL_NETWORK_SIZE → Розмір мережі контактів по  <br>співробітнику; INTERNAL_NETWORK_SIZE → Розмір мережі контактів по кадровому підрозділу співробітника; INTERNAL_NETWORK_SIZE → Розмір мережі контактів по напряму співробітника; INTERNAL_NETWORK_SIZE → Розмір мережі контактів по Холдингу; INTERNAL_NETWORK_SIZE → Розмір мережі контактів; INTERNAL_NETWORK_SIZE → internal_network_size_direction; INTERNAL_NETWORK_SIZE → internal_network_size_holding; INTERNAL_NETWORK_SIZE → Розмір мережі контактів по  <br>співробітнику за попередні три місяці; INTERNAL_NETWORK_SIZE → Розмір мережі контактів по  <br>підрозділу (команді); INTERNAL_NETWORK_SIZE → Розмір мережі контактів по напряму команди

Розрахункове значення.  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [DM.vw_R27_dim_Employee_Metric_Health_and_Wellbeing]  <br>Відбір по працівнику на пріортетному місцю роботи USER_ACCESS_ID.  <br>Розраховується як середньомісячне значення за попередні три місяці (розраховано в таблиці).<br>Якщо дані по працівнику у вітрині відсутні, то показати надпис "Дані відсутні" (наприклад, якщо немає ліцензії та працівник не користується teams чи outlook Розрахункове значення.  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Сторінка-Ефективність-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Direction_PDP`, `Індивідуальний-профіль-працівника/Сторінка-Взаємодія-Viva-та-залученість-працівника/Таблиця-vw_R27_calc_Viva_Holding_PDP`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Командний-профіль/Сторінка-Взаємодія-Viva-та-залученість-команд`, `Командний-профіль/Сторінка-Ефективність`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md) · [Group Profile](../report/group-profile.md)

## Пов'язані міри

**Використовує:** [PP.Розмір мережі (співробітник, 3м)](../measures/pp-rozmir-merezhi-spivrobitnyk-3m.md)

**Використовується в:** [PP.Розмір мережі (кадровий підрозділ, 3м)](../measures/pp-rozmir-merezhi-kadrovyi-pidrozdil-3m.md), [PP.Розмір мережі (напрям, 3м)](../measures/pp-rozmir-merezhi-napriam-3m.md), [PP.Розмір мережі (співробітник, 3м)](../measures/pp-rozmir-merezhi-spivrobitnyk-3m.md)

## Нотатки

_порожньо_
