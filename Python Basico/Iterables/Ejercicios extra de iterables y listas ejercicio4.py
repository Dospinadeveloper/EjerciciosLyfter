my_list = [10, 20, 30, 40, 50]

average = sum(my_list) / len(my_list)


new_list = [x for x in my_list if x > average]

print(f"Promedio: {average}")
print(f"Nueva lista: {new_list}")
