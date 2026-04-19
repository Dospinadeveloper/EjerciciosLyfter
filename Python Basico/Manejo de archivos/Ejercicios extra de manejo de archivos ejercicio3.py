import sys
def get_lines(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no existe.")
        sys.exit()

def transform_to_uppercase(lines_list):
    new_lines = []
    for line in lines_list:
        new_lines.append(line.upper())
    return new_lines

def save_lines(file_name, lines_list):
    with open(file_name, "w", encoding="utf-8") as file:
        file.writelines(lines_list)


if __name__=="__main__":
    original_lines = get_lines("hello_world.txt")
    modified_lines = transform_to_uppercase(original_lines)
    save_lines("hello_world2.txt", modified_lines)
    print("File processed line by line")
