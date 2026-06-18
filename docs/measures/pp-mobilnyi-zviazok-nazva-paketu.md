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

PERIOD → Дата нарахування премії Зірка МХП; PERIOD → Дата; PERIOD → Період нарахування; PERIOD → Період; PHONE_CORP_LIMIT → Мобільний зв'язок - Корпоративний ліміт; PHONE_CORP_LIMIT → Середні витрати на мобільний зв’язок; PHONE_CORP_LIMIT → Мобільний зв'язок; PHONE_PACKAGE_NAME → Мобільний зв'язок - Назва пакету

Це дата нарахування/виплати премії Зірка МХП (accrual_types_key = '9781d4aa-3a0d-1458-623a-7a93e90a2284'   та category_of_accrual_sort  = '2' ) Поточний період Потрібно відібрати всі записи по працівнику [person_key], періоду [Period], організації [organization_key]  <br>Якщо PHONE_CORP_LIMIT = "99999", виводимо значення "Безлімітний"  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні" або знак "-" Розрахункове.  <br>Потрібно зсумувати значення поля PHONE_CORP_LIMIT ( PHONE_CORP_LIMIT <> '99999') по членам команди, які мають компенсацію мобільного зв'язку, та поділити на кіль

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Деталізація-на-сторінці-Винагорода`, `Допоміжні-вітрини-для-звіту/Таблиця-(вью)-для-розрахунку-метрики-Укомплектованість-штату`, `Допоміжні-вітрини-для-звіту/Таблиця-періодична-(попередні-12-міс)-для-розрахунку-метрики-Середній-дохід`, `Командний-профіль/Сторінка-TRS-команди`, `Командний-профіль/Сторінка-TRS-команди/Сторінка-Винагорода-групового-профілю#вимоги-до-звіту`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
