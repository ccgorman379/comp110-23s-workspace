"""EX07 - Dictionary Functions - Practice With Dictionary Functions."""

__author__ = "730556314"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, will invert keys and values to form a new dictionary."""
    result: dict[str, str] = dict()
    for item in given_dict:
        result_key: str = given_dict[item]
        result_value: str = item
        result[result_key] = result_value
    return result


def favorite_color(given_dict: dict[str, str]) -> str:
    """Given a dictionary, will return str with of most frequently appearing color value."""
    new_dict: dict[str, int] = dict()
    for item in given_dict:
        if given_dict[item] in new_dict:
            new_dict[given_dict[item]] += 1
        else:
            new_dict[given_dict[item]] = 1
    max_int: int = 0
    result: str = ()
    for item in new_dict:
        if new_dict[item] > max_int:
            max_int = new_dict[item]
            result = item
    return result    


def count(given_list: list[str]) -> dict[str, int]:
    """Given a list of str, will return dictionary with the number of times each str appears in the list."""
    result: dict[str, int] = dict()
    for item in given_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result 