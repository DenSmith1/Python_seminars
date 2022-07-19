# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и  минимальным значением дробной части элементов.

def decimal_numbers_list(list_numbers: list):
    decim_numbers = []
    for i in range(len(list_numbers)):
        if type(list_numbers[i]) == float:
            decim = str(list_numbers[i])
            decim = decim.split('.')
            list_numbers[i] -= int(decim[0])
            decim_numbers.append(list_numbers[i])
    return decim_numbers

list_numbers = [1.1, 1.2, 3.1, 5, 10.01, 3.88]

decim_max = float(max(decimal_numbers_list(list_numbers)))
decim_min = float(min(decimal_numbers_list(list_numbers)))
print(f'Разница между максимальной и минимальной дробной частью элементов = {decim_max-decim_min}')


