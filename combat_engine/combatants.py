from dataclasses import dataclass
from math import floor, ceil


@dataclass
class Combatant:
    """Defines combatant information, behaviour and state"""
    name: str
    strength: int
    dexterity: int
    endurance: int

    def __post_init__(self):
        self.health = self.strength + self.dexterity + self.endurance
        self.str_modifier = self.calculate_modifier(self.strength)
        self.dex_modifier = self.calculate_modifier(self.dexterity)
        self.end_modifier = self.calculate_modifier(self.endurance)


    @staticmethod
    def calculate_modifier(value):
        if value in range(0, 3):
            return -2
        if value in range(3, 6):
            return -1
        if value in range(6, 9):
            return 0
        if value in range(9, 12):
            return 1
        if value in range(12, 15):
            return 2
        return 3