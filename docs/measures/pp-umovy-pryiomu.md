# PP.Умови прийому

*тека `Personal_Profile\Загальна інформація`*

## Бізнес-суть

Умови прийому

Потрібно змапити із українськими відповідниками  <br>ВРЕМЕННО - Тимчасово  <br>БЕССРОЧНО - Безстроково  <br>НА_ПЕРИОД_ОТСУТСТВИЯ_ОСНОВНОГО_РАБОТНИКА - На період відсутності основного працівника  <br>НА_ОПРЕДЕЛЕННЫЙ_СРОК - На визначений термін  <br>ПЕРЕВОД - перевод  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні"  або знак "-".

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
	SELECTEDVALUE('fact_Employee_List'[EMP_HIRING_CONDITION_TYPE_CODE]),
	"-"
)
```

### Джерела даних


Колонки: `EMP_HIRING_CONDITION_TYPE_CODE`

Power Query: `fact_Employee_List`

### Залежності (таблиці й колонки)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[EMP_HIRING_CONDITION_TYPE_CODE]`

### Схема

```mermaid
graph LR
  M["PP.Умови прийому"]
  M --> fact_Employee_List["fact_Employee_List"]
```

## Нотатки

_порожньо_
