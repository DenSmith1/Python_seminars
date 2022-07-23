# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def simple_numbers(number: int):
    simple_numbers = []
        
    while number > 1:
        for i in range (2, number + 1):
            count = 0
            for j in range (2, i + 1):
                if i % j == 0:
                    count += 1
            if count == 1:
                if number % i == 0:
                    simple_numbers.append(i)
                    number //= i
    
    return simple_numbers

number_n = int(input('Введите натуральное число --> '))
print(simple_numbers(number_n))
