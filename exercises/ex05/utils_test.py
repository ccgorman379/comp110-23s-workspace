"""EX05 - list Utility Functions - Writing Unit Tests."""

__author__ = "730556314"

from exercises.ex05.utils import only_evens, sub, concat


def test_empty_1() -> None:
    """Testing only_evens with an empty list input."""
    assert only_evens([]) == []


def test_one_element_1() -> None:
    """Testing only_evens with a list with one element."""
    test_list: list[int] = [2]
    assert only_evens(test_list) == [2]


def test_many_1() -> None:
    """Testing only_evens with a list with multiple elements."""
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]


def test_empty_2() -> None:
    """Testing concat with two empty list inputs."""
    assert concat([], []) == []


def test_one_element_2() -> None:
    """Testing concat with two lists each with one element."""
    test_list_1: list[int] = [1]
    test_list_2: list[int] = [2]
    assert concat(test_list_1, test_list_2) == [1, 2]


def test_many_2() -> None:
    """Testing concat with two lists each with multiple elements."""
    test_list_1: list[int] = [1, 2, 3]
    test_list_2: list[int] = [4, 5, 6]
    assert concat(test_list_1, test_list_2) == [1, 2, 3, 4, 5, 6]


def test_empty_3() -> None:
    """Testing sub with an empty list input and idices at zero."""
    assert sub([], 0, 0) == []


def test_one_element_3() -> None:
    """Testing sub with a list with one element."""
    test_list: list[int] = [1]
    assert sub(test_list, 0, 0) == []


def test_many_3() -> None:
    """Testing sub with a list with multiple elements."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(test_list, 1, 3) == [2, 3]