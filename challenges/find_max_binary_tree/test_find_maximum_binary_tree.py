from find_maximum_binary_tree import _Node, BinaryTree, Queue
import pytest


def test_find_max_binarytree_empty():
    tree = BinaryTree()
    assert tree.find_maximum_value() == None

def test_find_max_binarytree_one_el():
    tree = BinaryTree()
    tree._root = _Node(8)
    assert tree.find_maximum_value() == 8

def test_find_max_binarytree_several_el():
    tree = BinaryTree()
    tree._root = _Node(8)
    tree._root.left = _Node(10)
    tree._root.right = _Node(-2)
    assert tree.find_maximum_value() == 10
    tree._root.left.left = _Node(195)
    tree._root.left.right = _Node(-195)
    tree._root.right.right = _Node(10000)
    tree._root.left.left.left = _Node(-0.567)
    tree._root.left.left.right = _Node(10000)
    assert tree.find_maximum_value() == 10000

def test_find_max_binarytree_same_values():
    tree = BinaryTree()
    tree._root = _Node(-2)
    tree._root.left = _Node(-2)
    tree._root.right = _Node(-2)
    tree._root.left.left = _Node(-2)
    tree._root.left.right = _Node(-2)
    tree._root.right.right = _Node(-2)
    tree._root.left.left.left = _Node(-2)
    tree._root.left.left.right = _Node(-2)
    assert tree.find_maximum_value() == -2
    tree._root.right.left = _Node(1)
    assert tree.find_maximum_value() == 1


def test_find_max__imbalanced_binarytree():
    tree = BinaryTree()
    tree._root = _Node(-2)
    tree._root.left = _Node(5)
    tree._root.left.left = _Node(9)
    tree._root.left.left.left = _Node(2)
    tree._root.left.left.left.left = _Node(2)
    assert tree.find_maximum_value() == 9

# This test fails, this has something to do with 0, enterpreter evaluates it as falsy
# can find a way how to make it truthy

def test_find_max_binarytree_zeros():
    tree = BinaryTree()
    tree._root = _Node(-2)
    tree._root.left = _Node(-4)
    tree._root.right = _Node(0)
    assert tree.find_maximum_value() == 0

