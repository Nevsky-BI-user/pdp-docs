# PP.Позика на ноутбук

*тека `Personal_Profile\TRS`*

## Бізнес-суть

LAND_SHARE_CONTRACT_SUM → Сума позики; LAND_SHARE_CONTRACT_SUM → Позика на ноутбук (остання); LAND_SHARE_CONTRACT_SUM → Доля команди з позикою на ноутбук (%) (діюча); LAND_SHARE_CONTRACT_SUM → Середній розмір позики; LAND_SHARE_CONTRACT_SUM → Позики

Потрібно відібрати всі записи по працівнику [person_key], періоду [Period], організації [organization_key] ,  договору [CONTRACT_KEY], де [BUDGET_ITEM_CODE] = '0000008240'  <br>Якщо по працівнику не знайшлося запису, то вивести прочерк "-" Розрахункове поле: відношення кількості працівників із діючою на поточний день позикою на ноутбук до загальної чисельності команди Потрібно зсумувати значення поля land_share_contract_sum по всім працівникам із діючою позикою та подялити на кількість таких працівників.

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Доопрацювання-сторінки-ТРС`, `Командний-профіль/Сторінка-TRS-команди`, `Командний-профіль/Сторінка-TRS-команди/Доопрацювання-сторінки-TRS`, `Командний-профіль/Сторінка-TRS-команди/Сторінка-Винагорода-групового-профілю#вимоги-до-звіту`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

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
| displayFolder | `Personal_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
CALCULATE(
	LASTNONBLANKVALUE(
		VALUES('dim_Date'[Date]),
		CALCULATE(SUM('fact_Repayment_Credit'[LAND_SHARE_CONTRACT_SUM]))
	),
	fact_Repayment_Credit[BUDGET_ITEM_CODE]="0000008240",
	'fact_Repayment_Credit'[IS_INCOMING] = TRUE()
)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Repayment_Credit_PDP`

Колонки: `BUDGET_ITEM_CODE`, `Date`, `IS_INCOMING`, `LAND_SHARE_CONTRACT_SUM`

Power Query: `dim_Date`

### Залежності (таблиці й колонки)

Таблиці: `dim_Date`, `fact_Repayment_Credit`

Колонки: `dim_Date[Date]`, `fact_Repayment_Credit[BUDGET_ITEM_CODE]`, `fact_Repayment_Credit[IS_INCOMING]`, `fact_Repayment_Credit[LAND_SHARE_CONTRACT_SUM]`

### Схема

```mermaid
graph LR
  M["PP.Позика на ноутбук"]
  M --> dim_Date["dim_Date"]
  M --> fact_Repayment_Credit["fact_Repayment_Credit"]
```

## Нотатки

_порожньо_
