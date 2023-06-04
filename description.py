import re
from datetime import datetime, timedelta

def convert_time(link):
    time_str = re.search(r'\?t=(\d+)', link).group(1)
    # time_str = re.search(r'\s', link).group(1)
    # print(time_str)

    time_sec = int(time_str)
    delta = timedelta(seconds=time_sec)
    return (datetime.min + delta).time()

with open("description.txt", "r", encoding="utf-8") as file:

    lst = file.readlines()
    # print(links)
    # ['00:00:00 - О чём ролик\n', 'https://youtu.be/0K-q7MXF6B8?t=12 проблема с Удотом\n', 'https://youtu.be/0K-q7MXF6B8?t=53 дистанция холиауры\n', 'https://youtu.be/0K-q7MXF6B8?t=77 решение проблемы через адон\n', 'https://youtu.be/0K-q7MXF6B8?t=105 решение вопроса через ЕР\n', 'https://youtu.be/0K-q7MXF6B8?t=129 группа вк\n', 'https://youtu.be/0K-q7MXF6B8?t=130 группа вк\n', 'https://youtu.be/0K-q7MXF6B8?t=148 розыгрыш на 100 человек\n']

    for i in range(len(lst)):
        if '?t=' in lst[i]:
            time = convert_time(lst[i])
            lst[i] = re.sub(r'\?t=\d+', f'?t={time}', lst[i])

    with open("description.txt", "w", encoding="utf-8") as file:
        file.writelines(lst)

    # ['00:00:00 - О чём ролик\n', 'https://youtu.be/0K-q7MXF6B8?t=00:00:12 проблема с Удотом\n', 'https://youtu.be/0K-q7MXF6B8?t=00:00:53 дистанция холиауры\n', 'https://youtu.be/0K-q7MXF6B8?t=00:01:17 решение проблемы через адон\n', 'https://youtu.be/0K-q7MXF6B8?t=00:01:45 решение вопроса через ЕР\n', 'https://youtu.be/0K-q7MXF6B8?t=00:02:09 группа вк\n', 'https://youtu.be/0K-q7MXF6B8?t=00:02:10 группа вк\n', 'https://youtu.be/0K-q7MXF6B8?t=00:02:28 розыгрыш на 100 человек\n']



with open('description.txt', 'r') as f:
    data = f.read()

new_data = re.sub(r'https://youtu\.be/.*\?t=', '', data)

with open('description.txt', 'w') as f:
    f.write(new_data)
        
