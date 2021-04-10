from combat_engine.encounters import Initiative

import pytest

from collections import namedtuple


def combatant_fixture(name, dex, roll, round=1):
    """Helper function that returns namedtuple to mimic
    combatant objects"""
    return namedtuple('Combatant', [
        'name', 'dexterity',
        'initiative_roll', 'round'])(name, dex, roll, round)


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
        initiative_setup([player_no_roll])


def test_Initiative_order_method():
    """Given Initiative instance with combatants, when order method is called,
    then return the correct turn order"""
    initiative = initiative_setup(all_players)
    assert initiative.turn_order == [player2, player3, player1]


def test_Initiative_order_method_handles_equal_rolls_with_dex_check():
    """Given Initiative instance with combatants, when two cbts have equal
    initiative rolls, then use dex for secondary sort"""
    player4 = combatant_fixture('Player4', 12, 6)
    initiative = initiative_setup([player1, player4, player2])
    assert initiative.turn_order == [player2, player4, player1]


def test_Initiative_combatants_check_round():
    """Given Initiative instance with combatants, when it's time to take
    a turn, Initiative checks round attribute on each cbtant and stores lowest
    value on it's own attribute"""
    player_bigger_round = combatant_fixture('BigRound', 15, 7, 2)
    initiative = initiative_setup([player1, player_bigger_round])
    assert initiative.round == 1


def test_Initiative_restores_actions_on_round_change():
    """Given a set of combatants, when everyone has the same round value,
    they should all have the maximum number of actions available"""
