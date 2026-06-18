# PP.Бронювання до

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
VAR __val =
COALESCE(
	IF(
		NOT(ISBLANK(SELECTEDVALUE('fact_Employee_List'[RESERVATION_END_DATE]))) 
		&& SELECTEDVALUE('fact_Employee_List'[IS_AT_RISK]) = 1 
		&& ABS(
				DATEDIFF(
					SELECTEDVALUE('fact_Employee_List'[RESERVATION_END_DATE]), 
					TODAY(),
					DAY
				)
			) < 30,
		"⚠️" 
		&
		SELECTEDVALUE('fact_Employee_List'[RESERVATION_END_DATE])
	, SELECTEDVALUE('fact_Employee_List'[RESERVATION_END_DATE])),
	"-"
)

RETURN __val
```

### Джерела даних


Колонки: `IS_AT_RISK`, `RESERVATION_END_DATE`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[IS_AT_RISK]`, `fact_Employee_List[RESERVATION_END_DATE]`

### Схема

```mermaid
graph LR
  M["PP.Бронювання до"]
  M --> fact_Employee_List["fact_Employee_List"]
```

---

## Бізнес-суть

**Бізнес-назва:** Бронювання до

### Опис із ТЗ

Якщо значення в полі відсутнє, то показати текст "Дані відсутні"  або знак "-".

**Вимоги (ТЗ):**

- [Індивідуальний профіль працівника › Сторінка Загальна інформація про працівника](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%86%D0%BD%D0%B4%D0%B8%D0%B2%D1%96%D0%B4%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0/%D0%A1%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0%20%D0%97%D0%B0%D0%B3%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%20%D1%96%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D1%96%D1%8F%20%D0%BF%D1%80%D0%BE%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0)

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Загальна інформація

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
