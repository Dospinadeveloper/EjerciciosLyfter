import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            developer = input("Escriba un desarrollador: ")
            found = False
            
            for row in reader:
                if row['desarrollador'].strip().lower()== developer.strip().lower():
                    name = row['nombre']
                    clasif = row['clasificacion']
                    gender = row['genero']
                
                    print(f"{name} (Clasificación: {clasif}, Género: {gender})")
                    found = True
                    
            if not found:
                print(f"No games found for the developer. {developer}")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")

read_csv_file('video_juegos.csv')