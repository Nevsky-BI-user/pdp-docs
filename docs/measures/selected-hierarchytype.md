# Selected.HierarchyType

*тека `Hierarchy`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Hierarchy` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SELECTEDVALUE('t_HierarchyTypes'[Hierarchy_Type_Name])
```

### Джерела даних


Колонки: `Hierarchy_Type_Name`

Power Query: `t_HierarchyTypes`

### Залежності (таблиці й колонки)

Таблиці: `t_HierarchyTypes`

Колонки: `t_HierarchyTypes[Hierarchy_Type_Name]`

### Схема

```mermaid
graph LR
  M["Selected.HierarchyType"]
  M --> t_HierarchyTypes["t_HierarchyTypes"]
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
