import random
number = random.randint(1, 10) # Número entero entre 1 y 10

user_number = int(input("Escribe un número entero del 1 al 10: "))

while user_number != number:
    user_number = int(input("Fallaste, escribe otro número entero del 1 al 10: "))

print(f"Lo conseguiste el numero secreo es: {number}")
