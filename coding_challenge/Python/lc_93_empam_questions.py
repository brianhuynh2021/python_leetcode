'''
Example:
Input: list of orders (dicts), 
output: total price per customer sorted by total desc.
'''
orders = [
    {"customer": "Alice", "amount": 120},
    {"customer": "Bob", "amount": 90},
    {"customer": "Alice", "amount": 50}
]

orders = [
    {"customer": "Alice", "amount": 120},
    {"customer": "Bob", "amount": 90},
    {"customer": "Alice", "amount": 50}
]

# Step 1: Group and sum amounts per customer
totals = {}
for order in orders:
    customer = order["customer"]
    amount = order["amount"]
    totals[customer] = totals.get(customer, 0) + amount

# Step 2: Convert dict to list of tuples
result = list(totals.items())

# Step 3: Sort by total amount desc
result.sort(key=lambda x: x[1], reverse=True)

print(result)  
# [('Alice', 170), ('Bob', 90)]