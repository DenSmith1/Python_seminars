# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def odd_index_sum(list_nuumbers: list):
    odd_index_sum = 0
    for i in range(len(list_numbers)):
        if i % 2 == 1:
            odd_index_sum += list_numbers[i]
    return odd_index_sum

list_numbers = [2, 3, 5, 9, 3, 11, 2, 8]

print(f'Сумма элементов на нечетных позициях = {odd_index_sum(list_numbers)}')

