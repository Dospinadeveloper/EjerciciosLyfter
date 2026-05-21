import csv

def genre_counter(file_path):
    genre_count = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                gender = row['genero'].strip().capitalize()
                
                if gender in genre_count:
                    genre_count[gender] += 1
                else:
                    genre_count[gender] = 1

        print("Géneros en Orden Alfabético")
        
        for gen in sorted(genre_count.keys()):
            print(f"- {gen}: {genre_count[gen]}")

    except FileNotFoundError:
        print("The file does not exist.")

genre_counter('video_juegos.csv')
