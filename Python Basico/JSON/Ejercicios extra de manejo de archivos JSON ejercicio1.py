import json
import sys

def load_pokemon_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit()

def show_pokemon_list(pokemon_list):
    if not pokemon_list:
        print("The list is empty.")
        return

    print("\n===================== POKÉMON LIST =====================")
    
    for poke in pokemon_list:
        
        name = poke["name"]["english"]
        level = poke["level"]
        
        types = " / ".join(poke["type"])
        hp = poke["base"]["HP"]
        
        print(f"NAME: {name} | Level: {level} | Type: {types} | HP: {hp}")

def main():
    file_name = r'D:\LYFTER\EjerciciosLyfter\JSON\pokemon.json'
    data = load_pokemon_data(file_name)
    show_pokemon_list(data)


if __name__ == "__main__":
    main()
