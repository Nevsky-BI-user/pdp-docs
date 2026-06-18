# PP.Формат роботи (штат)

*тека `Personal_Profile\Паспорт\_Main`*

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
	SELECTEDVALUE('fact_Employee_List'[POSITION_WORK_FORMAT]),
	"-"
)
```

### Джерела даних


Колонки: `POSITION_WORK_FORMAT`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[POSITION_WORK_FORMAT]`

### Схема

```mermaid
graph LR
  M["PP.Формат роботи (штат)"]
  M --> fact_Employee_List["fact_Employee_List"]
```

---

## Бізнес-суть

Формат роботи (штат)

Поле зберігається в довіднику [DM.vw_R27_dim_Work_Format]   <br>Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List_PDP], через відповідний зв’язок за ключем work_format_on_position_key = work_format_key.   <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні".

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`, `Допоміжні-вітрини-для-звіту/Денормалізація-даних-для-вітрини-DM.vw_R27_fact_Employee_List_PDP`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
