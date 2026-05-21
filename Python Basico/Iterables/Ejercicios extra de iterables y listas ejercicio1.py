counter = 0
numbers = input("Introduce una lista de números separados por coma: ")
my_list = numbers.split(",")

search = input("¿Qué número quieres buscar? ")

for i in my_list:
    if i == search:
        counter = counter + 1
    

print(f"El número {search} aparece {counter} veces")
