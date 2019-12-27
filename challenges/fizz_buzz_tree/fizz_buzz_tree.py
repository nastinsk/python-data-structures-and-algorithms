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


def fizz_buzz(value):
    """Function to do the fizz_buzz on the given value"""
    if value % 15 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)

def fizz_buzz_tree(tree):
    """Function to change all values in the given tree according to fizz_buzz """

    new_tree = BinaryTree()

    if not tree._root:
        return new_tree

    def helper(current):
    """Helper function to use in recurtion to add new values in the new_tree according to their positions in the original tree"""
        node = _Node(fizz_buzz(current.value))

        if current.left:
            node.left = helper(current.left)
        if current.right:
            node.right = helper(current.right)
        return node


    new_tree._root = helper(tree._root)
    return new_tree



