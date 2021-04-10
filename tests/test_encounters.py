from combat_engine.encounters import Initiative

import pytest

from collections import namedtuple


def combatant_fixture(name, dex, roll):
    """Helper function that returns namedtuple to mimic
    combatant objects"""
    return namedtuple('Combatant', [
        'name', 'dexterity', 'initiative_roll'])(name, dex, roll)


player1 = combatant_fixture('Player1', 3, 6)
player2 = combatant_fixture('Player2', 12, 12)
player3 = combatant_fixture('Player3', 15, 7)
player_no_roll = combatant_fixture('Player_no_roll', 15, None)

all_players = [player1, player2, player3]


def initiative_setup(combatants):
    """Helper function that returns Initiative instance
    and adds combatants"""
    initiative = Initiative()
    for c in combatants:
        initiative.add_combatant(c)
    return initiative


def test_Initiative_participants():
    """Given players encountering combat, when initialised, an Initiative
    object exists which lists player turn order"""
    initiative = initiative_setup(all_players)
    assert initiative.combatants == [player1, player2, player3]


def test_add_combatant_requires_initiative_roll():
    """Given players encountering combat, when attempting to add
    them to an initiative instance without an initiative roll,
    then it fails with an exception"""
    with pytest.raises(ValueError):
        initiative = initiative_setup([player_no_roll])


# What should the initiative tracker return for the order? Options:
# 1.) A dictionary of combatants with players as keys and rolls