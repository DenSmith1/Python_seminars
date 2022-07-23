# Вычислить число c заданной точностью d

from cmath import pi

accuracy = input('Введите заданную точность d -->')
round_digits = len(accuracy)-2

# round_digits = int(input('До какого знака после запятой округлить число Pi? --> '))

str_pi = lambda x, y: str(x)[:y+2]
float_pi = float(str_pi(pi, round_digits))

print(float_pi)




