# PP.Адреса офісу (штат)

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
	SELECTEDVALUE('fact_Employee_List'[POSITION_OFFICE_ADRESS]),
	"-"
)
```

## Джерела


Колонки: `POSITION_OFFICE_ADRESS`

Power Query: `fact_Employee_List`

## Бізнес-суть

Адреса офісу (штат)

Поле зберігається в довіднику [DM.vw_R27_dim_office]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем  <br>office_on_position_key = office_key.  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні"

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Допоміжні-вітрини-для-звіту/Денормалізація-даних-для-вітрини-DM.vw_R27_fact_Employee_List_PDP`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[POSITION_OFFICE_ADRESS]`

## Схема

```mermaid
graph LR
  M["PP.Адреса офісу (штат)"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
