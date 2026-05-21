import csv
import os

FILENAME = "students_data.csv"

def export_to_csv(students):
    if not students:
        print("Nothing to export.")
        return
    try:
        with open(FILENAME, mode='w', newline='') as file:
            fieldnames = ['Name', 'Section', 'Spanish', 'English', 'Social Studies', 'Science', 'Average']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for s in students:
                row = {
                    'Name': s['name'],
                    'Section': s['section'],
                    **s['grades'],
                    'Average': s['average']
                }
                writer.writerow(row)
        print(f"Data successfully exported to {FILENAME}")
    except Exception as e:
        print(f"Error exporting data: {e}")

def import_from_csv():
    if not os.path.exists(FILENAME):
        print(f"Error: The file '{FILENAME}' does not exist.")
        return []
    
    students = []
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    "name": row['Name'],
                    "section": row['Section'],
                    "Grades": {
                        "Spanish": float(row['Spanish']),
                        "English": float(row['English']),
                        "Social Studies": float(row['Social Studies']),
                        "Science": float(row['Science'])
                    },
                    "average": float(row['Average'])
                }
                students.append(student)
        print("Data imported successfully.")
        return students
    except Exception as e:
        print(f"Error importing data: {e}")
        return []
