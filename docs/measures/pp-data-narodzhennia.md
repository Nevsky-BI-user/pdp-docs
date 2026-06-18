# PP.Дата народження

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\_Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR birthDay = SELECTEDVALUE('fact_Employee_List'[EMP_BIRTH_DATE])
VAR age = 
YEAR(TODAY()) - YEAR(birthDay) - 
IF(FORMAT(TODAY(), "MMDD") < FORMAT(birthDay, "MMDD"), 1, 0)

VAR __val =
FORMAT(birthDay, "dd.mm.yyyy")
	& " - " 
	& age
	& "р."

RETURN __val
```

## Джерела


Колонки: `EMP_BIRTH_DATE`

Power Query: `fact_Employee_List`

## Бізнес-суть

Дата народження

Поле зберігається в довіднику [dm.vw_R27_dim_person]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List], через відповідний зв’язок за ключем [person_key].  <br>Дата у форматі dd.MM.yyyy<br>Поле Вік - розрахункове. Поточна дата - дата народження.

**Вимоги:** `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника`, `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника`, `Допоміжні-вітрини-для-звіту/Денормалізація-даних-для-вітрини-DM.vw_R27_fact_Employee_List_PDP`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EMP_BIRTH_DATE]`

## Схема

```mermaid
graph LR
  M["PP.Дата народження"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
