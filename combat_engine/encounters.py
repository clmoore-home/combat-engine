"""Classes to track initiative, set the round, and keep a record
of all actions taken"""


class Initiative:
    """Calculate initiative for added players based on
    roll and dexterity values."""

    def __init__(self):
        self.combatants = {}

    def add_combatant(self, combatant):
        if not combatant.initiative_roll:
            raise ValueError('Combatant must roll for initiative')
        else:
            self.combatants[combatant.name] = combatant

    @property
    def turn_order(self):
        return sorted(self.combatants.values(),
            key=lambda x: (x.initiative_roll, x.dexterity), reverse=True)

    @property
    def round(self):
        return min(self.combatants.values(), key=lambda x: x.round).round

    @property
    def action_log(self):
        """Return a list of all actions taken"""

    def check_actions_and_restore(self):
        """Check that combatants all have the same round value, and
        if they do, restore action count to 3."""
        if all([cbt.round for cbt in self.combatants.values()]):
            for combatant in self.combatants.values():
                combatant.actions = 3
