# PP.Вид зайнятості

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
COALESCE(
	SELECTEDVALUE('fact_Employee_List'[EMPLOYMENT_TYPE]),
	"-"
)
```

## Джерела


Колонки: `EMPLOYMENT_TYPE`

Power Query: `fact_Employee_List`

## Бізнес-суть

EMPLOYMENT_TYPE → Вид зайнятості

Поле зберігається в довіднику [dm.vw_R27_dim_Employment_Type]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем [employment_type_key].

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EMPLOYMENT_TYPE]`

## Схема

```mermaid
graph LR
  M["PP.Вид зайнятості"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
