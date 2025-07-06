def solution(S):
    # Implement your solution here
    n = len(S) # get the length of s
    char_list = list(S)

    # Iterate only through a half characters of string
    
    for i in range(n//2):
        opposite_char = n - i - 1
        if char_list[i] == '?' and char_list[opposite_char] == '?':
            char_list[i] = char_list[opposite_char] = 'a'
        elif char_list[i] != char_list[opposite_char]:
            return "No"
        elif char_list[i] == '?':
            char_list[i] = char_list[opposite_char]
        elif char_list[opposite_char] == '?':
            char_list[opposite_char] = char_list[i]
        
    if n%2 != 0 and char_list[n//2] == '?':
        char_list[n//2] = 'a'
  
    return ''.join(char_list)

print(solution('?ab??a'))