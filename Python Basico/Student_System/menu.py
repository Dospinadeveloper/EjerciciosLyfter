import actions
import data

def show_main_menu(students):
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Students")
        print("2. View All Students")
        print("3. View Top 3 Students")
        print("4. View Average of All Students")
        print("5. Export to CSV")
        print("6. Import from CSV")
        print("7. Remove Student")
        print("8. View Failing Students")
        print("9. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            actions.add_students(students)
        elif choice == "2":
            actions.view_all_students(students)
        elif choice == "3":
            actions.view_top_three(students)
        elif choice == "4":
            actions.view_overall_average(students)
        elif choice == "5":
            data.export_to_csv(students)
        elif choice == "6":
            imported_data = data.import_from_csv()
            if imported_data:
                students.extend(imported_data)
        elif choice == "7":
            actions.remove_student(students)
        elif choice == "8":
            actions.view_failing_students(students)
        elif choice == "9":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
