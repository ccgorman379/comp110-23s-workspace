"""CQ04 - Dict Function Writing."""

def zip(list_1: list[str], list_2: list[int]) -> dict[str, int]:
    """Given two lists, returns a dict using those lists as keys and values."""
    result: dict[str, int] = {}
    if len(list_1) != len(list_2) or len(list_1) == 0 or len(list_2) == 0:
        return dict(result)
    idx: int = 0
    while len(list_1) < idx and len(list_2) < idx:
        result[list_1(idx)] = list_2(idx)
        idx += 1
    return dict(result)