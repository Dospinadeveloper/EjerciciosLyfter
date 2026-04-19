import json
import sys
from pathlib import Path

def load_pokemon_data(file_name):
    Script_Folder = Path(__file__).parent
    Full_Path = Script_Folder / file_name
    
        
    try:
        with open(Full_Path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: The file '{Full_Path}' does not exist.")
        sys.exit()

def show_statistics(data):
    for poke in data:
        name_only = poke['name']['english']
        print(f"\nName: {name_only}")
        
        for stat, value in poke['base'].items():
            print(f"{stat}: {value}")

def main():
    file_name = 'pokemon.json'
    data = load_pokemon_data(file_name)
    show_statistics(data)

if __name__ == "__main__":
    main()
