import pytest
from lc_80_number_range_optimized import optimized_number_range


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], []),
        ([5], ["5"]),
        ([1, 2, 3], ["1->3"]),
        ([1, 3, 5], ["1", "3", "5"]),
        ([0, 1, 2, 6, 7, 9], ["0->2", "6->7", "9"]),
        ([1, 2, 3, 7, 8], ["1->3", "7->8"]),
    ],
)
def test_optimized_number_range(arr, expected):
    assert optimized_number_range(arr) == expected
