"""File to define Fish class."""


class Fish:
    """Fish living in the river."""

    age: int
    
    def __init__(self):
        """New fish attributes."""
        self.age = 0
        return None
    
    def one_day(self):
        """One day passes for a fish."""
        self.age += 1
        return None