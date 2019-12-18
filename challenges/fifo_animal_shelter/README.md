# First-in, First out Animal Shelter.

## Author: Anastasia Lebedeva, Chris Ceder

## Challenge
Create a class called AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.</br>
Implement the following methods: </br>
* enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
* dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return None.

### Example Input ---> Output:
**enqueue(value)**
Internal state before: </br>
[cat2]->[dog1]->[cat1] </br>
Input </br>
"dog3", "dog"
Internal state after: </br>
[dog3]->[cat2]->[dog1]->[cat1] </br>


**dequeue()** </br>
Input: </br>
[]->[10]->[15]->[20] </br>

Output: </br>
20 </br>

Internal State: </br>
[5]->[10]->[15]) </br>



## Approach & Efficiency
* __init__(self, stack1) - initialization of the PseudoQueue class with the 1 given Stack and 1 empty Stack
* enqueue(value) - Method to inserts value into the PseudoQueue, using a first-in, first-out approach.
* dequeue() - Method to extract a value from the PseudoQueue, using a first-in, first-out approach. Returns value of extracted node


## Solution
![Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/queue-with-stacks.jpg)

[Link to Code](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/challenges/queue_with_stacks/queue_with_stacks.py)
