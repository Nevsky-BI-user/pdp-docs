# PP.Адреса офісу (працівник)

*тека `Personal_Profile\Паспорт\_Main`*

## Бізнес-суть

Адреса офісу (працівник)

Поле зберігається в довіднику [DM.vw_R27_dim_office]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем office_on_employee_key = office_key.  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні"

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Допоміжні-вітрини-для-звіту/Денормалізація-даних-для-вітрини-DM.vw_R27_fact_Employee_List_PDP`

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
| displayFolder | `Personal_Profile\Паспорт\_Main` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
COALESCE(
	SELECTEDVALUE('fact_Employee_List'[EMP_OFFICE_ADRESS]),
	"-"
)
```

### Джерела даних


Колонки: `EMP_OFFICE_ADRESS`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EMP_OFFICE_ADRESS]`

### Схема

```mermaid
graph LR
  M["PP.Адреса офісу (працівник)"]
  M --> fact_Employee_List["fact_Employee_List"]
```

## Нотатки

_порожньо_
