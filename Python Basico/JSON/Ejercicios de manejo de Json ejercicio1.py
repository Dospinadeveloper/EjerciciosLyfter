import json

def load_pokemon_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_pokemon_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_pokemon_input():
    print("--- Enter the new Pokémon's details ---")
    name = input("Name (English): ")
    level = int(input("Level: "))
    types = input("Types (separated by comma, e.g., Grass, Poison): ").split(",")
    
    print("Base Stats:")
    return {
        "name": {"english": name},
        "level": level,
        "type": [t.strip() for t in types],
        "base": {
            "HP": int(input(" HP: ")),
            "Attack": int(input(" Attack: ")),
            "Defense": int(input(" Defense: ")),
            "Sp. Attack": int(input(" Sp. Attack: ")),
            "Sp. Defense": int(input(" Sp. Defense: ")),
            "Speed": int(input(" Speed: "))
        }
    }

def main():
    file_name = 'pokemon.json'
    
    pokemon_list = load_pokemon_data(file_name)

    new_pokemon = get_pokemon_input()

    pokemon_list.append(new_pokemon)
    save_pokemon_data(file_name, pokemon_list)
    
    print(f"\n{new_pokemon['name']['english']} has been added successfully!")

if __name__ == "__main__":
    main()
