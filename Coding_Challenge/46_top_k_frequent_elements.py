'''
🧠 What is the “Top K Frequent Elements” Problem?

You are given:
	•	A list of numbers nums
	•	A number k

Goal:
Return the k most frequent elements in the list.
nums = [1, 1, 1, 2, 2, 3]
k = 2

👉 Step-by-step explanation:
	1.	Count how many times each number appears:
	•	1 appears 3 times
	•	2 appears 2 times
	•	3 appears 1 time
	2.	We want the top 2 most frequent elements → so pick the two with highest frequency:
	•	✅ 1 and 2 → because they have the two highest counts

➡️ Expected output: [1, 2]
(The order doesn’t matter — it can be [2, 1] too.)

🤔 Why is this problem important?

This is a common pattern in interviews. It tests:
	•	Your ability to use hash maps (dictionaries)
	•	Your understanding of sorting or heaps
	•	Your skill in optimizing for performance (not just brute force)
'''

# Traditional method:
def sort_result(items):
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    return sorted_items
    
def top_k_frequent_elements(nums: list, k: int)-> list:
    result = []
    check_appear = {}
    for num in nums:
        if num not in check_appear:
            check_appear[num] = 1
        else:
            check_appear[num] += 1
    sorted_item = sort_result(check_appear.items())
    result = [item[0] for item in sorted_item[:k]]
    return result

# Optimize method:
def top_k_frequent_elements_optimize(nums, k):
    import heapq
    result = []
    check_appear = {}
    heap = []
    for num in nums:
        check_appear[num] = check_appear.get(num, 0) + 1
    # using heap to check each item of dictonary and push only k items in heap
    for num, freq in check_appear.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    result = [num for freq, num in heap]
    return result

if __name__=='__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    nums_1 = [1, 1, 1, 2, 2, 3, 3, 7, 7, 9, 4, 5,6]
    k_1 = 3
    result = top_k_frequent_elements(nums, k)
    result_1 = top_k_frequent_elements_optimize(nums_1, k_1)
    print(f'Top {k} frequent elements: {result}')
    print(f'Top {k_1} frequent elements: {result_1}')
    