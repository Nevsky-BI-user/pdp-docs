# PP.Статус працівника

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
	SELECTEDVALUE('fact_Employee_List'[STATUS_NAME]),
	"-"
)
```

## Джерела


Колонки: `STATUS_NAME`

Power Query: `fact_Employee_List`

## Бізнес-суть

STATUS_NAME → Статус працівника; STATUS_NAME → Статус співробітника

Поле зберігається в довіднику [dm.vw_R27_dim_Employee_Status]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем [status_key].  <br>Поле Статус не може бути пустим, бо у працівника він завжди є.

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[STATUS_NAME]`

## Схема

```mermaid
graph LR
  M["PP.Статус працівника"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
