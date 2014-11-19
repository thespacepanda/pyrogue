"""
    pyrogue/attack
    ~~~~~~~~~~~~~~

    This module represents the attack component for game entities.
"""

from component import Component

import random

class Attack(Component):
    """This component allows entities to attack one another."""
    def attack(self, target):
        """
        This takes an entity that has a health component, and modifies
        its health according to our attack value and its dexterity
        value.
        """
        assert target.stats

        if (owner.stats.accuracy >
            random.randrange(target.stats.dexterity)):
            damage = (owner.stats.strength -
                      random.randrange(target.stats.defense))
            if damage < 0:
                damage = 0
            target.stats.health -= damage
