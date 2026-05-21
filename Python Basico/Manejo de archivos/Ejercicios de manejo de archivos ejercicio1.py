def get_songs(file_name):
    empty_list = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            
            for line in file:
                clean_song = line.strip()
                
                if clean_song != "":
                    empty_list.append(clean_song)
        return sorted(empty_list, key=str.lower)
        
    except FileNotFoundError:
        print("Error: El archivo no existe.")
        return []

def save_songs(new_Name, lista_ordenada):
    with open(new_Name, "w", encoding="utf-8") as file:
        for song in lista_ordenada:
            file.write(song + "\n")
    print("¡File saved successfully.!")

my_songs = get_songs("songs.txt")

if len(my_songs) > 0:
    save_songs("canciones_ordenadas.txt", my_songs)
else:
    print("The new file was not created in alphabetical order because the initial file is empty. ")
