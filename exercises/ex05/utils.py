"""EX05 - list Utility Functions - Continuing to build utility functions and writing unit tests."""

__author__ = "730556514"

def only_evens(given_list: list[int]) -> list[int]:
    """Given list, returns a new list with only even elements of given list."""
    new_list: list[int] = []
    for value in given_list:
        if value % 2 == 0:
            new_list.append(value)
    return new_list

def concat(given_list_1: list[int], given_list_2: list[int]) -> list[int]:
    """Given two lists, returns a new lists with all elements of first list followed by all elements of second list."""
    new_list: list[int] = []
    for value in given_list_1:
        new_list.append(value)
    for value in given_list_2:
        new_list.append(value)
    return new_list

def sub(given_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Given list and two ints for indices, returns a new list that is a subset of the given list between the given idices."""
    new_list: list[int] = []
    for idx in range(start_idx, end_idx -1):
        new_list.append(given_list(idx))
    return new_list