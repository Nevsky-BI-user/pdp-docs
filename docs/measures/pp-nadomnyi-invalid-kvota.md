# PP.Надомний інвалід (квота)

*тека `Personal_Profile\Загальна інформація`*

## Бізнес-суть

Надомний інвалід (квота)

<br>  <br>Якщо 1 - Так, якщо 0 - Ні.

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

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
	SWITCH(
		SELECTEDVALUE('fact_Employee_List'[DISABLED_TYPE]),
		"Технічні з інвалідністю", "Так",
		"Ні"
	),
	"-"
)
```

### Джерела даних


Колонки: `DISABLED_TYPE`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[DISABLED_TYPE]`

### Схема

```mermaid
graph LR
  M["PP.Надомний інвалід (квота)"]
  M --> fact_Employee_List["fact_Employee_List"]
```

## Нотатки

_порожньо_
