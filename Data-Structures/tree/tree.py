class _Node:
    """Private class to create a nodes for the tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Class to create a binary tree"""
    def __init__(self):
        self._root = None

    def pre_order(self, node=None, arr = []):
        """Method to return an array of trre values in "pre-order" order"""

        node = node or self._root

        arr.append(node.value)

        if node.left:
            self.pre_order(node.left, arr)

        if node.right:
            self.pre_order(node.right, arr)

        return arr

    def in_order(self, node=None, arr = []):
        """Method to return an array of tree values "in-order" """

        node = node or self._root

        if node.left:
            self.in_order(node.left, arr)

        arr.append(node.value)

        if node.right:
            self.pre_order(node.right, arr)

        return arr

    def post_order(self, node=None, arr = []):
        """Method to return an array of tree values "post-order" """

        node = node or self._root

        if node.left:
            self.post_order(node.left, arr)

        if node.right:
            self.post_order(node.right, arr)

        arr.append(node.value)

        return arr


class BinarySearchTree(BinaryTree):
    """Class to create a Binary Search Tree """

    def add(self, value):
        """Method that accepts a value, and adds a new node with that value in the correct location in the binary search tree"""

        node = _Node(value)
        if not self._root:
            self._root = node
            return

        current = self._root
        while True:
            if node.value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return


    def contains(self,value):
        """Method that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once."""

        if self._root == None:
            raise myException("Tree is empty")

        current = self._root
        while current:
            if current.value == value:
                return True
            if current.value > value:
                current = current.left
            else:
                current = current.right
        return False

class myException(Exception):
    pass

