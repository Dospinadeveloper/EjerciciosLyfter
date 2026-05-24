import re

def is_valid_name(name):
    return bool(name.strip()) and all(x.isalpha() or x.isspace() for x in name)

def is_valid_section(section):
    return bool(re.match(r"^\d{1,2}[A-Z]$", section))

def student_exists(name, section, students):
    return any(s['name'] == name and s['section'] == section for s in students)

def get_valid_grade(subject_name):
    while True:
        try:
            grade = float(input(f"Enter {subject_name} grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_students(students):
    while True:
        name = input("Full Name: ")
        if not is_valid_name(name):
            print("Invalid name. Use letters only.")
            continue
            
        while True:
            section = input("Section (e.g., 11B): ").upper().strip()
            if is_valid_section(section):
                break  # Sale del bucle de sección porque el formato es correcto
            else:
                print("Invalid section format. Please try again (e.g., 10A, 11B).")

        if student_exists(name, section, students):
            print("Student already exists in this section.")
            continue

        spanish = get_valid_grade("Spanish")
        english = get_valid_grade("English")
        social_studies = get_valid_grade("Social Studies")
        science = get_valid_grade("Science")

        student = {
            "name": name,
            "section": section,
            "grades": {
                "Spanish": spanish,
                "English": english,
                "Social Studies": social_studies,
                "Science": science
            },
            "average": (spanish + english + social_studies + science) / 4
            
            
        }
        students.append(student)
        
        if input("Add another? (y/n): ").lower() != 'y':
            break

def view_all_students(students):
    if not students:
        print("No students registered.")
        return
    for s in students:
        #print(f"Name: {s['name']} | Section: {s['section']} | Avg: {s['average']:.2f}")
        print(f"Name: {s['name']} | Section: {s['section']} | Spanish: {s['grades']['Spanish']} | English: {s['grades']['English']} | Social Studies: {s['grades']['Social Studies']} | Science: {s['grades']['Science']} | Avg: {s['average']:.2f}")
        #print(f"Name: {s['name']} | Section: {s['section']} | Spanish: {s['grades']['Spanish']} | Avg: {s['average']:.2f}")

def view_top_three(students):
    top = sorted(students, key=lambda x: x['average'], reverse=True)[:3]
    print("\n--- Top 3 Students ---")
    view_all_students(top)

def view_overall_average(students):
    if not students:
        print("No data available.")
        return
    total_avg = sum(s['average'] for s in students) / len(students)
    print(f"The overall class average is: {total_avg:.2f}")

def remove_student(students):
    name = input("Name to remove: ")
    section = input("Section: ").upper()
    for i, s in enumerate(students):
        if s['name'] == name and s['section'] == section:
            confirm = input(f"Are you sure you want to delete {name}? (y/n): ")
            if confirm.lower() == 'y':
                students.pop(i)
                print("Student removed.")
                return
            else:
                print("Operation cancelled by the user.")
                return
    print("Student not found. Please verify the entered information.")

def view_failing_students(students):
    print("\n--- Failing Students (Grade < 60) ---")
    found = False
    for s in students:
        failing_subjects = {k: v for k, v in s['grades'].items() if v < 60}
        if failing_subjects:
            found = True
            subjects_str = ", ".join([f"{k}: {v}" for k, v in failing_subjects.items()])
            print(f"{s['name']} ({s['section']}) -> {subjects_str}")
    if not found:
        print("No failing students found.")
