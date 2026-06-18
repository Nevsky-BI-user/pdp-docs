# Selected.HierarchyType

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Hierarchy` |
| formatString | — |
| dataType | — |
| Прихована | ні |

## DAX

```dax
SELECTEDVALUE('t_HierarchyTypes'[Hierarchy_Type_Name])
```

## Джерела


Колонки: `Hierarchy_Type_Name`

Power Query: `t_HierarchyTypes`

## Бізнес-суть

!!! warning "Без бізнес-визначення"
    Поля міри не знайдено у wiki «Таблицях джерел даних». Заповніть `manualNotes`.

## Залежності

Таблиці: `t_HierarchyTypes`

Колонки: `t_HierarchyTypes[Hierarchy_Type_Name]`

## Схема

```mermaid
graph LR
  M["Selected.HierarchyType"]
  M --> t_HierarchyTypes
```

## Нотатки

_порожньо_
