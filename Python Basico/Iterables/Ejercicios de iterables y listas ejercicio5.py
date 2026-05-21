numbers = []

for i in range(10):
    num = float(input(f"Ingresa el número {i+1}: "))
    numbers.append(num)

print(f"\n{numbers}. El más alto fue: {max(numbers)}")
