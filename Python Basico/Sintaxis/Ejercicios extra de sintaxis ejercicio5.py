numbers = 3
number = 0
number_1 = 0
number_2 = 0
number_3 = 0
counter = 1
sum = 0


while counter <= numbers:
    number = int(input(f"Escribe el numero {counter}: "))
    
    if counter == 1:
        number_1 = number
    elif counter == 2:
        number_2 = number
    else:
        number_3 = number
    
    
    counter = counter + 1
sum = (number_1 + number_2 + number_3)


if number_1 == 30 or number_2 == 30 or number_3 == 30 or sum == 30:
    print ("Correcto")
else:
    print ("Incorrecto")