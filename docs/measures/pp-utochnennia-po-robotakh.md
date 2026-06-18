# PP.Уточнення по роботах

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
IF(
	SELECTEDVALUE('fact_Employee_List'[POSITION_JOB_SPECIFICATION]) = "",
	"-")
```

## Джерела


Колонки: `POSITION_JOB_SPECIFICATION`

Power Query: `fact_Employee_List`

## Бізнес-суть

POSITION_JOB_SPECIFICATION → Уточнення по роботам

Поле зберігається в довіднику [dm.vw_R27_dim_position]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем [position_key] = [position_code_key].  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні"  або знак "-".  <br>Якщо значення не вміщається в одну строку, перенести на іншу

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[POSITION_JOB_SPECIFICATION]`

## Схема

```mermaid
graph LR
  M["PP.Уточнення по роботах"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
