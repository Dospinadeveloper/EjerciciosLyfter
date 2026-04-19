def convert_to_integer(my_list):
    print("-------------Result-------------")
    for i in my_list:
        try:
            element = int(i)
            print(f" '{i}' converted to {element}")
        except ValueError:
            print(f"Could not convert the element '{i}'")

my_list = ['4', 'hello', '10', '5.2']
convert_to_integer(my_list)
