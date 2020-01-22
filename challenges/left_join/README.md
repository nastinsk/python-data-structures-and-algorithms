# Left Join

## Author: Anastasia Lebedeva, Travis Williams

## Challenge
Implement a simplified LEFT JOIN for 2 Hashmaps.
For this challenge we assumed that our imput is 2 dictionaries.

## Approach & Efficiency
Time Big O(n)
Space Big O(n)

## Input:
### Synonym Dicitionary

| Key         | Value       |
| ----------- | ----------- |
| fond        | enamored    |
| wrath       | anger       |
| diligent    | employed    |
| outfit      | garb        |
| guide       | usher       |
...

### Antonym Dictionary

| Key         | Value       |
| ----------- | ----------- |
| fond        | averse      |
| wrath       | delight     |
| diligent    | idle        |
| guide       | follow      |
| flow        | jam         |
...

## Output:
{</br>
"fond": ["enamored","averse"],
"wrath": ["anger","delight"],
"diligent": ["employed","idle"],
"outfit": ["garb",None],
"guide": ["usher","follow"]<br>
}

## Solution
![Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/left-join.jpg)

[Link to Code](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/challenges/left_join/left_join.py)



