"""
    pyrogue/component
    ~~~~~~~~~~~~~~~~~

    This module provides the abstract base class for components.
"""

class Component(object):
    """These are components which will be owned by game entities."""
    def __init__(self, owner):
        self.owner = owner
    def update(self):
        """Simplest update function does nothing."""
        pass
