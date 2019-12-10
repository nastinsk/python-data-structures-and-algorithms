# class Node:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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
                current = current.next
        return False

    def append(self, value):
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

    def __str__(self):
        list_str = ''
        current = self.head
        while current:
            # print(current, "current")
            list_str += str(current.value ) + ', '
            current = current.next
        return list_str[:-2]

    def insert_before(self, value, new_value):
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



test_list = LinkedList()
test_list.append(9)
