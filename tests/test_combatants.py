import combat_engine.combatants as cbt

import pytest

input_character = {'name': 'TestChar1', 'strength': 7, 'dexterity': 11, 'endurance': 13}


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
    """Test that an instantiated Combatant has an attribute with correctly calculated hitpoints"""
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
    print(value, cbt.Combatant.calculate_modifier(value))
    assert cbt.Combatant.calculate_modifier(value) == expected