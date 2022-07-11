# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

list = [True, False]
for z in list:
    for y in list:
        for x in list:
            if not(x or y or z) == ((not x) and (not y) and (not z)):
                print('True')
            else:
                print ('False')
                