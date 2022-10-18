# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = input("Введите текст через пробел:\n") # \n - перенос на след строку
print(f"Вводной текст: {txt}") # https://python-scripts.com/f-strings
find_txt = "абв"
list = [i for i in txt.split() if find_txt not in i] # split для разделения строки на список строк
print(f'Вывод: {" ".join(list)}') # join - метод объединения списка строк