def count_vowels(my_string):
    counter = 0
    
    for i in my_string:
        
        if i.lower() in "aeiouáéíóú":
            counter += 1
    return counter


my_string = "This code was made by Duberney OspinA rios"
result = count_vowels(my_string)
print(f"{result} vowels were found in the text")
