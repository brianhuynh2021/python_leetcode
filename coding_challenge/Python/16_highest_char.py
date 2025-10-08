def highest_char_with_both_cases(s):
    # Step 1: Convert the string to a list of characters
    char_list = list(s)

    # Step 2: Sort the list of characters ignoring case
    char_list.sort(key=lambda x: x.lower(), reverse=True)

    # Step 3: Initialize a variable to store the highest character
    highest_char = ""

    # Step 4: Iterate through the sorted list to find the highest character with both cases
    for i in range(len(char_list) - 1):
        # Step 5: Check if the current character and the next character have both cases
        if (
            char_list[i].lower() == char_list[i + 1].lower()
            and char_list[i] != char_list[i + 1]
        ):
            highest_char = char_list[i]
            break  # Once found, break the loop
    # Step 6: Return the highest character found
    return highest_char


# Example usage
input_array = "DFbdAxa"
highest_char = highest_char_with_both_cases(input_array)
print("Highest character with both uppercase and lowercase letters:", highest_char)
