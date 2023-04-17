"""File to define Bear class."""


class Bear:
    """Bears living by the river."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """New bear attributes."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """One day passes for a bear."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Bear eating."""
        self.hunger_score += num_fish
        return None