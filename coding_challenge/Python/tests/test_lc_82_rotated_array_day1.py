import pytest
from lc_82_rotated_array_day1 import optimized_rotated_arr


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([4,5,6,7,0,1,2], 0, True),
        ([4,5,6,7,0,1,2], 3, False),
        ([1], 0, False),
        ([1], 1, True),
        ([3,1], 3, True),
        ([3,1], 1, True),
        ([1,3], 1, True),
        ([1,3], 2, False),
])

def test_optimized_rotated_arr(nums, k, expected):
    assert optimized_rotated_arr(nums, k) == expected
    
