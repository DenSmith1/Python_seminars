# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from pickle import FALSE, TRUE
from posixpath import split, splitext

path1 = 'Seminar4/polynom1.txt'
path2 = 'Seminar4/polynom2.txt'


with open (path1, 'r') as file:
    formula1 = file.readline()[0:-4].split(" + ") # преобразую в список, откидываю из многочлена " = 0"
    
with open (path2, 'r') as file:
    formula2 = file.readline()[0:-4].split(" + ") 

def formula_to_list(formula: str):  # преобразуем многочлен в список кортежей (коэфф, степень х)
    for i in range(len(formula)):
        if 'x^' in formula[i]:
            formula[i] = tuple(map(int,formula[i].split('x^')))
        elif 'x' in formula[i]:
            formula[i] = (int(formula[i][0:-1]),1)
        else:
            formula[i] = (int(formula[i]),0)
    return formula

def sum_of_polinoms(formula1: list, formula2: list): # находим сумму двух списков
    sum_of_polinoms = []
    hits = FALSE
    for i in range(len(formula1)):
        koeff1 = formula1[i]
        for j in range(len(formula2)):
            koeff2 = formula2[j]
            if koeff1[1] == koeff2[1]:
                sum = ((koeff1[0]+koeff2[0]),koeff1[1])
                sum_of_polinoms.append(sum)
                hits = TRUE
        if hits is FALSE:    
                sum_of_polinoms.append(koeff1)
      
    for j in range(len(formula2)):          # прогоняю вторую формулу на предмет совпадения элементов
        hits = FALSE 
        koeff2 = formula2[j]    
        for i in range(len(sum_of_polinoms)):
            koeff1 = sum_of_polinoms[i]
            if koeff2[1] == koeff1[1]:
                hits = TRUE
        if hits is FALSE:
            sum_of_polinoms.append(koeff2)    

    sum_of_polinoms.sort(key = lambda x: (-x[1], x[0]))
    return sum_of_polinoms


def polynomials(koeffs: list):      # преобразую список в новую формулу многочлена
    koeff = koeffs[0]
    formula_str = str(f'{koeff[0]}x^{len(koeffs)-1}+')  
    for i in range(1,len(koeffs)):
        koeff = koeffs[i]                               
        if koeff[1] == 1:
            formula_str += str(f'{koeff[0]}x+')
        elif koeff[1] == 0:
            formula_str += str(f'{koeff[0]}')
        else:                              
            formula_str += str(f'{koeff[0]}x^{len(koeffs)-1-i}+')
              

    formula_str += ' = 0'
    return formula_str   


print(formula_to_list(formula1))
print(formula_to_list(formula2))

sum = sum_of_polinoms(formula1, formula2)
print(sum)
print(polynomials(sum))

