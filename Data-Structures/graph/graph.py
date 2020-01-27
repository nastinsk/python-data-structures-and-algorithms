class Graph:
    """Class to implement Graph object with the given methods"""

    def __init__(self):

        self._adjacency_list = {}


    def add_node(self, value):
        """
        Adds a new vertex to the graph
        Input: the value of that vertex
        Output: the added vertex
        """
        vertex = Vertex(value)

        self._adjacency_list[vertex] = []

        return vertex


    def size(self):
        """Returns the total number of nodes in the graph"""
        return len(self._adjacency_list)


    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Adds a new edge between two nodes in the graph with ability to add weight
        Input: two vertexes to be connected by the edge

        *Both nodes should already be in the Graph
        """

        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in Graph')

        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in Graph')

        adjacencies = self._adjacency_list[start_vertex]

        adjacencies.append((end_vertex,weight))


    def get_nodes(self):
        """Returns all of the nodes in the graph as a collection"""
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        Returns a collection of vertexes connected to the given vertex with the weights of their connections
        Input: Takes in a given vertex
        """

        return self._adjacency_list[vertex]


class Vertex:
    """Class to create Vertex with the given value"""
    def __init__(self, value):
        self.value = value
