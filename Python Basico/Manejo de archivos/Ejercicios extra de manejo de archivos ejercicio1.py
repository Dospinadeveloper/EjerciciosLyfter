def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def clean_text(text):
    return " ".join(text.split())

def write_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

def display_content(file_name):
    content = read_file(file_name)
    print(content)

def run_process():
    try:
        original_data = read_file("hello_world.txt")
        cleaned_text = clean_text(original_data)
        write_file("hello_world_2.txt", cleaned_text)
        display_content("hello_world_2.txt")
    
    except FileNotFoundError:
        print("Error: The file 'hello_world.txt' does not exist.")
    except IOError:
        print("Error: Could not read from or write to the disk.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_process()
