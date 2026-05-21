my_list = [10, 9, 1, 12, -10]

All_positive = True

for num in my_list:
    if num <= 0:
        All_positive = False
        break  

if All_positive:
    print("Los numeros de la lista son positivos")
else:
    print("Hay al menos un número negativo o cero")
