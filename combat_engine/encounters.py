"""Classes to track initiative, set the round, and keep a record
of actions taken"""
from collections import defaultdict


class Initiative:
    """Calculate initiative for added players based on
    roll and dexterity values."""

    def __init__(self):
        self.combatants = []

    def add_combatant(self, combatant):
        if not combatant.initiative_roll:
            raise ValueError('Combatant must roll for initiative')
        else:
            self.combatants.append(combatant)
