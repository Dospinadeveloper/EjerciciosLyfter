import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            
            ESRB = input("Escriba la ESRB que desea visualizar: ").strip().lower()
            
            for row in reader:
                if row['clasificacion'].strip().lower()== ESRB:
                    print('-----')
                    for key, value in row.items():
                        print(f"{key}: {value}")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")

read_csv_file('video_juegos.csv')