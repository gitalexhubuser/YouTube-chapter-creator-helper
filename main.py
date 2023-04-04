import datetime

def convert_from(link):
    # text = 'https://youtu.be/Gmt3Nk9KoMc?t=370'

    # Извлечение времени из текста
    # - вызывается функция `split('=')`, которая разделяет строку "https://youtu.be/Gmt3Nk9KoMc?t=370" на массив подстрок, разделенных знаком "=": ["https://youtu.be/Gmt3Nk9KoMc?t", "370"].
    # time_str = link.split('=')[1].split('t=')[-1]
    time_str = link.split('=')[1]

    # Преобразование строки в число
    time_sec = int(time_str)

    # Вычисление времени
    time = str(datetime.timedelta(seconds=time_sec))

    # Вывод времени
    print(f"Время: {time}")




try:
    print('Нажми: Копировать URL видео с привязкой по времени и нажми Enter')
    x = input()
    # print("x", x)
    convert_from(x)
except Exception as e:
    print("Произошла ошибка: ", e)
    input("Нажмите Enter чтобы выйти")
