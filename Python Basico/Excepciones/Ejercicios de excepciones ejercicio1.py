def calculator():
    current_number = 0.0
    while True:
        print(f"\n--- Current result: {current_number} ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Clear result (Reset)")
        print("6. Exit")
        
        option = input("Select an option: ")
        
        if option == '6':
            print("Goodbye!")
            break
            
        if option == '5':
            current_number = 0.0
            print("Result cleared.")
            continue
        
        if option > '6' or option < '1':
            current_number = 0.0
            print("Error: Invalid option.")
            continue
            
        if option in ['1', '2', '3', '4']:
            try:
                new_number = float(input("Enter number: "))
                if option == '1':
                    current_number += new_number
                elif option == '2':
                    current_number -= new_number
                elif option == '3':
                    current_number *= new_number
                elif option == '4':
                    if new_number == 0:
                        print("Error: Cannot divide by zero.")
                    else:
                        current_number /= new_number
            except ValueError:
                print("Error: Please enter a valid number.")
        else:
            print("Error: Invalid option.")

calculator()
