import json
import sys
from pathlib import Path

def load_pokemon_data(file_name):
    carpeta_del_script = Path(__file__).parent
    ruta_completa = carpeta_del_script / file_name
    
        
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: The file '{ruta_completa}' does not exist.")
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
