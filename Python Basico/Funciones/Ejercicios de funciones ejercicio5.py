def count_letters(text):
    upper_case = 0
    lower_case = 0
    
    for character in text:
        if character.isupper():
            upper_case += 1
        elif character.islower():
            lower_case += 1
            
    print(f"There are {upper_case} upper case letters and {lower_case} lower case letters")


count_letters("I love Nación Sushi")
