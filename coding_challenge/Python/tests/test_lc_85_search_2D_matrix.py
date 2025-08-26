from lc_85_search_2D_matrix_1st import optimized_search_matrix_binary
from unittest import TestCase

class TestSearch2DMatrix(TestCase):
    def test_found_target(self):
        self.assertTrue([[1,5, 7, 11], [13, 18, 24]], 18)