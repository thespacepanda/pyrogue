"""
    pyrogue.attack
    ~~~~~~~~~~~

    This handles the attack interaction between entities
"""

# Essentially we are going to modify the entity class so that it
# supports FOV - we will use a decorator, which is a higher-order
# function (takes and returns a function or class).

# -ing naming convention for our decorators, looks nice:
# @viewing
# class Entity(object) ...

def attacking(self):
    """
    This decorator adds attack functionality to an entity.
    """

    def attack(self, target):
        """
        This method calculates the attack every update.
        """
        from random import randint
    attack = self.stats.dexterity + self.equipment.weapon_in_hand

    if self.stats.accuracy > target.stats.dexterity:
       target.stats.health = target.stats.health - attack
       return target.stats.health
    else:
        return target.stats.health

    # alternative syntax to use decorators - can also use @decorator
    # but only when defining the function.
    entity.attack = attack
    return attack