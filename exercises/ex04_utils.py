"""EX04 - list Utility Functions - Working with Lists."""

__author__ = "730556314"


def all(given_list: list[int], given_int: int) -> bool:
    """Given one list of ints and one int, indicate whether all ints in list are equal to int."""
    check_idx: int = 0
    if len(given_list) == 0:
        return False
    while check_idx < len(given_list):
        if given_list[check_idx] == given_int:
            check_idx += 1
        else:
            return False
    return True 


def max(given_list: list[int]) -> int:
    """Given one list of ints, return the largest in the list."""
    if len(given_list) == 0:
        raise ValueError("max() arg is an empty List")
    check_idx: int = 0
    max: int = given_list[0]
    while check_idx < len(given_list):
        if given_list[check_idx] >= max:
            max = given_list[check_idx]
            check_idx += 1
        else:
            check_idx += 1
    return max
    print(max)


def is_equal(given_list_1: list[int], given_list_2: list[int]) -> bool:
    """Given two lists, indicate whether every element at every index is equal in both lists."""
    check_idx: int = 0
    if len(given_list_1) != len(given_list_2):
        return False
    while check_idx < len(given_list_1):
        if given_list_1[check_idx] == given_list_2[check_idx]:
            check_idx += 1
        else:
            return False
    return True