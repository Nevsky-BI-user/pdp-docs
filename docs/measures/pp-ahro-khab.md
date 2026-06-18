# PP.Агро Хаб

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
	SELECTEDVALUE('fact_Employee_List'[HAB_FOR_AGRO]),
	"-"
)
```

## Джерела


Колонки: `HAB_FOR_AGRO`

Power Query: `fact_Employee_List`

## Бізнес-суть

HAB_FOR_AGRO → Агро Хаб

Поле зберігається в довіднику [dm.vw_R27_dim_unit]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем [division_key] = [unit_key].  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні"  або знак "-".  <br>Якщо значення не вміщається в одну строку, перенести на іншу

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[HAB_FOR_AGRO]`

## Схема

```mermaid
graph LR
  M["PP.Агро Хаб"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
