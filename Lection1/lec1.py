# a = int(input('Введите число а:'))
# b = int(input('Введите число b:'))
# # if b == a*a:
# #     print(f'{b} квадрат числа {a}')
# # elif a == b*b:
# #     print(f'{a} квадрат числа {b}')
# # else:
# #     print('данные числа не являются квадратами друг друга')

# if (b == a * a) or (a == b * b):
#     print(' -> да')
# else:
#     print('-> нет')

# -------------------------------------------
# list = [0,0,0,0,0]        # list = []
# for i in range(5):
#     list[i] = int(input(f'Введите число {i} '))

# max_number = 0
# for i in range(5):
#     if list[i] > max_number:
#         max_number = list[i]

# print ('максимальное число', max_number)

# --------------------------------------------
# a = list()
# for i in range(5):
#     x = int(input('-->'))
#     a.append(x)

# maxx = a[0]

# for i in range(1,5): # range(1, len(a))  len(a) - длина списка; можно было указать for i in a
#     if a[i] > maxx:
#         maxx = a[i]

# print(maxx)
# --------------------------------------------
# a = int(input('--> '))
# x = -a
# while x <= a:
#     print(x, end = ' | ')
#     x += 1

# ---------------------------------------------
# a = int(input('--> '))
# if ((a % 5 == 0 and a % 10 == 0)) or ((a % 15 == 0) and not(a%30 == 0)): # ..and (a%30 !=0)
#     print('кратно')
# else:
#     print('не кратно')

# ---------------------------------------------
# a = float(input('-->'))

# b = int(a * 10)
# print(b % 10)

# ---------------------------------------------
x = input('x = ')

for i in range(len(x)):
    if x[i] == ',':
        print(x[i + 1])
        break
