def find_words(word_list, num): 
    list_2 = [] 
    for i in word_list: 
        if len(i) > int(num): 
            list_2.append(i) 
    return list_2 

original_list = input("Enter a list of words separated by spaces: ") 
word_list = original_list.split() 
num = input("Enter the minimum number of letters in the word: ") 

list_2 = find_words(word_list, num) 

print(f"This is the original list: {word_list}") 
print(f"This is the new list: {list_2}")
