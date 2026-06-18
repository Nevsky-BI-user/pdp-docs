# PP.Координатор для мобілізованих

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
"В розробці"
// COALESCE(
//     FORMAT(
//         SELECTEDVALUE('fact_Employee_List'[MILITARY_REGISTRATION]),
//         "0"
//     ),
//     "-"
// )
```

### Джерела даних


Колонки: `MILITARY_REGISTRATION`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[MILITARY_REGISTRATION]`

### Схема

```mermaid
graph LR
  M["PP.Координатор для мобілізованих"]
  M --> fact_Employee_List["fact_Employee_List"]
```

---

## Бізнес-суть

Координатор для мобілізованих

Дані відсутні в побудованих вітринах. Потрібно досліджувати джерело. Буде додано пізніше.

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника/Додаткові-кадрові-дані`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
