# Insert and Shift an array in middle at index

## Authors: Anastasia Lebedeva, Kateryna Shydlovska

## Challenge
Write a function called insert_Shift_Array which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

### Example Input ---> Output:
[2,4,6,8], 5 ---->  [2,4,5,6,8]
[a,b,c,d,e], z ----> [a,b,c,z,d,e]


## Approach & Efficiency
In our solution we created function wich takes to arguments(list and element to be inserted in the middle), then we find middle of the list using '//' operator, than we used '%' operator to check if list have odd or even number of elements, and then depends on the condition we add the new element to the middle of original array using properties of list indexes.


## Solution
[Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/array_shift.jpg)

