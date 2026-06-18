# PP.Максимум вилки

*тека `Personal_Profile\TRS` · формат `#,0`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | `#,0` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
MAX(fact_Employee_List[max_salary_range])
```

### Джерела даних


Колонки: `max_salary_range`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[max_salary_range]`

### Схема

```mermaid
graph LR
  M["PP.Максимум вилки"]
  M --> fact_Employee_List["fact_Employee_List"]
```

---

## Бізнес-суть

max_salary_range → Максимум вилки

Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List]  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні" або знак "-"

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
