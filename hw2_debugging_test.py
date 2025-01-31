import pytest
from hw2_debugging import merge_sort

def test_merge_sort_reverse():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_merge_sort_sorted():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort_unsorted():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    
def cablumsa_test1():
    arr1 = [1, 2, 3, 4, 5]
    assert merge_sort(arr1) == [1, 2, 3, 4, 5]

def cablumsa_test2():
    arr2 = [5, 3, 4]
    assert merge_sort(arr2) == [3,4,5]

def cablumsa_test3():
    arr3 = [2]
    assert merge_sort(arr3) == [2]
    
def test_merge_sort_gckoonts_1():
    assert merge_sort([8,6,7,5,3,0,9]) == [0,3,5,6,7,8,9]

def test_merge_sort_gckoonts_2():
    assert merge_sort([0,0,0,1,0]) == [0,0,0,0,1]

def test_merge_sort_gckoonts_3():
    assert merge_sort([32,11,15,27,38,1]) == [1,11,15,27,32,38]

if __name__ == "__main__":
    pytest.main()
