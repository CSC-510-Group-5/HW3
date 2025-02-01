"""This module provides implementations of different sorting algorithms."""
import rand

def selection_sort(input_array):
    """
    Sorts an array in ascending order using the selection sort algorithm.
    Parameters:
    arr (list): The list of elements to be sorted.
    Returns:
    list: The sorted list in ascending order.
    """
    for i, _ in enumerate(input_array):
        min_idx = i
        for j in range(i + 1, len(input_array)):
            if input_array[j] < input_array[min_idx]:
                min_idx = j
        input_array[i], input_array[min_idx] = input_array[min_idx], input_array[i]
    return input_array

def bubble_sort(input_array):
    """
    Sorts an array of elements using the bubble sort algorithm.
    Args:
        arr (list): A list of elements to be sorted.
    Returns:
        list: The sorted list of elements.
    """
    n = len(input_array)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if input_array[j] > input_array[j + 1]:
                # Swap if the element found is greater than the next element
                input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]
                swapped = True
                #this line is an issue

        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break

    return input_array

def insertion_sort(input_array):
    """
    Sorts an array of elements using the insertion sort algorithm.
    Parameters:
    arr (list): A list of elements to be sorted.
    Returns:
    list: The sorted list of elements.
    """
    for i in range(1, len(input_array)):
        key = input_array[i]
        j = i - 1
        while j >= 0 and input_array[j] > key:
            input_array[j+1] = input_array[j]
            j -= 1
        input_array[j+1] = key
    return input_array

def merge_sort(input_array):
    """
    Sorts an array in ascending order using the merge sort algorithm.
    Parameters:
    arr (list): The list of elements to be sorted.
    Returns:
    list: A new list containing the sorted elements.
    """
    if len(input_array) == 1:
        return input_array

    half = len(input_array)//2
    return recombine(merge_sort(input_array[:half]), merge_sort(input_array[half:]))

def recombine(left_array, right_array):
    """
    Merges two sorted arrays into a single sorted array.
    Args:
        leftArr (list): The first sorted array.
        rightArr (list): The second sorted array.
    Returns:
        list: A merged and sorted array consisting of all elements from leftArr and rightArr.
    """
    left_index = 0
    right_index = 0
    merge_array = []
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merge_array.append(left_array[left_index])
            left_index += 1
        else:
            merge_array.append(right_array[right_index])
            right_index += 1

    merge_array.extend(left_array[left_index:])
    merge_array.extend(right_array[right_index:])

    return merge_array

arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
