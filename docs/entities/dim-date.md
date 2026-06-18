# dim_Date

| Властивість | Значення |
|---|---|
| Тип | бізнес-сутність / таблиця |
| Сервер | — |
| База | — |
| Power Query | `dim_Date` |
| Джерела | — |

## Колонки

| Колонка | Тип | Джерело | Calc |
|---|---|---|---|
| Date | — | [Date] |  |
| Year | — | [Year] |  |
| MonthNumber | — | [MonthNumber] |  |
| MonthFull | — | [MonthFull] |  |
| MonthAbbr | — | [MonthAbbr] |  |
| WeekNumber | — | [WeekNumber] |  |
| DayOfMonth | — | [DayOfMonth] |  |
| DayOfWeek | — | [DayOfWeek] |  |
| DayOfWeekFull | — | [DayOfWeekFull] |  |
| DayOfWeekAbbr | — | [DayOfWeekAbbr] |  |
| QuarterAbbr | — | [QuarterAbbr] |  |
| Quarter | — | [Quarter] |  |
| QuarterNumber | — | [QuarterNumber] |  |
| FullDate | — | [FullDate] |  |
| FullDateNu | — | [FullDateNu] |  |
| Quarter and Year | — | [Quarter and Year] |  |
| MonthAndYearAbbr | — | [MonthAndYearAbbr] |  |
| SortMonth&Year | — | [SortMonth&Year] |  |
| Week&Year | — | [Week&Year] |  |
| Week&YearIndex | — | [Week&YearIndex] |  |
| TillToday | — | [TillToday] |  |
| Date d mmmm | — | [Date d mmmm] |  |
| SortDate d mmmm | — | [SortDate d mmmm] |  |

## Зв'язки

| Напрям | Колонка | Пов'язана таблиця | Колонка |
|---|---|---|---|
| to | PERIOD | `fact_TRS` | Date |
| to | PERIOD | `fact_Vacation_Reserve` | Date |
| to | PERIOD | `fact_Vacation` | Date |
| to | PERIOD | `fact_TRS_Plan` | Date |
| to | PERIOD | `fact_Mobile_Limit` | Date |
| to | period | `fact_Sick_Leaves` | Date |
| to | PERIOD | `fact_Repayment_Credit` | Date |
| to | PERIOD | `fact_Monthly_Viva_Insights` | Date |
| to | DISMISSAL_DATE | `fact_Burnout_Indicators` | Date |
| to | EXEC_DATE | `fact_OKR_Goals` | Date |
| to | DATE_ID | `fact_Employee_Performance_Total` | Date |
| to | PLAN_DATE | `fact_OKR_SVG` | Date |
| to | PERIOD | `fact_Employee_History_Position` | Date |

## Пов'язані міри

