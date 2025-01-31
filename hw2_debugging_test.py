from hw2_debugging import merge_sort

def cablumsa_test1():
    arr1 = [1, 2, 3, 4, 5]
    assert merge_sort(arr1) == [1, 2, 3, 4, 5]

def cablumsa_test2():
    arr2 = [5, 3, 4]
    assert merge_sort(arr2) == [3,4,5]

def cablumsa_test3():
    arr3 = [2]
    assert merge_sort(arr3) == [2]