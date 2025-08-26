'''
Problem

Given ratings with product and rating, compute average rating per product. Sort by average desc then product asc.
ratings = [
    {"product": "A", "rating": 5},
    {"product": "A", "rating": 3},
    {"product": "B", "rating": 4},
]
output:
[('A', 4.0), ('B', 4.0)]
'''

def averate_rating(ratings: list):
    products = {}
    count = {}
    for r in ratings:
        product = r["product"]
        rating = r["rating"]
        products[product] = products.get(product, 0) + rating
        count[product] = count.get(product, 0) + 1
    result = []
    for p in products:
        avg = products[p]/count[p]
        result.append((p, avg))
    sorted(result, key=lambda x: (-x[1], x[0]), reverse=True)
    