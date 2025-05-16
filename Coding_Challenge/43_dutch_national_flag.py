"""The Dutch National Flag Problem is a classic algorithm problem introduced by Edsger Dijkstra. 
It’s designed to help us sort an array with three distinct types of elements. 
Let’s go step-by-step, like a teacher guiding a junior student.

Concept First:

Imagine you have an array of red, white, and blue balls, and you want to rearrange them so that:
	•	all red balls come first,
	•	then all white balls,
	•	and finally all blue balls.

This corresponds to sorting an array of 3 values, typically:
	•	0 → red
	•	1 → white
	•	2 → blue

For example:
Input:  [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
"""

def dutch_flag_sort(arr: list)-> list:
    distinc_arr = set(arr)
    if len(distinc_arr) != 3:
        raise ValueError('Dutch national flag sort only works for 3 categories')
    
    low = 0
    mid = 0
    high = len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            temp = arr[mid]
            arr[mid] = arr[low]
            arr[low] = temp
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else: # arr[mid] == 2
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high -= 1
    return arr           
        
            
if __name__== '__main__':
    arr = [2, 0, 2, 1, 1, 0,0, 1]
    print("Sorted:", dutch_flag_sort(arr))
    