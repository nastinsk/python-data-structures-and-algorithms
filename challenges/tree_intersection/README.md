# Tree intersection

## Author: Anastasia Lebedeva, Sharmarke Ibrahim

## Challenge
Find common values in 2 binary trees.


## Approach & Efficiency
Time Big O(n) where n is amount of elements in the biggest tree.
Space Big O(n)

## Input:
tree1:
```
             __7___
            /      \
         __3       _2
        /   \     /  \
       6     9   10   1
      / \
     5   8
```
```
tree2:
                ___10___
               /        \
          ___134        _5
         /      \      /  \
       _23       9    10   45
      /   \
     32    8
```

## Output: {10,9,8,5}

## Solution
![Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/tree-intersectionjpg)

[Link to Code](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/challenges/tree_intersection/tree_intersection.py)


for test use command python -m pytest  (this is the only way to make pytest work with binary tree module)
