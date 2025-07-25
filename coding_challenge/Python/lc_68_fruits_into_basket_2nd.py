'''
🍌 Problem Statement (Simplified):
You are given an array fruits where each element represents a 
type of fruit. You have two baskets, and you can only pick one 
type of fruit per basket. You need to find the length of the longest 
subarray with at most 2 distinct fruits.
'''

def fruit_into_basket_brute(fruits: list[int])->int:
    if not fruits:
        raise ValueError('fruits must be not empty')
    n = len(fruits)
    max_len = 0
    for i in range (n):
        for j in range(i,n):
            sub_fruits = fruits[i:j+1]
            num_types = len(set(sub_fruits))
            if num_types <= 2:
                max_len = max(max_len, len(sub_fruits))
                
    return max_len

print(fruit_into_basket_brute([1, 2, 1, 2, 3]))