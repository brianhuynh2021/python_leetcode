

def most_frequent_num(nums):
    if not nums:  # Check if the list is empty
        return None  # or raise ValueError("List is empty")

    frequent = {}
    for el in nums:
        if el not in frequent:
            frequent[el] = 1
        else:
            frequent[el] += 1

    # Find the element with the highest frequency
    max_count = 0
    majority_element = None
    for num, count in frequent.items():
        if count > max_count:
            max_count = count
            majority_element = num

    # Check if the found element is indeed a majority element
    if max_count > len(nums) // 2:
        return majority_element
    else:
        return None  # or any specific value indicating no majority was found

result = most_frequent_num([2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 5])
