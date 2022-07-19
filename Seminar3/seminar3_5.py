# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

def negafibonacci(n: int):
    a, b = 1, -1
    for i in range(0, -n, -1):
        yield a
        a, b = b, a - b
    
def fibonacci(n: int):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

number = int(input('Введите целое число: '))
data1 = list(negafibonacci(number))
data1 = data1[::-1]                     # разворот списка

data2 = list(fibonacci(number))
data = data1 + data2
print(data)

