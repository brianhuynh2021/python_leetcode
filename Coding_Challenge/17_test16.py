
def highest_chars(s: str)->str:
    char_list = list(s)
    char_list.sort(key= lambda x: x.lower(), reverse=True)
    
    highest_char = ''
    
    for i in range(len(char_list)-1):
        if char_list[i].lower() == char_list[i+1] and char_list[i] != char_list[i+1]:
            highest_char = char_list[i]
            break
    return highest_char

# Example usage
input_array = "DFbdAxa"
highest_char = highest_chars(input_array)
print("Highest character with both uppercase and lowercase letters:", highest_char)
