
# Binary search in a sorted 1D array

## Authors: Anastasia Lebedeva, Terrell Douglas

## Challenge
Write a function called binary_search which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

### Example Input ---> Output:
* [4,8,15,16,23,42], 15 ---->  2
* [11,22,33,44,55,66,77], 90 ----> -1


## Approach & Efficiency
In our solution we created function wich takes two arguments(ordered list and search key element).
Create low var equal to 0, create high var equal to len(arr)
Set While loop which will rub on;y if len(arr)> 0
Set middle var to product of (low+high)//2
compare middle value with key value and either:
    - return value if equal
    -adjust high or low values
    - return -1 if key doesn't exist in arr
return -1 if lenght of arr is 0


Big O(log N)


## Solution
![Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/array-binary-search.jpg)

[Link to Code](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/array_shift/challenges/master/array_binary_search.py)
