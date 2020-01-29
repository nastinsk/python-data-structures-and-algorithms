from graph import Graph

def helper(lst_nodes):
    dict_nodes = {}
    for node in lst_nodes:
        dict_nodes[node.value] = node
    return dict_nodes

def helper2(lst_nodes):
    neighbors = {}
    for node in lst_nodes:
        neighbors[node[0].value] = node
    return neighbors

def get_edge(graph, arr):


    dict_nodes = helper(graph.get_nodes())
    trip_price = 0

    for i in range (0, len(arr)-1):

        if arr[i] not in dict_nodes:
            return False, '$0'

        if arr[i] in dict_nodes:
            neighbors_dict = helper2(graph.get_neighbors(dict_nodes[arr[i]]))

            if arr[i+1] in neighbors_dict:
                trip_price += neighbors_dict[arr[i+1]][1]

            else:
                return False, '$0'

            # neighbors = graph.get_neighbors(dict_nodes[arr[i]])
            # for el in neighbors:
            #     print(neighbors[0][0].value, neighbors[1][0].value, neighbors[2][0].value)


            #     if el[0].value == arr[i+1]:
            #         print("now")
            #         trip_price += el[1]
            #         break
            #     else:

            #         return False, '$0'

    return True, f'${trip_price}'


