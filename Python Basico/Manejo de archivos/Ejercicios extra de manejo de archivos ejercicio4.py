def save_lines(file_name, text):
    try:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(f"{text}")
        print("Linea guardada exitosamente ")

    except PermissionError:
        print("Error: El archivo está bloqueado por otro programa o no tienes permisos.")
    except Exception as e:
        print(f" Ocurrió un error inesperado: {e}")

if __name__ == '__main__':
    text = input("ingrese una linea de texto: ")
    save_lines("hello_world2.txt", text)