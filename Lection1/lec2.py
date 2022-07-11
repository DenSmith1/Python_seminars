# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.

#     *Пример:*

#     - Для N = 5: 1, -3, 9, -27, 81

# МОЙ ВАРИАНТ:

# def func(n: int):
#     a=1
#     for i in range(n):
#         print(a, end = ' ')
#         a *= -3

# n = int(input("Введите число n: 5"))
# func(n)

# ------------------------------------------------------------
# number = int(input("Введите количество шагов: "))

# def list_from(number: int):
#     list_numbers = []
#     for element in range (0, number):
#         list_numbers.append((-3)**element)
#     return list_numbers

# print(list_from(number))
# ------------------------------------------------------------

# Напишите программу, в которой пользователь будет задавать
# две строки, а программа - определять количество вхождений одной строки в другой.


orginal_text = str(input("Введите текст: "))
textt = str(input("Введите текст, который нужно найти: "))


def find_text(text1: str, text2: str):
    countt = 0
    for index in range(0,len(text1) - len(text2)+1):
        if text2 in text1[index:index+len(text2)]: 
            countt += 1

    return countt


print(f'Текст встречается: {find_text(orginal_text, textt)}  раз')

# org_text = input("Введите строку: ")
# find_text = input("Введите искомую строку: ")

# def text_finder(org_text: str, find_text: str):
#     counter = 0
#     for index in range (0, len(org_text) - len(find_text)+1):
#         if find_text in org_text[index:index+len(find_text)]: counter += 1
#     return counter

# print(f"Текст '{find_text}' втречается в тексте {text_finder(org_text, find_text)} раз")
