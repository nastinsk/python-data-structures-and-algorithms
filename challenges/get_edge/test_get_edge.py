from graph import Graph
from get_edge import get_edge
import pytest

@pytest.fixture
def my_graph():
    graph = Graph()

    pandora = graph.add_node("Pandora")
    metroville = graph.add_node("Metroville")
    arendelle = graph.add_node("Arendelle")
    monstropolis = graph.add_node("Monstropolis")
    narnia = graph.add_node("Narnia")
    naboo = graph.add_node("Naboo")

    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(metroville, monstropolis, 105)
    graph.add_edge(arendelle, monstropolis, 42)
    graph.add_edge(metroville, narnia, 37)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(naboo, naboo, 250)
    graph.add_edge(monstropolis, naboo, 73)

    return graph


def test_two_direct_cities(my_graph):
    graph = my_graph

    assert get_edge(graph, ['Metroville', 'Pandora']) == (True, '$82')

def test_three_direct_cities(my_graph):
    graph = my_graph

    assert get_edge(graph, ['Arendelle', 'Monstropolis', 'Naboo']) == (True, '$115')

def test_two_non_direct_cities(my_graph):
    graph = my_graph

    assert get_edge(graph, ['Naboo', 'Pandora']) == (False, '$0')


def test_three_non_direct_cities(my_graph):
    graph = my_graph

    assert get_edge(graph, ['Narnia', 'Arendelle', 'Naboo']) == (False, '$0')


def test_not_in_graph(my_graph):
    graph = my_graph

    assert get_edge(graph, ['Metroville', 'Pandora', 'Kazan']) == (False, '$0')

