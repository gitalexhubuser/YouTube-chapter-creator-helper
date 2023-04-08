import re, os, pyperclip

path = os.path.abspath(os.curdir) # path = os.getcwd()
print("path ", path)

input_file = path + "\\description.txt"
output_file = path + "\\description.txt"

def convert_file():
    # .*? - любое количество символов (включая нулевое), соответствующих любому символу, кроме перевода строки, нежадным способом (т.е. остановится на первом вхождении следующего шаблона)
    with open(input_file, 'r', encoding='utf8', errors='ignore') as f:
        text = f.read()

    matches = re.findall(r'https://youtu.be/(.*?)\?t=(\d+)', text)
    # print("matches ", matches)

    for match in matches:
        video_id = match[0] # print("video_id ", video_id)
        seconds = int(match[1]) # print("seconds ", seconds)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        hr_tens, hr_ones = divmod(hours, 10)
        min_tens, min_ones = divmod(minutes, 10)
        sec_tens, sec_ones = divmod(seconds, 10)
        time_str = f"{hr_tens}{hr_ones}:{min_tens}{min_ones}:{sec_tens}{sec_ones}"

        replace_str = f"{time_str} -"
        text = text.replace(f"https://youtu.be/{video_id}?t={match[1]}", replace_str)
        # pyperclip.copy(text)

    with open(output_file, 'w', encoding='utf8', errors='ignore') as f:
        # f.write("00:00:00 - \r\n") # вставить 00 00 если нету
        f.write(text)


try:
    convert_file()
except Exception as e:
    print("Произошла ошибка: ", e)
    input("Нажмите Enter чтобы выйти")
