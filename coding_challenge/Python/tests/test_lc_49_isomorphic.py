from unittest import TestCase

from lc_49_isomorphic_strings_2nd import is_isomorphic_optimized


class TestIsomorphic(TestCase):
    def test_happy_case(self):
        s = "foo"
        t = "add"
        self.assertEqual(is_isomorphic_optimized(s, t), True)

    def test_unhappy_case(self):
        s = "foo"
        t = "bar"
        self.assertEqual(is_isomorphic_optimized(s, t), False)


def test_unhappy_case(s, t):
    s = "foo"
    t = "bar"
    assert is_isomorphic_optimized(s, t) == False


def test_happy_case(s, t):
    s = "foo"
    t = "add"
    assert is_isomorphic_optimized(s, t) == True
