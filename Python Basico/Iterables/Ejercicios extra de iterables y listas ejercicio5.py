new_list = []


for i in range(5):
    word = input(f"Ingrese la palabra No. {i+1} ")
    if len (word) > 4:
        new_list.append(word)

print(new_list)
