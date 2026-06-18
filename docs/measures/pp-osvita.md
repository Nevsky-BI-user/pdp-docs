# PP.Освіта

*тека `Personal_Profile\Загальна інформація`*

## Бізнес-суть

EDUCATION_LVL → Освіта; EDUCATION_LVL → Рівень освіти

Рівень освіти в останньому ВНЗ  <br>Поле зберігається в довіднику [dm.vw_R27_dim_person]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List], через відповідний зв’язок за ключем [person_key].  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні" або знак "-".

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника/Деталізація-блоку-Освіта`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
COALESCE(
	SELECTEDVALUE('fact_Employee_List'[EDUCATION_LVL]),
	"-"
)
```

### Джерела даних


Колонки: `EDUCATION_LVL`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EDUCATION_LVL]`

### Схема

```mermaid
graph LR
  M["PP.Освіта"]
  M --> fact_Employee_List["fact_Employee_List"]
```

## Нотатки

_порожньо_
