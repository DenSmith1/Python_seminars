# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

def digits_summary(number: float):
    digits_summary = 0
    number_str = str(number)

    for i in range(len(number_str)):
        if number_str[i] != '.':
            number_int = int(number_str[i])
            digits_summary += number_int
    return digits_summary

number = float(input('Ввведите вещественное число: '))

print(f'Сумма цифр числа = {digits_summary(number)}')


