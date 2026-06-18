# PP.Адреса офісу (працівник)

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
COALESCE(
	SELECTEDVALUE('fact_Employee_List'[EMP_OFFICE_ADRESS]),
	"-"
)
```

## Джерела


Колонки: `EMP_OFFICE_ADRESS`

Power Query: `fact_Employee_List`

## Бізнес-суть

Адреса офісу (працівник)

Поле зберігається в довіднику [DM.vw_R27_dim_office]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем office_on_employee_key = office_key.  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні"

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Допоміжні-вітрини-для-звіту/Денормалізація-даних-для-вітрини-DM.vw_R27_fact_Employee_List_PDP`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EMP_OFFICE_ADRESS]`

## Схема

```mermaid
graph LR
  M["PP.Адреса офісу (працівник)"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
