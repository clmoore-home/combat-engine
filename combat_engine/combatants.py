import random

from dataclasses import dataclass
from math import floor


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
        self.actions = 3
        self.round = 0

    @staticmethod
    def calculate_modifier(value):
        return floor((value / 3) - 2)

    def roll_for_initiative(self, roll=None):
        """Set initiative_roll attribute on instance"""
        if hasattr(self, 'initiative_roll'):
            return self.initiative_roll
        if not roll:
            roll = sum((random.randint(1, 6), random.randint(1, 6)))
        self.initiative_roll = roll

    def deplete_action_count(self, action_type):
        """Deplete action count by one if action_type is minor,
        by 2 if major."""
        if self.actions == 0:
            raise AttributeError('Out of actions for this round')
        match action_type:
            case 'minor':
                self.actions -= 1
                self._set_round()
            case 'major':
                self.actions -= 2
                self._set_round()  # DRY this up?
            case _:
                raise ValueError('Action type not recognised')

    def take_aim(self, target):
        """Set aim count and target attributes"""
        self.deplete_action_count('minor')
        match target:
            case self.current_target:
                self.aim += 1
            case _:
                self.current_target = target
                self.aim = 1

    def _set_round(self):
        """Method used by Combatant to check/set the round
        when depleting actions"""
        if self.round == 0:
            self.round = 1
        if self.actions == 0:
            self.round += 1
