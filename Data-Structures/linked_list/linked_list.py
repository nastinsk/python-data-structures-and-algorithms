# class Node:
class Node:
    """ Class for the Node instances"""

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """ Class for the LInkedLists instances"""

    def __init__(self):
        """method to iniate a LinkedList"""

        self.head = None

    def __repr__(self):
        """method to represent that LinkedList created"""

        return "LinkedList created"

    def insert(self, value):
        """method to insert new node to the beginnig of the list"""

        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        """method to check if the given value in the liked list"""
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def __str__(self):
        """method that returns a string that represents all list elements"""

        list_str = ''
        current = self.head
        while current:
            # print(current, "current")
            list_str += str(current.value ) + ', '
            current = current.next
        return list_str[:-2]

    def append(self, value):
        """method to append new node to the end of the list"""

        current = self.head
        while current:

            print(current.value)
            if current.next == None:
                current.next = Node(value)
                return self.__str__()
            else:
                current = current.next

        self.head = Node(value)
        return self.__str__()

    def insert_before(self, value, new_value):
        """method to insert new element before the given element of the list"""

        if self.includes(value):
            current = self.head
            previous = current
            while current:
                if current.value == value:
                    node = Node(new_value)
                    node.next = current
                    previous.next = node
                    return self.__str__()
                previous = current
                current = current.next
        else:
            return 'Value is not in the list'

    def insert_after(self, value, new_value):
        """method to insert new element after the given element of the list"""

        if self.includes(value):
            current = self.head
            while current:
                if current.value == value:
                    node = Node(new_value)
                    node.next = current.next
                    current.next = node
                    return self.__str__()
                current = current.next
        else:
            return 'Value is not in the list'

