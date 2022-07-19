# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def int_to_bin(decimal_number: int):
    n = int('10')
    bin_num = int
    if decimal_number % 2 == 0:
        bin_num = int('0')
    else:
        bin_num = int(decimal_number % 2)

    while (decimal_number // 2 !=1):
        decimal_number //= 2
        bin_num += (decimal_number % 2) * n
        n *= 10

    if (decimal_number //2 == 1):
        bin_num += n
    return bin_num

decimal_number = int(input('Введите число: '))
print(int_to_bin(decimal_number))
