# PP.FinBP

*тека `Personal_Profile\Загальна інформація`*

## Бізнес-суть

FinBP

Поле зберігається в довіднику [ dm.vw_R27_dim_person]  <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP] та таблиці dm.vw_R27_dim_Employee_Special_Head_FinBP, через відповідний зв’язок за ключем [emp_finbp_id] = id, щоб із  таблиці dm.vw_R27_dim_person по ключу emp_finbp_id =person_key витягти значення  full_name.  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні"  <br>Якщо ПІБ FinBP не вміщається в одну строку, перенести на іншу ПІБ FinBP керівника команди  <br>Поле зберігається в довіднику [ dm.vw_R27_d

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Допоміжні-вітрини-для-звіту/Денормалізація-даних-для-вітрини-DM.vw_R27_fact_Employee_List_PDP`, `Командний-профіль/Паспортна-частина-групового-профілю/Редизайн-паспортної-частини-групового-профілю`, `Командний-профіль/Сторінка-Загальна-інформація-про-команду`

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
	SELECTEDVALUE('fact_Employee_List'[EMPLOYEE_FINBP_NAME]),
	"-"
)
```

### Джерела даних


Колонки: `EMPLOYEE_FINBP_NAME`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EMPLOYEE_FINBP_NAME]`

### Схема

```mermaid
graph LR
  M["PP.FinBP"]
  M --> fact_Employee_List["fact_Employee_List"]
```

## Нотатки

_порожньо_
