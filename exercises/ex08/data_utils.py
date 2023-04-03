"""EX08 - Data Wrangling - Functions for Data Wrangling."""

__author__ = "730556314"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in table: 
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column  headers as keys."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], row_number: int) -> dict[str, list[str]]:
    """Produce a new table with only the number of rows indicated."""
    result: dict[str, list[str]] = {}
    if len(table) <= row_number:
        return table
    for key in table:
        wanted_values: list[str] = []
        data_to_get: list[str] = table[key]
        idx: int = 0
        while idx < row_number:
            wanted_values.append(data_to_get[idx])
            idx += 1
        result[key] = wanted_values
    return result


def select(table: dict[str, list[str]], wanted_columns: list[str]) -> dict[str, list[str]]:
    """Produce a new table with only wanted columns."""
    result: dict[str, list[str]] = {}
    for column in wanted_columns:
        result[column] = table[column]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new table by combining two inputed tables."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else:
            result[column] = table_2[column]
    return result


def count(given_list: list[str]) -> dict[str, int]:
    """Given a list, will output how many times eahc of the items in the list appear."""
    result: dict[str, int] = {}
    for item in given_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result