# AC.Export.Інтервал взаємодії (Viva), год. в день

*тека `Analytical Cases\Loss_Productivity\Export`*

## Бізнес-суть

Collab_Span_Norm_AVG_3month → Інтервал взаємодії (Viva), год. в день

**Вимоги:** `Кейс-Втрати-Продуктивності-Працівників`

## На сторінках звіту

[Продуктивність працівників](../report/produktyvnist-pratsivnykiv.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

---

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Analytical Cases\Loss_Productivity\Export` |
| formatString | — |
| dataType | — |
| Прихована | ні |

### DAX

```dax
SELECTEDVALUE('fact_Loss_of_Productivity'[Collab_Span_Norm_AVG_3month])
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_fact_Loss_of_Productivity`

Колонки: `Collab_Span_Norm_AVG_3month`

Power Query: `fact_Loss_of_Productivity`

### Залежності (таблиці й колонки)

Таблиці: `fact_Loss_of_Productivity`

Колонки: `fact_Loss_of_Productivity[Collab_Span_Norm_AVG_3month]`

### Схема

```mermaid
graph LR
  M["AC.Export.Інтервал взаємодії (Viva), год. в день"]
  M --> fact_Loss_of_Productivity["fact_Loss_of_Productivity"]
```

## Нотатки

_порожньо_
