from linked_list import Node, LinkedList

linked_list = LinkedList()
values = ['a', 'b', 'c', 'd','e']

for el in values:
    linked_list.insert(el)

def test_list_nodes_order():
    assert "e, d, c, b, a" == linked_list.__str__()

def test_append():
    assert "a" == linked_list.kth_from_end(0)

def test_append():
    assert "a" == linked_list.kth_from_end(0)

