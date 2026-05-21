
number_id = 1
number_1 = 0
number_2 = 0
number_3 = 0
Largest_number = 0


while number_id <= 3:
    number = int(input("Escribe los numeros a comparar: "))
    if number_id == 1:
        number_1 = number
    elif number_id == 2:
        number_2 = number
    else:
        number_3 = number
    number_id = number_id + 1


largest_number = max(number_1, number_2, number_3)

print(f"El número mayor es: {largest_number}")