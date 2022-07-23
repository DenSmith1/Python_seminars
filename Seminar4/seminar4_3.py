#Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

from pickle import FALSE, TRUE

def find_repeat_numbers(list: list):
    new_list = [list[0]]
    for i in range(1, len(list)):
        find_number = TRUE
        for j in range(len(new_list)):
            if list[i] == new_list[j]:
                find_number = TRUE
                break
            else:
                find_number = FALSE
        if find_number is FALSE:
            new_list.append(list[i])
    return new_list

list_numbers = [1,2,3,4,1,1,6,7,3,5,1,6,4]
new_list = find_repeat_numbers(list_numbers)
print(new_list)

