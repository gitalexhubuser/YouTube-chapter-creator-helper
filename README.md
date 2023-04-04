# YouTube chapter creator helper
<img src="Images/Header.jpg" width="100%" align="center"/>
## Описание
В строке 
``
https://youtu.be/5lwH4APNOuo?t=216
``
преобразует число в
``216``
в человеческие ``3 минуты и 36 секунд``

Вдохновился после просмотра вот [этого](https://youtu.be/Gmt3Nk9KoMc) видеоролика.

Решил сделать свой проект, чтоб более быстро и более удобно нарезать видео на главы.

<img src="Images/61c32b51b6c49d47a4ef7b14_YouTube-Chapters-1.png" width="30%" align="center"/>

Проверить что всё верно можно [тут](https://calculat.io/ru/date/seconds/370)

<img src="Images/woGD4aT6xQ.jpg" width="20%" align="center"/>


## Использование
### Вариант через буфер обмена - main.py
- нажать ``Копировать URL видео с привязкой по времени``

<img src="Images/wwJeQS06Tg.jpg" width="40%" align="center"/>

- открыть ``main.py`` и ввести результат копирования
- в буфере и в консоли окажется отформатированный вариант для вставки в описание под видео в творческой студии

### Вариант через регулярные выражения, чтение запись файла - description.py
- открыть description.txt
- 1-й строкой в самое начало вставить ``00:00:00 - ``
- вставить любое кол-во ссылок с тайм кодом и дать им описание
- запустить description.py
- наблюдать изменения в description.txt

## Ссылки
| Описание | Ссылка |
| ------ | ------ |
Репо: | https://github.com/gitalexhubuser/YouTube-timecode-helper
