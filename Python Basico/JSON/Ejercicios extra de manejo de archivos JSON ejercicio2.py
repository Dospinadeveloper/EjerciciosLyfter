import json
import sys
from pathlib import Path

def load_pokemon_data(file_name):
    script_directory = Path(__file__).parent
    full_path = script_directory / file_name
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at: {full_path}")
        sys.exit()
    except json.JSONDecodeError:
        print(f"Error: The file '{file_name}' has a JSON formatting error.")
        sys.exit()

def filter_pokemon_by_type(data, search_type):
    return [
        poke.get('name', {}).get('english', 'Unknown') 
        for poke in data 
        if search_type in poke.get('type', [])
    ]

def display_results(results, search_type):
    print(f"\n--- List of {search_type} type Pokémon ---")
    if not results:
        print(f"No results found for type '{search_type}'.")
    else:
        for name in results:
            print(f"- {name}")

def main():
    file_name = 'pokemon.json'
    data = load_pokemon_data(file_name)
    
    search_type = input("Enter the Pokémon type (e.g., Grass): ").capitalize().strip()
    
    results = filter_pokemon_by_type(data, search_type)
    display_results(results, search_type)

if __name__ == "__main__":
    main()
