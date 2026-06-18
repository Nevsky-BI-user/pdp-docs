# PP.Діти до 14 років

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
COALESCE(
	FORMAT(
		SELECTEDVALUE('fact_Employee_List'[CHILDREN_AMOUNT_UNDER_14]),
		"0"
	),
	"-"
)
```

### Джерела даних


Колонки: `CHILDREN_AMOUNT_UNDER_14`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[CHILDREN_AMOUNT_UNDER_14]`

### Схема

```mermaid
graph LR
  M["PP.Діти до 14 років"]
  M --> fact_Employee_List["fact_Employee_List"]
```

---

## Бізнес-суть

CHILDREN_AMOUNT_UNDER_14 → Діти до 14 років

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
