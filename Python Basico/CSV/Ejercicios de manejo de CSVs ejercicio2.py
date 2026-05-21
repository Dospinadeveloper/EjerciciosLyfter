import csv

def register_video_games():
    file_name = 'video_games.csv'
    headers = ['title', 'genre', 'developer', 'rating']
    
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers,delimiter='\t')
        writer.writeheader()
        
        while True:
            print("\n--- Enter Video Game Data ---")
            title = input("Title: ")
            genre = input("Genre: ")
            developer = input("Developer: ")
            rating = input("ESRB Rating: ")
            
            
            writer.writerow({
                'title': title,
                'genre': genre,
                'developer': developer,
                'rating': rating
            })
            
            continue_adding = input("\nDo you want to add another game? (y/n): ").lower()
            if continue_adding != 'y':
                break
                
    print(f"\nData saved successfully to {file_name}")

if __name__ == "__main__":
    register_video_games()
