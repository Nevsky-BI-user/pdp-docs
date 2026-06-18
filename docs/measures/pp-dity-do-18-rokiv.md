# PP.Діти до 18 років

*тека `Personal_Profile\Загальна інформація` · формат `0`*

## Бізнес-суть

Діти до 18 років

Поле зберігається в довіднику [dm.vw_R27_dim_person]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List], через відповідний зв’язок за ключем [person_key].

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Допоміжні-вітрини-для-звіту/Денормалізація-даних-для-вітрини-DM.vw_R27_fact_Employee_List_PDP`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SELECTEDVALUE('fact_Employee_List'[CHILDREN_AMOUNT_UNDER_18])
```

### Джерела даних


Колонки: `CHILDREN_AMOUNT_UNDER_18`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[CHILDREN_AMOUNT_UNDER_18]`

### Схема

```mermaid
graph LR
  M["PP.Діти до 18 років"]
  M --> fact_Employee_List["fact_Employee_List"]
```

## Нотатки

_порожньо_
