def sort_words(text):
    
    word_list = text.split("-")
    
    word_list.sort()
    
    result = "-".join(word_list)
    
    return result

input_string = "python-variable-function-computer-monitor"
print(sort_words(input_string))
