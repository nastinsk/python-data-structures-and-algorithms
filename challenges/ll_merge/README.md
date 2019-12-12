# Function to merge two linked lists.

## Authors: Anastasia Lebedeva

## Challenge
Write a function called merge_lists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

### Example Input ---> Output:
Input:
* lis1: head -> [1] -> [3] ->[2]->x
* list2: head -> [5] -> [9] ->[4]->x
Otput:
* head -> [1] -> [5] -> [3] -> [9] -> [2]->[4] ->x

Input:
* lis1: head -> [1] -> [3] ->x
* list2: head -> [5] -> [9] ->[4]->x
Otput:
* head -> [1] -> [5] -> [3] -> [9] ->[4] ->x

Input:
* lis1: head -> [1] -> [3] ->[2] ->x
* list2: head -> [5] -> [9] ->x
Otput:
* head -> [1] -> [5] -> [3] -> [9] ->[2] ->x


## Approach & Efficiency



## Solution
![Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/ll-merge.jpg)

[Link to Code](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/challenges/ll_merge/ll_merge.py)
