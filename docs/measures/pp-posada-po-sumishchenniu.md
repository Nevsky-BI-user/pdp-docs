# PP.Посада по суміщенню

*тека `Personal_Profile\Загальна інформація`*

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
"В розробці"
// COALESCE(
//     SELECTEDVALUE('fact_Employee_List'[EMPLOYEE_ADMIN_NAME]),
//     "-"
// )
```

### Джерела даних


Колонки: `EMPLOYEE_ADMIN_NAME`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EMPLOYEE_ADMIN_NAME]`

### Схема

```mermaid
graph LR
  M["PP.Посада по суміщенню"]
  M --> fact_Employee_List["fact_Employee_List"]
```

---

## Бізнес-суть

EMPLOYEE_ADMIN_NAME → Адміністративний керівник

Поле зберігається в довіднику [dm.vw_R27_dim_Employee_Special_Head_admin]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем [emp_head_admin_id] = id.  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні"  <br>Якщо ПІБ керівника не вміщається в одну строку, перенести на іншу

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
