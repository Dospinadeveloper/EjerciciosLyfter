def sum_values(my_list):
    total_sum = 0.0
    for value in my_list:
        try:
            new_value = float(value)
            total_sum += new_value
            print(f"'{value} Converted to {new_value}")
        except (ValueError):
            print(f"Invalid element: {value}")
    
    print(f"Total sum: {total_sum}")

my_list = ['10', 'apple', '5.5', '3', 'n/a']
sum_values(my_list)
