"""EX05 - list Utility Functions - Writing Unit Tests."""

__author__ = "730556314"

from exercises.ex05.utils import only_evens, sub, concat

def test_empty() -> None:
    assert only_evens([]) == []

def test_one_element() -> None:
    test_list: list[int] = [2]
    assert only_evens(test_list) == []

def test_many() -> None:
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]

def test_empty() -> None:
    assert concat([],[]) == []

def test_one_element() -> None:
    test_list_1: list[int] = [1]
    test_list_2: list[int] = [2]
    assert concat(test_list_1, test_list_2) == [1, 2]

def test_many() -> None:
    test_list_1: list[int] = [1, 2, 3]
    test_list_2: list[int] = [4, 5, 6]
    assert concat(test_list_1, test_list_2) == [1, 2, 3, 4, 5, 6]

def test_empty() -> None:
    assert sub([], 0, 0) == []

def test_one_element() -> None:
    test_list: list[int] = [1]
    assert sub(test_list, 0, 0) == []

def test_many() -> None:
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(test_list, 1, 3) == [2, 3]