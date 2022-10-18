# RLE алгоритм- https://tonais.ru/osnovy/kodirovanie-dlin-seriy-rle-python


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res

def decoding(text):
    number = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha(): # https://docs-python.ru/tutorial/operatsii-tekstovymi-strokami-str-python/metod-str-isalpha/
                                 # Метод строки str.isalpha() возвращает True,
                                 # если все символы в строке str являются буквенными и есть хотя бы один символ
                                 # (строка не пустая и не состоит из одного пробела), в противном случае False.
            number += text[i]
        else:
            res = res + text[i] * int(number)
            number = ''
    return res


s = input("Введите текст для проверки: ")
print(f"Текст после кодинга: {coding(s)}")
print(f"Текст после декодинга: {decoding(coding(s))}")