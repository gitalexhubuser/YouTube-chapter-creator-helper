﻿import re, pyperclip

def convert_file():

    with open('description.txt', 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()

    matches = re.findall(r'https://youtu.be/(\w+)\?t=(\d+)', text)
    for match in matches:
        video_id = match[0]
        seconds = int(match[1])
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        hr_tens, hr_ones = divmod(hours, 10)
        min_tens, min_ones = divmod(minutes, 10)
        sec_tens, sec_ones = divmod(seconds, 10)
        time_str = f"{hr_tens}{hr_ones}:{min_tens}{min_ones}:{sec_tens}{sec_ones}"
        replace_str = f"{time_str} -"
        text = text.replace(f"https://youtu.be/{video_id}?t={match[1]}", replace_str)
        pyperclip.copy(text)

    # открываем файл для записи
    with open('description.txt', 'w', encoding='utf-8', errors='replace') as f:
        f.write(text)


try:
    convert_file()
except Exception as e:
    print("Произошла ошибка: ", e)
    input("Нажмите Enter чтобы выйти")