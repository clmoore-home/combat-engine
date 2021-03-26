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
        self.aim = 0
        self.current_target = None
        self.minor_action_count = 0

    @staticmethod
    def calculate_modifier(value):
        return floor((value / 3) - 2)

    def take_aim(self, target):
        """Set aim count and target attributes"""
        self.minor_action_count += 1
        match target:
            case self.current_target:
                self.aim += 1
            case _:
                self.current_target = target
                self.aim = 1
