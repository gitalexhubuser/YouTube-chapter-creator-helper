import datetime, pyperclip

def convert_from(link):
    time_str = link.split('=')[1]
    time_sec = int(time_str)
    time = str(datetime.timedelta(seconds=time_sec))
    result = time + " - "
    pyperclip.copy(result)
    print(result)



try:
    while True:
        print('Нажми: Копировать URL видео с привязкой по времени и нажми Enter')
        x = input()
        convert_from(x)
except Exception as e:
    print("Произошла ошибка: ", e)
    input("Нажмите Enter чтобы выйти")
