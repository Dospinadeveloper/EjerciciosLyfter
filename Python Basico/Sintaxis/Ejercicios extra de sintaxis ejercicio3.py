counter = 1
counter_2 = 0


number = int(input("Escribe un numero: "))

while counter <= number:
    counter_2 = counter_2 + counter
    counter = counter + 1
print (f"{counter_2}")