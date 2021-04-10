"""Classes to track initiative, set the round, and keep a record
of actions taken"""


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

    @property
    def turn_order(self):
        return sorted(self.combatants,
            key=lambda x: (x.initiative_roll, x.dexterity), reverse=True)

    @property
    def round(self):
        return min(self.combatants, key=lambda x: x.round).round
