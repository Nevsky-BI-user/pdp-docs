# 'PP.Мобільний зв''язок - Назва пакету'

*тека `Personal_Profile\TRS`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _lim = MAX(fact_Mobile_Limit[PHONE_CORP_LIMIT])
VAR _person = VALUES('fact_Mobile_Limit'[PERSON_KEY])
RETURN
CALCULATE(
	IF(
		ISBLANK(_lim),
		"Відсутній",
		LASTNONBLANKVALUE(
			'fact_Mobile_Limit'[PERIOD],
			CALCULATE(MAX(fact_Mobile_Limit[PHONE_PACKAGE_NAME]))
		) &" - " &
		IF (
			_lim = 99999,
			"Безлімітний",
			LASTNONBLANKVALUE(
				'fact_Mobile_Limit'[PERIOD],
				CALCULATE(MAX(fact_Mobile_Limit[PHONE_CORP_LIMIT]))
			)
		)
	),
	ALL('fact_Mobile_Limit'[USER_ACCESS_ID]), ALL('dim_Admin_OS'[USER_ACCESS_ID]),
	TREATAS(_person, 'fact_Mobile_Limit'[PERSON_KEY])
)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`, `DM.vw_R27_fact_Mobile_Limit_PDP`

Колонки: `PERIOD`, `PERSON_KEY`, `PHONE_CORP_LIMIT`, `PHONE_PACKAGE_NAME`, `USER_ACCESS_ID`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`, `fact_Mobile_Limit`

Колонки: `dim_Admin_OS[USER_ACCESS_ID]`, `fact_Mobile_Limit[PERIOD]`, `fact_Mobile_Limit[PERSON_KEY]`, `fact_Mobile_Limit[PHONE_CORP_LIMIT]`, `fact_Mobile_Limit[PHONE_PACKAGE_NAME]`, `fact_Mobile_Limit[USER_ACCESS_ID]`

### Схема

```mermaid
graph LR
  M["'PP.Мобільний зв''язок - Назва пакету'"]
  M --> dim_Admin_OS["dim_Admin_OS"]
  M --> fact_Mobile_Limit["fact_Mobile_Limit"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
