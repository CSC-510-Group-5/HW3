"""This module provides a function to generate a random array using the `shuf` command."""
import subprocess


def random_array(arr):
    """
    Replaces each element in the input array with a random integer between 1 and 20.
    Args:
        arr (list): A list of integers to be replaced with random integers.
    Returns:
        list: The modified list with each element replaced by a random integer between 1 and 20.
    """

    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
