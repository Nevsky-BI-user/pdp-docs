# PP.Робочий телефон

*тека `Personal_Profile\Паспорт\_Main`*

## Бізнес-суть

PHONE_WORK → Робочий телефон

Поле зберігається в довіднику [dm.vw_R27_dim_person]<br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List], через відповідний зв’язок за ключем [person_key].<br>Якщо поле робочий телефон (phone_work) має значення, то виводити його. Якщо воно відсутнє (Null), то виводити особистий телефон (phone_personal).Якщо обидва поля відсутні, то показати текст "Дані відсутні"

**Вимоги:** `Індивідуальний-профіль-працівника/Паспортна-частина-індивідуального-профілю-співробітника/Сторінка-Картка-(паспорт)-працівника`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Паспорт\_Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
COALESCE(
	SELECTEDVALUE('fact_Employee_List'[PHONE_WORK]),
	SELECTEDVALUE('fact_Employee_List'[PHONE_PERSONAL]),
	"-"
)
```

### Джерела даних


Колонки: `PHONE_PERSONAL`, `PHONE_WORK`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[PHONE_PERSONAL]`, `fact_Employee_List[PHONE_WORK]`

### Схема

```mermaid
graph LR
  M["PP.Робочий телефон"]
  M --> fact_Employee_List["fact_Employee_List"]
```

## Нотатки

_порожньо_
