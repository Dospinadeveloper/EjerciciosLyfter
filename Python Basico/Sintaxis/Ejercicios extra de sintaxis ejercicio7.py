result = 0
number = 0

number = int(input("Introduce un número del 1 al 10: "))


if number <= 10:

    print(f"Tabla de multiplicar del {number}:")

    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")
else:
    print("El número es mayor a 10.  Digita un numero entre 1 y 10.")
