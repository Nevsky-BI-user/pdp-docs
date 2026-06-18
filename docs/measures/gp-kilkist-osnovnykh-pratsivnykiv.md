# GP.Кількість основних працівників

*тека `Group_Profile\Загальна інформація`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Group_Profile\Загальна інформація` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
"В розробці"
//VAR _res  = 
//    CALCULATE(
//        COUNTROWS('fact_Employee_List'), 
//        'fact_Employee_List'[POSITION_CATEGORY_INTERNAL_SORT] IN { 8, 2, 3, 6, 11}
//    )
//RETURN FORMAT(COALESCE(_res, "-"), "0")
```

### Джерела даних


Колонки: `POSITION_CATEGORY_INTERNAL_SORT`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[POSITION_CATEGORY_INTERNAL_SORT]`

### Схема

```mermaid
graph LR
  M["GP.Кількість основних працівників"]
  M --> fact_Employee_List["fact_Employee_List"]
```

---

## Бізнес-суть

POSITION_CATEGORY_INTERNAL_SORT → Доля Senior managers (%); POSITION_CATEGORY_INTERNAL_SORT → Доля Middle managers (%); POSITION_CATEGORY_INTERNAL_SORT → Доля Line  (%); POSITION_CATEGORY_INTERNAL_SORT → Доля Specialists (%); POSITION_CATEGORY_INTERNAL_SORT → Доля Workers (%)

Розрахункове поле: відношення кількості Senior managers у команді до загальної кількості працівників.  <br>Відношення кількості працівників, для яких position_category_internal_sort = 2 до загальної чисельності команди (метрика Кількість співробітників всього, чол.) Розрахункове поле: відношення кількості Middle managers у команді до загальної кількості працівників.  <br>Відношення кількості працівників, для яких position_category_internal_sort = 3 до загальної чисельності команди (метрика Кількість співробітників всього, чол.) Розрахункове поле: відношення кількості Line  у команді до загальн

**Вимоги:** `Командний-профіль/Сторінка-Загальна-інформація-про-команду`

## На сторінках звіту

[Group Profile](../report/group-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
