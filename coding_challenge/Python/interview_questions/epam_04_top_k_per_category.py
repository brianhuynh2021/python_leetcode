# Problem

# For each category, find the top K items by price.

# Input

items = [
    {"category": "A", "name": "i1", "price": 10},
    {"category": "A", "name": "i2", "price": 50},
    {"category": "B", "name": "i3", "price": 20},
    {"category": "A", "name": "i4", "price": 30},
]
K = 2

# Output

# {'A': [{'category': 'A', 'name': 'i2', 'price': 50}, {'category': 'A', 'name': 'i4', 'price': 30}], 'B': [{'category': 'B', 'name': 'i3', 'price': 20}]}


def top_k_per_category(items, k):
    result = {}
    cats = {item["category"] for item in items}
    for cat in cats:
        arr = [item for item in items if item["category"] == cat]
        arr.sort(key=lambda x: x["price"], reverse=True)
        result[cat] = arr[:k]
    return result


def topk_per_category_bruteforce(items, k=2):
    res = {}
    cats = {x["category"] for x in items}
    for cat in cats:
        arr = [x for x in items if x["category"] == cat]
        arr.sort(key=lambda x: x["price"], reverse=True)
        res[cat] = arr[:k]
    return res
