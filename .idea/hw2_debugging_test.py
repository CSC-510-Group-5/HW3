import pytest
from hw2_debugging import merge_sort

def test_merge_sort_gckoonts_1():
    assert merge_sort([8,6,7,5,3,0,9]) == [0,3,5,6,7,8,9]

def test_merge_sort_gckoonts_2():
    assert merge_sort([0,0,0,1,0]) == [0,0,0,0,1]

def test_merge_sort_gckoonts_3():
    assert merge_sort([32,11,15,27,38,1]) == [1,11,15,27,32,38]

if __name__ == "__main__":
    pytest.main()