# PP.Середина вилки

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | `#,0` |
| dataType | — |
| Прихована | ні |

## DAX

```dax
MAX(fact_Employee_List[avg_tariff_rate])
```

## Джерела


Колонки: `avg_tariff_rate`

Power Query: `fact_Employee_List`

## Бізнес-суть

avg_tariff_rate → Середина вилки

Це поле має бути доступне у візуалізаціях, побудованих на основі фактової таблиці [dm.vw_R27_fact_Employee_List]  <br>Якщо значення в полі відсутнє, то показати текст "Дані відсутні" або знак "-"

**Вимоги:** `Індивідуальний-профіль-працівника/Сторінка-Винагорода-працівника`

## Залежності

Таблиці: `fact_Employee_List`

Колонки: `fact_Employee_List[avg_tariff_rate]`

## Схема

```mermaid
graph LR
  M["PP.Середина вилки"]
  M --> fact_Employee_List
```

## Нотатки

_порожньо_
