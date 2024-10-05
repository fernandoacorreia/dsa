from merge_sort import merge_sort
import pytest

@pytest.mark.parametrize("arr", [
    [],
    [1],
    [1, 2],
    [2, 1],
    ([1, 1, 1]),
    ([2, 3, 1]),
    ([7, 6, 5, 4]),
    ([9, -1, 7, 0, 2]),
    ([1, 1, 1, 2, 2, 2]),
    ([2, 1, 2, 1, 2, 1]),
    ([1, 2, 3, 4, 5, 6]),
    ([1, 2, 3, 4, 5, 6, 7]),
    ([6, 5, 4, 3, 2, 1]),
    ([7, 6, 5, 4, 3, 2, 1]),
    ([10, 66, 88, 18, 85, 54, 8, 30, 98, 79, 95, 72]),
    ([29, 63, 50, 76, 33, 84, 67, 68, 23, 10, 47, 45]),
    ([18, 78, 58, 75, 97, 41, 96, 91, 93, 55, 32, 33]),

])
def test_merge_sort(arr):
    input = arr.copy()
    expected = arr.copy()
    expected.sort()
    result = merge_sort(input)
    assert result == expected
