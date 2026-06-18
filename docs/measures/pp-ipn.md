# PP.ІПН

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
	FORMAT(
		SELECTEDVALUE('fact_Employee_List'[TAX_CODE]),
		"0"
	),
	"-"
)
```

## Джерела


Колонки: `TAX_CODE`

Power Query: `fact_Employee_List`

## Бізнес-суть

TAX_CODE → ІПН

Поле зберігається в довіднику [dm.vw_R27_dim_person ]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List], через відповідний зв’язок за ключем [person_key].

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[TAX_CODE]`

## Схема

```mermaid
graph LR
  M["PP.ІПН"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
