import unittest

from lc_88_temperature_daily_1st import daily_temperatures_brute


class TestDailyTemperature(unittest.TestCase):
    def test_has_daily_warmer_temperatures(self):
        self.assertEqual(
            daily_temperatures_brute([74, 70, 77, 69, 75]), [2, 1, 0, 1, 0]
        )

    def test_no_daily_warmer_temperature(self):
        self.assertEqual(daily_temperatures_brute([100, 90, 95]), [0, 1, 0])

    def test_mixed_temperatures(self):
        self.assertEqual(
            daily_temperatures_brute([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0],
        )

    def test_flat_temperatures(self):
        # All days same temp → no warmer days
        self.assertEqual(daily_temperatures_brute([70, 70, 70, 70]), [0, 0, 0, 0])

    def test_single_element(self):
        with self.assertRaises(ValueError):
            daily_temperatures_brute([70])

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            daily_temperatures_brute([])

    def test_same_then_one_hot(self):
        self.assertEqual(daily_temperatures_brute([55, 55, 53, 60]), [3, 2, 1, 0])

    def test_warmer_day_far(self):
        self.assertEqual(
            daily_temperatures_brute([60, 50, 45, 40, 70]), [4, 3, 2, 1, 0]
        )


if __name__ == "__main__":
    unittest.main()
