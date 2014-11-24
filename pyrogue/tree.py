"""
    pyrogue.tree
    ~~~~~~~~~~~~

    This module makes a self balancing binary tree.
"""

class Tree(object):
    """
    This class represents a self balancing binary tree; it takes an
    optional list to populate it at initialization time.
    """
    def __init__(self, starting_list=[]):
        self._root = None
        self.left = None
        self.right = None
        if len(starting_list) == 1:
            self._root = starting_list[0]
        else:
            for item in sorted(starting_list):
                self.insert(item)
    def insert(self, item):
        """
        This inserts an item into the tree, balancing itself along
        the way. Returns False if the item is already in the tree,
        else returns True.
        """
        if self._root is not None:
            leaf = self._root
            if item > leaf:
                self.right = Tree(item)
                self.left = Tree(leaf)
            elif item < leaf:
                self.right = Tree(leaf)
                self.left = Tree(item)
            else:
                # item == leaf
                return False
            # we are a branch now, not a leaf
            self._root = None
        else:
            # we are adding to one side of a branch
            left = self.left
            right = self.right
            if left._root is not None:
