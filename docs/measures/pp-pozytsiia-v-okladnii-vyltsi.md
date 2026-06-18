# PP.Позиція в окладній вилці

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
VAR _salary = MAX(fact_Employee_List[MIN_TARIFF_RATE])
vAR _salary_total = _salary + [PP.Роз'їзний характер роботи, грн] +[PP.Доплата за шкідливі умови праці,грн] + [PP.Премія за місяць, грн]
VAR _min = MAX(fact_Employee_List[min_salary_range])
VAR _max = MAX(fact_Employee_List[max_salary_range])
VAR _mid_range = MAX(fact_Employee_List[AVG_TARIFF_RATE])
VAR _position =  DIVIDE(_salary - _mid_range, _mid_range)
VAR _result = 
SWITCH(
	TRUE(),
	_salary_total < _min, "Нижче мінімума",
    _salary_total > _max, "Вище максимуму",
	_position <= -0.051, "Мінімум-середина",
	_position <= 0.05 , "Cередина",
	_position > 0.05, "Середина-Максимум",
	"Дані відсутні"
)
RETURN --_result & ":  " & 
DIVIDE(_salary_total, _mid_range)
```

## Джерела


Колонки: `AVG_TARIFF_RATE`, `MIN_TARIFF_RATE`, `max_salary_range`, `min_salary_range`

Power Query: `fact_Employee_List`

## Бізнес-суть

AVG_TARIFF_RATE → Середина вилки; MIN_TARIFF_RATE → Оклад; MIN_TARIFF_RATE → Позиція в окладній вилці; MIN_TARIFF_RATE → Зарплата (вилки); MIN_TARIFF_RATE → Розподіл за вилкою зарплат; MIN_TARIFF_RATE → Положення у вилці; max_salary_range → Максимум вилки

Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List]  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні" або знак "-" Розрахункове поле.  <br>Потрібно визначити в якому діапазоні знаходиться сума значень (min_tariff_rate + сума доплати за роз'їзний характер роботи+сума доплати за шкідливі умови праці+премія за місяць.)  <br>Сума доплати за роз'їзний характер роботи - значення поля PAYMENT_PLAN_SUM, де  ACCRUAL_ORG_CODE = 00193, IS_ACTUAL  = "1", END_DATE > поточна дата, або END_DATE = "01.01.2001  <br>Сума доплати за

**Вимоги:** `Індивідуальний-профіль-працівника/Історія-по-посадам`, `Індивідуальний-профіль-працівника/Історія-по-посадам/Реліз-1.-Історія-по-посадам`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`, `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника/Доопрацювання-сторінки-ТРС`, `Допоміжні-вітрини-для-звіту/Таблиця-для-розрахунку-агрегованих-метрик-по-звіту`, `Командний-профіль/Сторінка-TRS-команди`, `Командний-профіль/Сторінка-TRS-команди/Сторінка-Винагорода-групового-профілю#вимоги-до-звіту`, `Командний-профіль/Сторінка-Моя-команда/ТЗ.-Деталізація-метрик-групового-профілю-звіту`

## Залежності

Міри: [PP.Доплата за шкідливі умови праці,грн](../measures/pp-doplata-za-shkidlyvi-umovy-pratsi-hrn.md), [PP.Премія за місяць, грн](../measures/pp-premiia-za-misiats-hrn.md)

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[AVG_TARIFF_RATE]`, `fact_Employee_List[MIN_TARIFF_RATE]`, `fact_Employee_List[max_salary_range]`, `fact_Employee_List[min_salary_range]`

## Схема

```mermaid
graph LR
  M["PP.Позиція в окладній вилці"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
