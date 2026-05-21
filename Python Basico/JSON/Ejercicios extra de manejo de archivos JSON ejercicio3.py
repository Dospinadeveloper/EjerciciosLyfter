import json
import sys
from pathlib import Path

def load_pokemon_data(file_name):
    script_folder = Path(__file__).parent
    full_path = script_folder / file_name
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: El archivo '{full_path}' no existe o está dañado.")
        sys.exit()

def calculate_averages_by_type(data):
    type_stats = {}
    for poke in data:
        base_total = sum(poke['base'].values())
        
        for p_type in poke['type']:
            if p_type not in type_stats:
                type_stats[p_type] = {'total_sum': 0, 'count': 0}
            
            type_stats[p_type]['total_sum'] += base_total
            type_stats[p_type]['count'] += 1
            
    averages = {t: stats['total_sum'] / stats['count'] for t, stats in type_stats.items()}
    return averages

def display_averages(averages):
    print(f"\n{'Tipo':<15} | {'Promedio BST':<15}")
    print("-" * 35)
    
    sorted_averages = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    
    for p_type, avg in sorted_averages:
        print(f"{p_type:<15} | {avg:>15.2f}")

def main():
    file_name = 'pokemon.json'
    
    data = load_pokemon_data(file_name)
    averages = calculate_averages_by_type(data)
    display_averages(averages)

if __name__ == "__main__":
    main()
