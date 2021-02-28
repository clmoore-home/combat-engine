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

Battlefield
    - Set number of combatants, use initiative tracker to keep tabs
    - Tracks actions that have occurred towards various combatants and collates the information for computer controlled combatants

Gear
    - Gear classes can be equipped to combatants
    - Use a database for gear.

Test environment
    - Console based run for testing mechanics