from epam_01_total_mount_per_cus import get_total_price_per_customer

# class TestTotalAmount(TestCase):
#     def test_happy_case(self):
#         orders = [
#             {"customer": "Alice", "amount": 120},
#             {"customer": "Bob", "amount": 90},
#             {"customer": "Alice", "amount": 50},
#         ]
#         self.assertEqual(get_total_price_optimize(orders), [('Alice', 170), ('Bob', 90)])


def test_total_amount_basic():
    orders = [
        {"customer": "Alice", "amount": 120},
        {"customer": "Bob", "amount": 90},
        {"customer": "Alice", "amount": 50},
    ]
    expected = [("Alice", 170), ("Bob", 90)]
    assert get_total_price_per_customer(orders) == expected
    print("Test successful")
