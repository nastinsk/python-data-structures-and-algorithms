
# Implementation: Singly Linked Lists
Linked List is a linear data structure.
It is a series of connected "nodes" that contains the "address" of the next node. Each node can store a data point which may be a number, a string or any other type of data.

## Author: Anastasia Lebedeva

## Challenge
Create a Node classs and LinkedList class that will have a singly linked list properties like adding element to the beginning of the linked list, check for the existence of the elemnt in the list and print all list elements as a string

## Approach & Efficiency
for the insert() function big O(1) because we can add new element only at the beginnig of the list

for the includes() function big O(N) because I used a while loop to iterate over all  linked list elements until element won't be found

for the __str__() it is also big O(N) because I also used a while loop in my solution to iterate over the list

## API
* .insert() - takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
* .includes() - takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
* .__str__ - takes in no arguments and returns a string representing all the values in the Linked List


## Credits
Thanks to Ethan Davis for helping me during code challenge 05


# Linked list insertions

Addin new insertion methods to the LinkedList class.

## Author: Anastasia Lebedeva, James Bond

## Challenge
Add three new methods to the LinkedList instance that will add new element to the list in different positions.

## Approach & Efficiency
for the .append(value) function big O() because
for the .insert_before(value, new_val) function big O() because
for the .insert_after(value, new_val) it is big O() because

## API
* .append(value) - adds a new node with the given value to the end of the list
* .insert_before(value, new_val) - adds a new node with the given 'newValue' immediately before the first 'value' node
* .insert_after(value, new_val) - adds a new node with the given 'newValue' immediately after the first 'value' node.





