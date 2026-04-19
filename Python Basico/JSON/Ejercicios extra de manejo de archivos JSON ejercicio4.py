import json
import sys
from pathlib import Path

def load_data(data):
    carpeta_del_script = Path(__file__).parent
    ruta_completa = carpeta_del_script / data
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Loading error: {e}")
        sys.exit()

def calculate_averages_by_type(data):
    level_sums = {}
    pokemon_counts = {}

    for poke in data:
        # We assign 50 to the level in case it has no value.
        level = poke.get('level', 50 )
        
        for p_type in poke['type']:
            if p_type not in level_sums:
                level_sums[p_type] = 0
                pokemon_counts[p_type] = 0
            
            level_sums[p_type] += level
            pokemon_counts[p_type] += 1

    print("\n--- AVERAGES BY TYPE ---")
    for p_type in level_sums:
        total = level_sums[p_type]
        count = pokemon_counts[p_type]
        average = total / count
        print(f"Type: {p_type} | Average: {average:.1f}")

def main():
    data = load_data('pokemon.json')
    calculate_averages_by_type(data)

if __name__ == "__main__":
    main()
