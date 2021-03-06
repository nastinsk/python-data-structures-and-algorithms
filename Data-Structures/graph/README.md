# Implementation: Graph.

## Author: Anastasia Lebedeva

## Challenge
Implement the graph, which should be represented as an adjacency list, and should include the following methods: add_node(), add_edge(), get_nodes(), get_neighbors(), size()

## Approach & Efficiency
* add_node() time Big O(1), space Big O(1)
* add_edge() time Big O(1), space Big O(1)
* get_nodes() time Big O(1), space Big O(1)
* get_neighbors() time Big O(1), space Big O(1)
* size() time Big O(1), space Big O(1)


## API
* class Vertex():
    - Class to create Vertex with the given value
    - Input: Vertex value
* class Graph():
    - class to implement Graph object with the given methods:

* add_node():
    - Adds a new vertex to the graph
    - Input: the value of that vertex
    - Output: the added vertex
* add_edge():
    - Adds a new edge between two nodes in the graph with ability to add weight
    - Input: two vertexes to be connected by the edge
    - Both nodes should already be in the Graph
* get_nodes():
    - Returns all of the vertexes in the graph as a collection
* get_neighbors():
    - Returns a collection of vertexes connected to the given vertex with the weights of their connections
    - Input: Takes in a given vertex
* size():
    - Returns the total number of nodes in the graph



# Breadth-first method

## Challenge
Implement a breadth-first traversal on a graph.

## Approach & Efficiency
* breadth_first time Big O(n), space Big O(n)

### Input: Vertex
### Output: list of nodes staring from the given vertex in the breadth-first order

## Solution
![Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/breadth-first-graph.jpg)

[Link to Code](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/Data-Structures/graph/graph.py)



# Deapth-first method

## Challenge
Implement a deapth-first traversal on a graph.

## Approach & Efficiency
* deapth_first time Big O(n^2), space Big O(n)

### Input: Vertex
![Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/Day28Example.png)

### Output: list of nodes staring from the given vertex in the deapth-first order
[A, B, C, G, D, E, H, F]

## Solution
![Whiteboard Solution](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/assets/depth-first-graph.jpg)

[Link to Code](https://github.com/nastinsk/python-data-structures-and-algorithms/blob/master/Data-Structures/graph/graph.py)
