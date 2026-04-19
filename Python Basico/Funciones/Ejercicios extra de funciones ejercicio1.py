def count_character(text, character):
    count = 0
    character = character.lower()
    for i in text:
        if i.lower()== character:
            count += 1
    return count


user_text = input("Enter the text: ")
search_char = input("Enter the character you want to find: ")


result = count_character(user_text, search_char)

print(f"The character '{search_char}' was found {result} times.")
