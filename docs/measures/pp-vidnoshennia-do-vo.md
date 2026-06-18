# PP.Відношення до ВО

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
		SELECTEDVALUE('fact_Employee_List'[MILITARY_REGISTRATION_UKR]),
		"0"
	),
	"-"
)
```

### Джерела даних


Колонки: `MILITARY_REGISTRATION_UKR`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[MILITARY_REGISTRATION_UKR]`

### Схема

```mermaid
graph LR
  M["PP.Відношення до ВО"]
  M --> fact_Employee_List["fact_Employee_List"]
```

---

## Бізнес-суть

MILITARY_REGISTRATION_UKR → Відношення до ВО

Якщо значення в полі відсутнє, то показати текст "Дані відсутні"  або знак "-".

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
