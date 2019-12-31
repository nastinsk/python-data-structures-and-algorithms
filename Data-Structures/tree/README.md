# Implementation: Binary Tree and BST Implementation.

## Author: Anastasia Lebedeva

**Credit:**
**To Ethan Davis** for working with me on the .add method for BinarySearchTree.
**To Raven Delaney** for working with me on the .breadth_first method for BinaryTree.

## Challenge
Create a Binary Tree class with methods pre_order, in_order and post_order
Create a BinarySearchTree class with methods add(value) and contains()


## Approach & Efficiency
* for method .pre_order time big O(n), space big O(n) because we are adding all values of the elements in the tree to the array
* for method .in_order time big O(n), space big O(n) because we are adding all values of the elements in the tree to the array
* for method .post_order time big O(n), space big O(n) because we are adding all values of the elements in the tree to the array
* for method .add() time big O(h) -height of the tree, space O(1)
* for contains .add() time big O(h) -height of the tree, space O(1)
* for breadth_first() method Time and space Big O(n)

## API
* _Node - Private class to create a nodes for the tree and also nodes for the Queue
* Queue - class to create a queue

* BinaryTree - Class to create a binary tree
* ----.pre_order() - BinaryTree method to return an array of trre values in "pre-order" order
* ----.in_order() - BinaryTree method to return an array of tree values "in-order"
* ----.post_order() - BinaryTree method to return an array of tree values "post-order
* ----.breadth_first - a BinaryTree static method which takes a Binary Tree as its unique input, traversing the input tree using a Breadth-first approach, and returns a list of the values in the tree in the order they were encountered.

* BinarySearchTree - Class to create a Binary Search Tree, inherits its properties from BinaryTree class
* ----.add(value) - BinarySearchTree method that accepts a value, and adds a new node with that value in the correct location in the binary search tree
* ----.contains(value) - BinarySearchTree method that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.


## Challenge: Breadth-first Traversal
Write a breadth first traversal method which takes a Binary Tree as its unique input,traversing the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

## Solution
![Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/breadth-first.jpg)


