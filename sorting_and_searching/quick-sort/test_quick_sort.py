import pytest
import quick_sort


test_cases = [
    ([]),
    ([1]),
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
]

@pytest.mark.parametrize("arr", test_cases)
def test_quick_sort_lomuto(arr):
    work = arr.copy()  # Don't modify the test cases.
    copy = arr.copy()
    copy.sort()
    quick_sort.quick_sort_lomuto(work)
    assert work == copy, f'{work} != {copy}'

@pytest.mark.parametrize("arr", test_cases)
def test_quick_sort_hoare(arr):
    work = arr.copy()  # Don't modify the test cases.
    copy = arr.copy()
    copy.sort()
    quick_sort.quick_sort_hoare(work)
    assert work == copy, f'{work} != {copy}'
