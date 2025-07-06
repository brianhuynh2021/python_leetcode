'''
The “Next Letter” problem you’re referring to is discussed in the context of 
bit manipulation, titled “Next Number” in Cracking the Coding Interview, 
problem 5.4. 

⸻

❓ Problem Summary (bit manipulation context)

Given a positive integer, print:
	•	The next smallest
	•	The next largest

numbers with the same number of 1 bits in their binary representation.
'''
# This normal method
def convert_to_binary(number: int):
    result = ''
    while number > 0:
        result += '1' if number%2 == 1 else '0'
        number //=2
    return result[::-1] if result else '0'

# Recursive method
def recursive_convert_dec_to_bin(number: int):
    if number == 0:
        return ''
    return recursive_convert_dec_to_bin(number//2) + str(number%2)

def count_ones(number: int)-> int:
    count = 0
    while number > 0:
        if number % 2 == 1:
            count += 1
        number //=2
    return count
    
if __name__=='__main__':
    number = 25
    result = recursive_convert_dec_to_bin(number)
    print(result)
     