# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def multip_numbers(list_numbers: list):
    multip_numbers = []
    multip = 0
    for i in range(len(list_numbers)//2):
        multip = list_numbers[i]*list_numbers[len(list_numbers)-1-i]
        multip_numbers.append(multip)
    if len(list_numbers)%2 == 1:
        multip_numbers.append(list_numbers[len(list_numbers)//2]**2)

    return multip_numbers

list_numbers = [2, 3, 4, 5, 6, 7, 8]

print(multip_numbers(list_numbers))
