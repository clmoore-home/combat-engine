# combat-engine
A simple combat engine based on the Traveller universe, written in python.

Includes:

Combatants
    - Combatants will have health points and armor points
    - Combatants will have simple actions (3 minor or 1 major 1 minor) based on traveller rules, e.g.:
        - Use weapon
        - Use melee skill
        - Take cover
        - Dodge
        - Aim
    - It should be possible to specify equipment (armor and weapons) to calculate the modifiers
    - Methods for rolling 1d6, 2d6, but also methods that accept a roll as input and calculate success/damage
    - It should be possible to create a combatant out of a character from TTC app.
    - It should be possible to have computer controlled combatants.

Actions
    - Base minor and major actions defined.
    - These would be functions rather than classes.

Initiative tracker
    - Add combatants in turn order
    - Accounting for missed turns due to dodging
    - Round tracking would be included here?
    - Check the gamedev stack exchange for ideas.

"Sides" tracker
    - Keeps track of combatants belonging to different combat factions
    - Just a dictionary of lists
    - Could just be an attribute on the battlefield object

Battlefield
    - Set number of combatants, use initiative tracker to keep tabs
    - Tracks actions that have occurred towards various combatants and collates the information for computer controlled combatants
    - Round tracking here instead?

Gear
    - Gear classes can be equipped to combatants
    - Use a database for gear?
    - Splits down to separate classes for Armor, Weapons, Peripherals
    - Meta classes for base attributes like techlevel, damage, range (ABC library - Abstract Base Class)
    - For repeated methods, you could define a super class that inherits from the meta, or mixins that the concretes inherit from in addition to the meta.

Test environment
    - Console based run for testing mechanics