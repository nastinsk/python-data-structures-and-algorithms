# Function to merge two linked lists.

## Author: Anastasia Lebedeva

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
* merge_list(list1, list2) function space Big O(1), time Big O(n)
To solve this challenge I've used a series of is statemnts to check if the any of the lists are empty, and return appropriate head pointer
If both lists content at least one element I've created a temp variable which stores next argument of the head node of the second list. This was made to preserve second list node connections from being lost during nodes transition nodes to the first list.
Then I am using a while loop that runs only until there is equal amount of elements in both lists and the current element of each list don't point to the None. In this whie loop I am reassigning nodes from different list to each other using Python swapping functionality.


## Solution
![Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/ll-merge.jpg)

[Link to Code](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/challenges/ll_merge/ll_merge.py)
