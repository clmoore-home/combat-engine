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
        self.minor_action_count = 0

    @staticmethod
    def calculate_modifier(value):
        return floor((value / 3) - 2)

    def minor_action(self, action):
        """Pass instance to action to set appropriate attribute"""
        self.minor_action_count += 1
        for key, value in action.items():
            setattr(self, key, value)


def aiming(combatant, target):
    action = {}
    action['aim'] = combatant.aim
    action['current_target'] = target
    if combatant.aim < 7:
        action['aim'] = combatant.aim + 1
    return action
# Actions should all have the same format of returning a dictionary of attributes to set?