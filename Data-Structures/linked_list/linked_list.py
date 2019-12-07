# class Node:

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "LinkedList created"

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.value
        return False


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


