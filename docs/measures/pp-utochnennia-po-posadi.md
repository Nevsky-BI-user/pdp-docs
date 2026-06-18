# PP.Уточнення по посаді

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
	SELECTEDVALUE('fact_Employee_List'[POSITION_SPECIFICATION]),
	"-"
)
```

### Джерела даних


Колонки: `POSITION_SPECIFICATION`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[POSITION_SPECIFICATION]`

### Схема

```mermaid
graph LR
  M["PP.Уточнення по посаді"]
  M --> fact_Employee_List["fact_Employee_List"]
```

---

## Бізнес-суть

POSITION_SPECIFICATION → Уточнення по посаді

Якщо значення в полі відсутнє, то показати текст "Дані відсутні" або знак "-".

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Загальна-інформація-про-працівника`

## На сторінках звіту

[Personal Profile](../report/personal-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
