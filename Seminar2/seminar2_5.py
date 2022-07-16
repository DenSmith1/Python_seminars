# Реализуйте алгоритм перемешивания списка.

from random import randint, random


list_original = [123, 25, 45, 12, 4523, 1111, 234]

def mix_list(list_original):
    new_list = list()
    range_list = len(list_original)
    while range_list > 0:
        k = randint(0, range_list-1)
        new_list.append(list_original[k])
        range_list -= 1
        list_original.remove(list_original[k])
    return new_list

print(f'Оригинальный список: {list_original}')
print(f'Перемешанный список: {mix_list(list_original)}')

