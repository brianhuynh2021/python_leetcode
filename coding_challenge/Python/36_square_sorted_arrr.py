'''
Take a sorted array of integers (may include negative numbers), 
square each number, and return a new array of the squares, 
also sorted in non-decreasing order.

Cho mảng các phần tủ số nguyên (có thể số âm), bình phương các phần tử.
Sau đó trả về các phần tử tăng dần trong mảng đó

Input:  [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]

sau_khi_binh_phuong_arr = [16, 1, 0, 9, 100]
'''

def square_array(arr: list)-> list:
    new_arr = [x*x for x in arr]
    print("Mang sau khi binh phuong la", new_arr)
    return new_arr

# Use insertion sort
def sorted_array(arr: list)-> list:
    for i in range(1, len(arr)):
        compare_element = arr[i]
        j = i
        while j > 0 and compare_element < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        compare_element = arr[j]
    return arr

if __name__=='__main__':
    arr = [-4, -1, 0, 3, 10]
    new_arr = square_array(arr)
    print("Squaring sorted array is: ", sorted_array(new_arr))