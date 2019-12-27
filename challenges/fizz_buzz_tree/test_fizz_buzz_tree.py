from fizz_buzz_tree import _Node, BinaryTree, fizz_buzz, fizz_buzz_tree

import pytest

@pytest.fixture
def my_tree():
    tree = BinaryTree()
    tree._root = _Node(6)
    tree._root.left = _Node(15)
    tree._root.right = _Node(7)
    tree._root.left.left = _Node(23)
    tree._root.left.right = _Node(21)
    tree._root.right.right = _Node(5)
    tree._root.left.left.left = _Node(15)
    tree._root.right.right.left = _Node(7)
    return tree

def test_fizz_buzz6(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree._root.value == "Fizz"

def test_fizz_buzz15(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree._root.left.value == "FizzBuzz"

def test_fizz_buzz7(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree._root.right.value == "7"

def test_fizz_buzz23(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree._root.left.left.value == "23"

def test_fizz_buzz21(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree._root.left.right.value == "Fizz"


def test_fizz_buzz5(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree._root.right.right.value == "Buzz"

def test_fizz_buzz15_samevalue(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree._root.left.left.left.value == "FizzBuzz"

def test_fizz_buzz7_samevalue(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree._root.right.right.left.value == "7"

def test_empty_tree():
    tree = BinaryTree()
    new_tree = fizz_buzz_tree(tree)
    assert new_tree._root == None




