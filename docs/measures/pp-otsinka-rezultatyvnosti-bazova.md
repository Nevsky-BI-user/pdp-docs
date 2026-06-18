# PP.Оцінка результативності базова

*тека `Personal_Profile\Паспорт\Spider`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\Spider` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
AVERAGE('fact_Employee_Performance'[Official_Rate])
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Employee_Performance_PBI`

Колонки: `Official_Rate`

Power Query: `fact_Employee_Performance`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_Performance`

Колонки: `fact_Employee_Performance[Official_Rate]`

### Схема

```mermaid
graph LR
  M["PP.Оцінка результативності базова"]
  M --> fact_Employee_Performance["fact_Employee_Performance"]
```

---

## Бізнес-суть

Official_Rate → Оцінка керівника (Офіційна оцінка компетенції); Official_Rate → Оцінка кожного індикатора керівником

**Вимоги:** `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Зміна-джерела-даних-для-павутинки-Оцінка-результативності`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника/ТЗ-на-побудову-візуала-Павутинка-по-оцінці-результативності-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Результативність-та-оцінка`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`, `Командний-профіль/Сторінка-Результативність-та-оцінка-команди`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

**Використовується в:** [PP.Ініціативність при виконанні завдань](../measures/pp-initsiatyvnist-pry-vykonanni-zavdan.md), [PP.Автономність при виконанні завдань](../measures/pp-avtonomnist-pry-vykonanni-zavdan.md), [PP.Виконання завдань у встановлені терміни](../measures/pp-vykonannia-zavdan-u-vstanovleni-terminy.md), [PP.Відповідність кількості виконаних завдань функціоналу](../measures/pp-vidpovidnist-kilkosti-vykonanykh-zavdan-funktsionalu.md), [PP.Націленість на отримання результату](../measures/pp-natsilenist-na-otrymannia-rezultatu.md), [PP.Подолання перешкод при вирішенні проблем](../measures/pp-podolannia-pereshkod-pry-vyrishenni-problem.md), [PP.Прийняття відповідальності за отриманий результат](../measures/pp-pryiniattia-vidpovidalnosti-za-otrymanyi-rezultat.md), [PP.Якість результату виконаних завдань](../measures/pp-iakist-rezultatu-vykonanykh-zavdan.md)

## Нотатки

_порожньо_
