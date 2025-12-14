from typing import List


def merge_two_sorted_arrays_brute_force(nums1: List[int],m: int, nums2: List[int], n: int)-> None:
    """
    Merge two sorted arrays in-place into nums1.

    nums1 has length m + n, where the first m elements are valid sorted values
    and the last n elements are placeholders (extra capacity). nums2 has length n
    and contains n valid sorted values. After this function returns, nums1 will
    contain the merged sorted sequence of all m + n elements.
    """
    p1 = 0
    p2 = 0
    tmp: List[int] = []
    while p1 < m and p2 < n:
        if nums1[p1] <= nums2[p2]:
            tmp.append(nums1[p1])
        else:
            tmp.append(nums2[p2])
            
    while p1 < m:
        tmp.append(nums1[p1])
        p1 += 1
    
    while p2 < n:
        tmp.append(nums2[p2])
        p2 += 1
    
    for idx in range(m + n):
        nums1[idx] = tmp[idx]
    
def merge_two_sorted_arrs_brute_force(nums1: List[int], m: int, nums2: List[int], n: int)-> None:
    for idx in range(n):
        nums1[m + idx] = nums2[idx]
    nums1.sort()

def merge_two_sorted_arrs_optimzed(nums1: List[int], m: int, nums2: List[int], n: int)-> None:
    i = m - 1
    j = n - 1
    k = m + n - 1
    
    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            i -= 1
        else:
            nums1[k] = nums1[i]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
            
        