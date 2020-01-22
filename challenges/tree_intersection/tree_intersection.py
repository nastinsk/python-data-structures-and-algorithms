from binarytree import tree, build

# class _Node:
#     """Private class to create a nodes for the tree"""
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.next = None

# class BinaryTree:
#     """Class to create a binary tree"""
#     def __init__(self):
#         self._root = None


def tree_intersection(tree1, tree2):
    tree1_set = pre_order(tree1)
    set_result = pre_order2(tree2, tree1_set)
    if set_result == set():
        return None
    else:
        return set_result


def pre_order(tree, node=None, tree_set=None):
    if tree == None:
        return None
    if tree_set is None:
        tree_set = set()

    node = node or tree

    tree_set.add(node.value)
    if node.left:
        pre_order(tree, node.left, tree_set)
    if node.right:
        pre_order(tree, node.right, tree_set)
    return tree_set

def pre_order2(tree, tree_set, node=None, set_result=None):
    if tree_set == None or tree == None:
        return None
    if set_result is None:
        set_result = set()

    node = node or tree

    if node.value in tree_set:
        set_result.add(node.value)

    if node.left:
        pre_order2(tree, tree_set, node.left, set_result)
    if node.right:
        pre_order2(tree, tree_set, node.right, set_result)
    return set_result



if __name__ == "__main__":

    values = [10, 134, 5, 23, 9, 10, 45, 32, 8]
    root = build(values)
    print(root)
