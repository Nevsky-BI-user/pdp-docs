# PP.HRBP

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
	SELECTEDVALUE('fact_Employee_List'[EMPLOYEE_HRBP_NAME]),
	"-"
)
```

## Джерела


Колонки: `EMPLOYEE_HRBP_NAME`

Power Query: `fact_Employee_List`

## Бізнес-суть

HRBP

Поле зберігається в довіднику [ dm.vw_R27_dim_person]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP] та таблиці dm.vw_R27_dim_Employee_Special_Head_HRBP, через відповідний зв’язок за ключем [emp_hrbp_id] = id, щоб із  таблиці dm.vw_R27_dim_person по ключу emp_hrbp_id =person_key витягти значення  full_name.  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні"  <br>Якщо ПІБ HRBP не вміщається в одну строку, перенести на іншу ПІБ HRBP керівника команди  <br>А якщо різні у керівника і членів команди? Подив

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Допоміжні-вітрини-для-звіту/Денормалізація-даних-для-вітрини-DM.vw_R27_fact_Employee_List_PDP`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EMPLOYEE_HRBP_NAME]`

## Схема

```mermaid
graph LR
  M["PP.HRBP"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
