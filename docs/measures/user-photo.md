# user_photo

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
VAR _url = 
	FIRSTNONBLANKVALUE(
		VALUES('dim_Admin_OS'[ORDER_NUM]),
		CALCULATE(SELECTEDVALUE('dim_Admin_OS'[URL_FOTO]))
	)
RETURN
IF (
	NOT ISBLANK ( _url ),
	"<div style='display:flex;justify-content:center;align-items:center;width:100%;height:100%;'>
		<img src='" & _url &
		"' width='150' height='150' style='border-radius:8px;object-fit:cover;'/>
	</div>"
)
```

### Джерела даних

Вихідні таблиці: `DM.vw_R27_dim_Employee_Access_List`

Колонки: `ORDER_NUM`, `URL_FOTO`

Power Query: `dim_Admin_OS`

### Залежності (таблиці й колонки)

Таблиці: `dim_Admin_OS`

Колонки: `dim_Admin_OS[ORDER_NUM]`, `dim_Admin_OS[URL_FOTO]`

### Схема

```mermaid
graph LR
  M["user_photo"]
  M --> dim_Admin_OS["dim_Admin_OS"]
```

---

## Бізнес-суть

!!! note "Бізнес-визначення відсутнє"
    Поля міри не зіставлено з wiki «Таблицями джерел даних». Можна заповнити вручну в `manualNotes`.

## На сторінках звіту

- [Group Profile](../report/group-profile.md)

## Пов'язані міри

_Прямих зв'язків з іншими мірами немає._

## Нотатки

_порожньо_
