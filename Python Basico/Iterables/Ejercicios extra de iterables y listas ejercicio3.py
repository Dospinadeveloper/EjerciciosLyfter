my_list = [9, 4, 7, 1, 5]

minNumber = my_list[0]

for number in my_list:
    if number < minNumber:
        minNumber = number

print(f"El menor valor es {minNumber}")
