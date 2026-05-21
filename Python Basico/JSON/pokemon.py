import json
import sys

def cargar_datos(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar: {e}")
        sys.exit()

def calcular_promedios_por_tipo(datos):
    suma_niveles = {}     
    conteo_pokemon = {}   

    for poke in datos:
        
        nivel = poke.get('level', sum(poke['base'].values()) / len(poke['base']))

        for tipo in poke['type']:
            
            if tipo not in suma_niveles:
                suma_niveles[tipo] = 0
                conteo_pokemon[tipo] = 0
        
            suma_niveles[tipo] += nivel
            conteo_pokemon[tipo] += 1

    print("\n--- PROMEDIOS POR TIPO ---")
    
    for tipo in suma_niveles:
        total = suma_niveles[tipo]
        cantidad = conteo_pokemon[tipo]
        promedio = total / cantidad
        
        print(f"Tipo: {tipo} | Promedio: {promedio:.1f}")

def main():
    datos = cargar_datos('pokemon.json')
    calcular_promedios_por_tipo(datos)

if __name__ == "__main__":
    main()
