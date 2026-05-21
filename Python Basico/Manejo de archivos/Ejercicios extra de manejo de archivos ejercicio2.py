def read_file_words(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read().split()
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    file_path = "hello_world.txt"
    content = read_file_words(file_path)
    
    if content is not None:
        print(f"The file has {len(content)} words.")
    else:
        print(f"Error: '{file_path}' was not found.")
