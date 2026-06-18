# PP.Відсоток зміни фіксованої винагороди

*тека `Personal_Profile\TRS` · формат `0.00%;-0.00%;0.00%`*

## Технічний опис

| Властивість | Значення |
|---|---|
| Тип | міра |
| Home table | _Measures |
| displayFolder | `Personal_Profile\TRS` |
| formatString | `0.00%;-0.00%;0.00%` |
| dataType | — |
| Прихована | ні |

### DAX

```dax
VAR _Now = [PP.Розмір фіксованої винагороди плановий, за місяць ПОТОЧНИЙ]
VAR _YearAgo = [PP.Розмір фіксованої винагороди плановий, за місяць СТАНОМ НА РІК НАЗАД]
VAR _result = DIVIDE(_Now-COALESCE(_YearAgo, _Now),_YearAgo, "Дані відсутні")
RETURN _result
```

### Джерела даних

—

### Залежності (таблиці й колонки)

—

### Схема

```mermaid
graph LR
  M["PP.Відсоток зміни фіксованої винагороди"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Personal Profile](../report/personal-profile.md) — Винагорода
- [TT:Зміна фікс винагороди](../report/tt-zmina-fiks-vynahorody.md)

## Пов'язані міри

**Використовує:** [PP.Розмір фіксованої винагороди плановий, за місяць ПОТОЧНИЙ](../measures/pp-rozmir-fiksovanoi-vynahorody-planovyi-za-misiats-potochnyi.md), [PP.Розмір фіксованої винагороди плановий, за місяць СТАНОМ НА РІК НАЗАД](../measures/pp-rozmir-fiksovanoi-vynahorody-planovyi-za-misiats-stanom-na-rik-nazad.md)

## Нотатки

_порожньо_
