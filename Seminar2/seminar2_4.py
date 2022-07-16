# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

def create_list(number):
    a = list()
    for i in range(-number,number+1):
        a.append(i)
    return a


def positions_to_int(positions):                            # подумал, что позиции могут состоять из более чем 1 символа, поэтому такое решение
    index = 0
    for i in range(len(positions)):
        if positions[i] == ' ':
            index = i
            break
    
    first_pos = int(f"{positions[0:index]}")                # попробовал записать по-разному, проверить как работает
    second_pos = int(positions[index+1:len(positions)])
    
    return first_pos, second_pos
    
number = int(input('Введите число: '))

list_numbers = create_list(number)
print('Ваш список: ')
print(list_numbers)

positions = input('Введите позиции в списке через пробел: ')

pos_1, pos_2 = positions_to_int(positions)

print(f'Произведение элементов {list_numbers[pos_1-1]} и {list_numbers[pos_2-1]} = {list_numbers[pos_1-1]*list_numbers[pos_2-1]}')
