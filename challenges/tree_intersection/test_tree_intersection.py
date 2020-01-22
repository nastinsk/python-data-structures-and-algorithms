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

def test_everything_match(my_tree):
    tree1 = my_tree
    values = [7, 3, 2, 6, 9, 10, 1, 5, 8]
    tree2 = build(values)

    assert tree_intersection(tree1, tree2) == {7, 3, 2, 6, 9, 10, 1, 5, 8}

def test_floats():
    tree1 = build([0.3, 5, -54, -3, 34])
    tree2 = build([-54, 95, 0.3, 123, 34])

    assert tree_intersection(tree1, tree2) == {0.3, -54, 34}

def test_empty_tree():
    tree1 = build([])
    tree2 = build([3, 4])
    assert tree_intersection(tree1, tree2) == None

def test_2nd_tree_is_empty():
    tree1 = build([3, 3, 4, 5])
    tree2 = build([])
    assert tree_intersection(tree1, tree2) == None

def test_same_values():
    tree1 = build([10, 10, 10, 8])
    tree2 = build([10, 10, 10, 10, 10])
    assert tree_intersection(tree1, tree2) == {10}




