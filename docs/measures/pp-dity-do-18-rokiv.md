# PP.Діти до 18 років

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | `0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
SELECTEDVALUE('fact_Employee_List'[CHILDREN_AMOUNT_UNDER_18])
```

## Джерела


Колонки: `CHILDREN_AMOUNT_UNDER_18`

Power Query: `fact_Employee_List`

## Бізнес-суть

Діти до 18 років

Поле зберігається в довіднику [dm.vw_R27_dim_person]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List], через відповідний зв’язок за ключем [person_key].

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Допоміжні-вітрини-для-звіту/Денормалізація-даних-для-вітрини-DM.vw_R27_fact_Employee_List_PDP`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[CHILDREN_AMOUNT_UNDER_18]`

## Схема

```mermaid
graph LR
  M["PP.Діти до 18 років"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
