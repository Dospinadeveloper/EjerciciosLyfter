while True:
    try:
        name = input("Enter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        
        if name.isdigit():
            raise ValueError("The name cannot be a number.")

        while True:
            try:
                age_text = int(input("Enter your age: ").strip())
                print(f"Hello {name}, your age is {age_text} years.")
                break
            except:
                print("Invalid number.")
                
        break        
    except ValueError as e:
        print(f"Notice: {e}")

