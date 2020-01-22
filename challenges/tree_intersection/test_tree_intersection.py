from binarytree import tree, build
# # from tree_intersection import _Node, BinaryTree, tree_intersection, pre_order, pre_order2
from tree_intersection import tree_intersection, pre_order, pre_order2

import pytest

@pytest.fixture
def my_tree():
    #         __7___
    #        /      \
    #     __3       _2
    #    /   \     /  \
    #   6     9   10   1
    #  / \
    # 5   8
    values = [7, 3, 2, 6, 9, 10, 1, 5, 8]
    root = build(values)
    return root

@pytest.fixture
def my_tree2():
    #            ___10___
    #           /        \
    #      ___134        _5
    #     /      \      /  \
    #   _23       9    10   45
    #  /   \
    # 32    8

    values = [10, 134, 5, 23, 9, 10, 45, 32, 8]
    root = build(values)
    return root


def test_binarytree_module_build(my_tree):
    root = my_tree
    assert root.value == 7
    assert root.left.value == 3
    assert root.right.value == 2
    assert root.left.left.value == 6
    assert root.left.right.value == 9
    assert root.left.left.left.value == 5
    assert root.left.left.right.value == 8


def test_simply_tree_case(my_tree, my_tree2):
    tree1 = my_tree
    tree2 = my_tree2
    assert tree_intersection(tree1, tree2) == {10,9,8,5}


def test_no_match(my_tree):
    tree1 = my_tree
    values = [100, 100, 100, 100]
    tree2 = build(values)
    assert tree_intersection(tree1, tree2) == None
