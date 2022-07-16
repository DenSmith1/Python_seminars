# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.

def multip_digits(number):
    a = list()
    multip_digits = 0
    for n in range (1, number+1):
        multip_digits += (1+1/n)**n     
        a.append(int(multip_digits))            # не совсем понял условие задачи. сделал как понял)
    return a

number = int(input('Введите целое число: '))
print(multip_digits(number))
