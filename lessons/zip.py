"""CQ04 - Dict Function Writing."""

def zip(list_1: list[str], list_2: list[int]) -> dict[str, int]:
    """Given two lists, returns a dict using those lists as keys and values."""
    result: dict[str, int] = {}
    if len(list_1) != len(list_2) or len(list_1) == 0 or len(list_2) == 0:
        return dict(result)
    i = 0
    for item in list_1:
        result[item] = list_2[i] 
        i += 1
    print(result)
    return result


zip(list_1 = ["hi", "hello", "good"], list_2 = [1, 2, 3])

    
