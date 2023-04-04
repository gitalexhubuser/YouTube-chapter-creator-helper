import datetime

# На первом шаге извлекаем время `370` из текста. 
# Затем преобразуем его в число `time_sec`. 
# Далее, используя метод `timedelta()`, вычисляем время `time` 
# в формате дни:часы:минуты:секунды. 
# Наконец, выводим результат на экран.

def convert_from(link):
    # text = 'https://youtu.be/Gmt3Nk9KoMc?t=370'
    text = link

    # Извлечение времени из текста
    time_str = text.split('=')[1].split('t=')[1]

    # Преобразование строки в число
    time_sec = int(time_str)

    # Вычисление времени
    time = str(datetime.timedelta(seconds=time_sec))

    # Вывод времени
    print(f"Время: {time}")




try:
    print('Нажми: Копировать URL видео с привязкой по времени и нажми Enter')
    x = input()
    convert_from(x)
except Exception as e:
    print("Произошла ошибка: ", e)
    input("Нажмите enter чтобы выйти")
