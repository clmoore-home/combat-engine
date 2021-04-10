import combat_engine.combatants as cbt

import pytest

input_character = {'name': 'TestChar1', 'strength': 7, 'dexterity': 11,
    'endurance': 13}
target = {'name': 'TargetCombatant', 'strength': 6, 'dexterity': 10,
    'endurance': 12}
target2 = {'name': 'TargetCombatant2', 'strength': 6, 'dexterity': 10,
    'endurance': 12}


@pytest.mark.parametrize('attribute,expected', input_character.items())
def test_Combatant(attribute, expected):
    """
    GIVEN: Combatant input data in dictionary form
    WHEN: Combatant class instantiated with input attributes
    THEN: The combatant is instantiated with input attributes
    """
    combatant = cbt.Combatant(**input_character)
    assert getattr(combatant, attribute) == expected


def test_Combatant_has_hitpoints():
    """Test that an instantiated Combatant has an attribute with correctly
    calculated hitpoints"""
    combatant = cbt.Combatant(**input_character)
    assert combatant.health == 31


@pytest.mark.parametrize('attribute,expected', [
    ('str_modifier', 0),
    ('dex_modifier', 1),
    ('end_modifier', 2)
])
def test_Combatant_has_attribute_dms(attribute, expected):
    """Test that a dm is set for each of str, dex, end according to value"""
    combatant = cbt.Combatant(**input_character)
    assert getattr(combatant, attribute) == expected


@pytest.mark.parametrize('value,expected', [
    (1, -2),
    (2, -2),
    (3, -1),
    (4, -1),
    (5, -1),
    (6, 0),
    (7, 0),
    (8, 0),
    (9, 1),
    (10, 1),
    (11, 1),
    (12, 2),
    (13, 2),
    (14, 2),
    (15, 3)
])
def test_Combatant_calculate_modifier(value, expected):
    assert cbt.Combatant.calculate_modifier(value) == expected


def test_Combatant_takes_minor_action_aim():
    """Given a combatant, when taking an 'aim' minor action, then
    the aim state is stored for calculating DMs, and action count is
    updated"""
    combatant = cbt.Combatant(**input_character)
    tgt = cbt.Combatant(**target)
    combatant.take_aim(tgt)
    assert combatant.aim == 1
    assert combatant.actions == 2
    assert combatant.current_target == tgt


def test_Combatant_resets_aim_if_target_changes():
    """Given a combatant, when taking aim at a new target, then the aim count is
    reset."""
    combatant = cbt.Combatant(**input_character)
    tgt = cbt.Combatant(**target)
    tgt2 = cbt.Combatant(**target2)
    for _ in range(2):
        combatant.take_aim(tgt)
    assert combatant.aim == 2
    assert combatant.current_target == tgt
    combatant.take_aim(tgt2)
    assert combatant.current_target == tgt2
    assert combatant.aim == 1


def test_Combatant_action_count_depletes():
    """Given a Combatant, when taking a minor action, then their
    count depletes by 1, and when taking a major action, count
    depletes by two."""
    combatant = cbt.Combatant(**input_character)
    assert combatant.actions == 3
    tgt = cbt.Combatant(**target)
    combatant.take_aim(tgt)
    assert combatant.actions == 2


def test_combatant_count_resetting():
    """Given a combatant that has reached max number of minor actions per round,
    when they try to take another action, block it until the round is reset"""
    combatant = cbt.Combatant(**input_character)
    tgt = cbt.Combatant(**target)
    with pytest.raises(AttributeError):
        for _ in range(4):
            combatant.take_aim(tgt)
    assert combatant.actions == 0
