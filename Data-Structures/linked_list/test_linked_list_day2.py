from linked_list import Node, LinkedList

linked_list = LinkedList()
values = ['a', 'b', 4, 'd']
for el in values:
    linked_list.insert(el)


def test_append():
    assert "d, 4, b, a, z" == linked_list.append('z')

def test_append_to_empty():
    linked_list = LinkedList()
    assert "z" == linked_list.append('z')

def test_insert_before_value_in_list():

    assert "d, 4, b, 3, a, z" == linked_list.insert_before('a', 3)

def test_insert_before_value_not_in_list():

    assert 'Value is not in the list' == linked_list.insert_before('e', 3)

def test_insert_before_to_empty_list():
    linked_list = LinkedList()
    assert 'Value is not in the list' == linked_list.insert_before('e', 3)

def test_insert_after_value_in_list():

    assert "d, 4, b, 3, cat, a, z" == linked_list.insert_after(3, 'cat')

def test_insert_after_value_not_in_list():

    assert 'Value is not in the list' == linked_list.insert_after('e', 3)

def test_insert_after_to_empty_list():
    linked_list = LinkedList()
    assert 'Value is not in the list' == linked_list.insert_before('e', 3)
