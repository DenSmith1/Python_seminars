# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


def koeffs(degree: int):                # создаем список кортежей, где 1 значение - коэффициент, второе - true/false(будет/нет этот член в многочлене)
    koeff = randint(0,100)
    formulas = [(koeff,1)]
    for i in range (degree):
        koeff = randint(0,100)
        koeff2 = randint(0,1)
        
        formulas.append((koeff, koeff2))

    return formulas

def polynomials(koeffs: list):      # создаем уравнение. степень обозначаем ^
    koeff = koeffs[0]
    formula_str = str(f'{koeff[0]}x^{len(koeffs)-1}+')  # первый коэфф. в степени должен быть всегда
    for i in range(1,len(koeffs)):
        koeff = koeffs[i]                               # присваиваю переменной тип кортеж
        if koeff[1] != 0:                               # вопрос: как здесь изменить условие, чтобы не использовать 24 строку?
            if (len(koeffs)-1-i) == 0:
                formula_str += str(f'{koeff[0]}+')
            else:
                formula_str += str(f'{koeff[0]}x^{len(koeffs)-1-i}+')

    formula_str = formula_str[:-1]+' = 0'
    return formula_str       

degree = int(input('Введите натуральную степень k --> '))
form = polynomials(koeffs(degree))
print (form)

path = 'Seminar4/polynom.txt'
with open(path, 'a') as add_file:
    add_file.write(f'{form}\n')