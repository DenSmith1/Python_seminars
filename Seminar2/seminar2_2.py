# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

def multip_digits(number):
    a = list()
    multip_digits = 1
    for i in range (1, number+1):
        multip_digits *= i
        a.append(multip_digits)
    return a

number = int(input('Введите целое число: '))
print(multip_digits(number))

