"""EX07 - Dictionary Functions Tests- Practice With Testing Dictionary Functions."""

__author__ = "730556314"


from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_empty_1() -> None:
    """Testing invert with an empty dict input."""
    assert invert({}) == {}


def test_one_element_1() -> None:
    """Testing invert with a dict with one element."""
    test_dict: dict[str, str] = {"A": "1"}
    assert invert(test_dict) == {"1": "A"}


def test_many_1() -> None:
    """Testing invert with a dict with multiple elements."""
    test_dict: dict[str, str] = {"A": "1", "B": "2", "C": "3"}
    assert invert(test_dict) == {"1": "A", "2": "B", "3": "C"}


def test_empty_2() -> None:
    """Testing favorite_color with an empty dict input."""
    assert favorite_color({}) == ()


def test_one_element_2() -> None:
    """Testing favortie_color with a dict with one element."""
    test_dict: dict[str, str] = {"Cat": "Blue"}
    assert favorite_color(test_dict) == "Blue"


def test_many_2() -> None:
    """Testing favorite_color with a dict with multiple elements."""
    test_dict: dict[str, str] = {"Cat": "Blue", "Bella": "Pink", "Nann": "Blue"}
    assert favorite_color(test_dict) == "Blue"


def test_empty_3() -> None:
    """Testing count with an empty list input."""
    assert count([]) == {}


def test_one_element_3() -> None:
    """Testing count with a list with one element."""
    test_list: list[str] = ["A"]
    assert count(test_list) == {"A": 1}


def test_many_3() -> None:
    """Testing count with a list with multiple elements."""
    test_list: list[str] = ["A", "B", "C", "A"]
    assert count(test_list) == {"A": 2, "B": 1, "C": 1}