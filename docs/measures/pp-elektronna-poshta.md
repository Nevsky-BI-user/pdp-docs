# PP.Електронна пошта

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
	SELECTEDVALUE('fact_Employee_List'[EMAIL]),
	"-"
)
```

## Джерела


Колонки: `EMAIL`

Power Query: `fact_Employee_List`

## Бізнес-суть

EMAIL → Електронна пошта

Якщо значення в полі відсутнє, то показати текст "Дані відсутні"

**Вимоги:** `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EMAIL]`

## Схема

```mermaid
graph LR
  M["PP.Електронна пошта"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
