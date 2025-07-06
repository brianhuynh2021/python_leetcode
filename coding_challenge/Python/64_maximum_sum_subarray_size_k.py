def max_sum_subarray_sliding(arr, k):
    n = len(arr)
    if n < k:
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, n):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
        
    return max_sum
        