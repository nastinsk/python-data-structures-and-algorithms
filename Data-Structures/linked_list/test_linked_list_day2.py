from linked_list import Node, LinkedList

linked_list = LinkedList()
values = ['a', 'b', 4, 'd']
for el in values:
    linked_list.insert(el)

def test_append():
    assert "d, 4, b, a, z" == linked_list.append('z')
