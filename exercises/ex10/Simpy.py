"""EX10 - Simpy - Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730556314"


class Simpy:
    """New class Simpy."""
    
    values: list[float]

    def __init__(self, given_values: list[float]) -> None:
        """Create a new object of Simpy class."""
        self.values = given_values
        return None

    def __str__(self) -> str:
        """Change str output format."""
        return f"Simpy({self.values})"
    
    def fill(self, repeat_value: float, fill_number: int) -> None:
        """Change a Simpy's values with a specific number of a repeated value."""
        idx: int = 0
        self.values = []
        while idx < fill_number:
            self.values.append(repeat_value)
            idx += 1
        return None
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Make a Simpy's values a range of values starting and stopping at a given value and taking steps of a given size."""
        assert step != 0.0
        self.values = []
        while abs(start) < abs(stop):
            self.values.append(start)
            start += step
        return None
    
    def sum(self) -> float:
        """Calculate and return the sum of all the items in values."""
        idx: int = 0
        sum: float = 0.0
        while idx < len(self.values):
            sum += self.values[idx]
            idx += 1
        return sum
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Produce a new Simpy with things added with thing being added can be Simpy or float."""
        new_list: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                new_list.append(item + rhs)
            return Simpy(new_list)
        else:
            for item in range(0, len(self.values)):
                new_list.append(self.values[item] + rhs.values[item])
            return Simpy(new_list)
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Produce a new Simpy with things to the power of input which can be Simpy or float."""
        new_list: list[float] = []
        if isinstance(rhs, float):
            for item in self.values:
                new_list.append(item ** rhs)
            return Simpy(new_list)
        else:
            for item in range(0, len(self.values)):
                new_list.append(self.values[item] ** rhs.values[item])
            return Simpy(new_list)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Test to see if values are equal to each other to produce bool list."""
        new_list: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if rhs == item:
                    new_list.append(True)
                else:
                    new_list.append(False)
            return new_list
        else:
            for item in range(0, len(self.values)):
                if rhs.values[item] == self.values[item]:
                    new_list.append(True)
                else:
                    new_list.append(False)
            return new_list
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Test to see if values are greater than givens."""
        new_list: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if rhs < item:
                    new_list.append(True)
                else:
                    new_list.append(False)
            return new_list
        else:
            for item in range(0, len(self.values)):
                if rhs.values[item] < self.values[item]:
                    new_list.append(True)
                else:
                    new_list.append(False)
            return new_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Add subscription notation to Simpy class."""
        new_list: list[bool] = []
        if isinstance(rhs, int): 
            return self.values[rhs]
        else:
            idx: int = 0
            while idx < len(self.values):
                if rhs[idx]:
                    new_list.append(self.values[idx])
                idx += 1
            return Simpy(new_list)