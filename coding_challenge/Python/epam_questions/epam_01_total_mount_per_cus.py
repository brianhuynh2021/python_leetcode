"""
Example:
Input: list of orders (dicts),
output: total price per customer sorted by total desc.
"""

orders = [
    {"customer": "Alice", "amount": 120},
    {"customer": "Bob", "amount": 90},
    {"customer": "Alice", "amount": 50},
]


def get_total_price_per_customer(orders: list) -> list:
    total = {}

    for order in orders:
        customer = order["customer"]
        amount = order["amount"]
        total[customer] = (
            total.get(customer, 0) + amount
        )  # Now total is list of dictionay

    result = list(total.items())
    result.sort(key=lambda x: x[1], reverse=True)
    return result


print(get_total_price_per_customer(orders))

from collections import defaultdict


def get_total_price_optimize(orders):
    total = defaultdict(int)
    for o in orders:
        total[o["customer"]] += o["amount"]
    return sorted(total.items(), key=lambda x: x[1], reverse=True)
