#Secret_number = 4
import random
Secret_number = random.randint(1, 10) # Número entero entre 1 y 10

number = int(input("Digite un numero del 1 al 10:  " ))

while number != Secret_number:
    number = int(input(f"{number}, no es el numero secreto.  Escribe otro numero entre  1 y 10: " ))
print ("Lo hiciste")