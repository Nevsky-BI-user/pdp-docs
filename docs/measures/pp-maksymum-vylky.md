# PP.Максимум вилки

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | `#,0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
MAX(fact_Employee_List[max_salary_range])
```

## Джерела


Колонки: `max_salary_range`

Power Query: `fact_Employee_List`

## Бізнес-суть

max_salary_range → Максимум вилки

Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List]  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні" або знак "-"

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[max_salary_range]`

## Схема

```mermaid
graph LR
  M["PP.Максимум вилки"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
