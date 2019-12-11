import pytest

from linked_list import Node, LinkedList

linked_list = LinkedList()
values = ['a', 'b', 'c', 'd','e']

for el in values:
    linked_list.insert(el)

def test_list_nodes_order():
    assert "e, d, c, b, a" == linked_list.__str__()

@pytest.mark.parametrize("test_input,expected", [(0, 'a'), (1, 'b'), (4, 'e'), (-1, 'e'), (-3, 'c'), (-5, 'a')])
def test_units(test_input, expected):
    assert linked_list.kth_from_end(test_input) == expected

def test_index_out_of_range():
     # Example imported class
    with pytest.raises(Exception):  # Pass in the expected error
        linked_list.kth_from_end(5)

def test_index_out_of_range_negative():
     # Example imported class
    with pytest.raises(Exception):  # Pass in the expected error
        linked_list.kth_from_end(-6)

def test_empty_list():
    linked_list = LinkedList()
    with pytest.raises(Exception):  # Pass in the expected error
        linked_list.kth_from_end(0)


def test_list_1_elem():
    linked_list = LinkedList()
    linked_list.insert('z')
    assert linked_list.kth_from_end(0) == 'z'
    assert linked_list.kth_from_end(-1) == 'z'
    with pytest.raises(Exception):  # Pass in the expected error
        linked_list.kth_from_end(2)
