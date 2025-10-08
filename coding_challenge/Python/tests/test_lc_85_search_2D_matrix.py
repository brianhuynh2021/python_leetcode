from unittest import TestCase


class TestSearch2DMatrix(TestCase):
    def test_found_target(self):
        self.assertTrue([[1, 5, 7, 11], [13, 18, 24]], 18)