Усього: 54.
- [GP.Доля команди з позикою на ноутбук (%) (діюча)](../measures/gp-dolia-komandy-z-pozykoiu-na-noutbuk-diiucha.md)
- [GP.Доля команди з соціальними виплатами, %](../measures/gp-dolia-komandy-z-sotsialnymy-vyplatamy.md)
- [GP.Доля команди із доплатою за наставництво, %](../measures/gp-dolia-komandy-iz-doplatoiu-za-nastavnytstvo.md)
- [GP.Доля команди із премією МХП Зірки, %](../measures/gp-dolia-komandy-iz-premiieiu-mkhp-zirky.md)
- [GP.Доля команди із премією за Банк ідей, %](../measures/gp-dolia-komandy-iz-premiieiu-za-bank-idei.md)
- [GP.Доля команди із премією за збереження та розширення земельного банку, %](../measures/gp-dolia-komandy-iz-premiieiu-za-zberezhennia-ta-rozshyrennia-zemelnoho-banku.md)
- [GP.Доля команди із премією за програмою «Приведи друга», %](../measures/gp-dolia-komandy-iz-premiieiu-za-prohramoiu-pryvedy-druha.md)
- [GP.Доля команди із проектним бонусом за стратегічні ІТ проєкти, %](../measures/gp-dolia-komandy-iz-proektnym-bonusom-za-stratehichni-it-proiekty.md)
- [GP.Доля команди із разовою премією за програмою визнання, %](../measures/gp-dolia-komandy-iz-razovoiu-premiieiu-za-prohramoiu-vyznannia.md)
- [GP.Доля команди із інвестиційним проєктним бонусом, %](../measures/gp-dolia-komandy-iz-investytsiinym-proiektnym-bonusom.md)
- [GP.Доля учасників команди із зміною зарплати (окладу), %](../measures/gp-dolia-uchasnykiv-komandy-iz-zminoiu-zarplaty-okladu.md)
- [GP.Середня заробітна плата](../measures/gp-serednia-zarobitna-plata.md)
- [GP.Середній % зростання зарплати (окладу) за 12 міс](../measures/gp-serednii-zrostannia-zarplaty-okladu-za-12-mis.md)
- [GP.Середній розмір доплати за наставництво](../measures/gp-serednii-rozmir-doplaty-za-nastavnytstvo.md)
- [GP.Середній розмір премії МХП Зірки](../measures/gp-serednii-rozmir-premii-mkhp-zirky.md)
- [GP.Середній розмір премії за Банк ідей](../measures/gp-serednii-rozmir-premii-za-bank-idei.md)
- [GP.Середній розмір премії за збереження та розширення земельного банку](../measures/gp-serednii-rozmir-premii-za-zberezhennia-ta-rozshyrennia-zemelnoho-banku.md)
- [GP.Середній розмір премії за програмою «Приведи друга»](../measures/gp-serednii-rozmir-premii-za-prohramoiu-pryvedy-druha.md)
- [GP.Середній розмір проектного бонус за стратегічні ІТ проєкти](../measures/gp-serednii-rozmir-proektnoho-bonus-za-stratehichni-it-proiekty.md)
- [GP.Середній розмір разової премії за програмою визнання](../measures/gp-serednii-rozmir-razovoi-premii-za-prohramoiu-vyznannia.md)
- [GP.Середній розмір соціальної підтримки](../measures/gp-serednii-rozmir-sotsialnoi-pidtrymky.md)
- [GP.Середній розмір інвестиційного проєктного бонусу](../measures/gp-serednii-rozmir-investytsiinoho-proiektnoho-bonusu.md)
- [PP.SVG.OKR.Загальна оцінка](../measures/pp-svg-okr-zahalna-otsinka.md)
- [PP.Y_axis_rcd](../measures/pp-y-axis-rcd.md)
- [PP.history_position_maxd](../measures/pp-history-position-maxd.md)
- [PP.min_Y_axis_rcd](../measures/pp-min-y-axis-rcd.md)
- [PP.Інвестиційний проєктний бонус](../measures/pp-investytsiinyi-proiektnyi-bonus.md)
- [PP.Інші доплати](../measures/pp-inshi-doplaty.md)
- [PP.Доплата за наставництво](../measures/pp-doplata-za-nastavnytstvo.md)
- [PP.Доплати за суміщення](../measures/pp-doplaty-za-sumishchennia.md)
- [PP.Квартальні премії факт](../measures/pp-kvartalni-premii-fakt.md)
- [PP.Колір шапки тултіпу](../measures/pp-kolir-shapky-tultipu.md)
- [PP.Місяці без відпустки](../measures/pp-misiatsi-bez-vidpustky.md)
- [PP.Наставництво](../measures/pp-nastavnytstvo.md)
- [PP.Позика (активна).Сума](../measures/pp-pozyka-aktyvna-suma.md)
- [PP.Позика на ноутбук](../measures/pp-pozyka-na-noutbuk.md)
- [PP.Поточний РЦД](../measures/pp-potochnyi-rtsd.md)
- [PP.Премія МХП Зірки](../measures/pp-premiia-mkhp-zirky.md)
- [PP.Премія за Банк ідей](../measures/pp-premiia-za-bank-idei.md)
- [PP.Премія за внутрішнє тренерство](../measures/pp-premiia-za-vnutrishnie-trenerstvo.md)
- [PP.Премія за збереження та розширення земельного банку](../measures/pp-premiia-za-zberezhennia-ta-rozshyrennia-zemelnoho-banku.md)
- [PP.Премія за програмою «Приведи друга»](../measures/pp-premiia-za-prohramoiu-pryvedy-druha.md)
- [PP.Приріст РЦД](../measures/pp-pryrist-rtsd.md)
- [PP.Приріст окладу](../measures/pp-pryrist-okladu.md)
- [PP.Проектний бонус за стратегічні ІТ проєкти](../measures/pp-proektnyi-bonus-za-stratehichni-it-proiekty.md)
- [PP.Разова премія за програмою визнання](../measures/pp-razova-premiia-za-prohramoiu-vyznannia.md)
- [PP.Розмір фіксованої винагороди плановий, за місяць СТАНОМ НА РІК НАЗАД](../measures/pp-rozmir-fiksovanoi-vynahorody-planovyi-za-misiats-stanom-na-rik-nazad.md)
- [PP.Річні бонуси](../measures/pp-richni-bonusy.md)
- [PP.Соціальна підтримка](../measures/pp-sotsialna-pidtrymka.md)
- [PP.Цільовий розмір річної винагороди, до оподаткування (12 місяців назад)](../measures/pp-tsilovyi-rozmir-richnoi-vynahorody-do-opodatkuvannia-12-misiatsiv-nazad.md)
- [PP.Щоквартальні премії в середньому за квартал](../measures/pp-shchokvartalni-premii-v-serednomu-za-kvartal.md)
- [PP.Щомісячні премії накопичувально](../measures/pp-shchomisiachni-premii-nakopychuvalno.md)
- [PP.Щомісячні премії середньомісячно](../measures/pp-shchomisiachni-premii-serednomisiachno.md)
- [date_filters_check](../measures/date-filters-check.md)

## Нотатки

_порожньо_
