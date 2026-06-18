# current_user_name

*тека `USER`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `USER` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _fullname =
    CALCULATE(
        VALUES('dim_Admin_OS'[EMPLOYEE_NAME]),
        'dim_Admin_OS'[EMPLOYEE_EMAIL] = USERPRINCIPALNAME()
    )
VAR _pos1 = FIND(" ", _fullname, 1, LEN(_fullname))
VAR _curr_time = HOUR(UTCNOW()+2)
VAR _intro =
    SWITCH(
        TRUE(),
        _curr_time < 10, ", доброго ранку!",
        _curr_time < 17, ", доброго дня!",
        ", доброго вечора!"
    )
RETURN 
IF(
    NOT ISBLANK(_fullname),
    MID(_fullname, _pos1 + 1, LEN(_fullname)) & _intro,
    ""
)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `EMPLOYEE_EMAIL`, `EMPLOYEE_NAME`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[EMPLOYEE_EMAIL]`, `dim_Admin_OS[EMPLOYEE_NAME]`

### Схема

```mermaid
graph LR
  M["current_user_name"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

---

## Бізнес-суть

??? note "Поля-джерела та пов'язані бізнес-метрики (1)"
    | Поле | Бізнес-метрики |
    |---|---|
    | `EMPLOYEE_NAME` | ПІБ співробітника |

**Вимоги (ТЗ):**

- [Індивідуальний профіль працівника › Історія по посадам › Реліз 1. Історія по посадам](https://dev.azure.com/MHPITDepProjects/People%20Digital%20Profile%20%28PDP%29/_wiki/wikis/PDP.wiki?pagePath=/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D1%96%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%B2%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8/%D0%92%D0%B8%D0%BC%D0%BE%D0%B3%D0%B8%20%D0%B4%D0%BE%20%D0%B7%D0%B2%D1%96%D1%82%D1%83%20People%20Digital%20Profile/%D0%86%D0%BD%D0%B4%D0%B8%D0%B2%D1%96%D0%B4%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9%20%D0%BF%D1%80%D0%BE%D1%84%D1%96%D0%BB%D1%8C%20%D0%BF%D1%80%D0%B0%D1%86%D1%96%D0%B2%D0%BD%D0%B8%D0%BA%D0%B0/%D0%86%D1%81%D1%82%D0%BE%D1%80%D1%96%D1%8F%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D0%B0%D0%B4%D0%B0%D0%BC/%D0%A0%D0%B5%D0%BB%D1%96%D0%B7%201.%20%D0%86%D1%81%D1%82%D0%BE%D1%80%D1%96%D1%8F%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D1%81%D0%B0%D0%B4%D0%B0%D0%BC)

## На сторінках звіту

_Не використовується на основних сторінках звіту._

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
