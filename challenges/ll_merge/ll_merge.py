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

    def length_(self):
        """method to get lenght of the list"""

        length = 0
        current = self.head
        while current:
            length+=1
            current = current.next
        return length

    def kth_from_end(self, k):
        """method to find k-th value from the end of the linked list.
        In our implementation K can be positive or negative and list can be empty"""

        length = self.length_()

        if not -length <= k < length:
            raise Exception("k not in the range")

        step_count = None

        if k >= 0:
            step_count = length - k -1
        if k < 0:
            step_count = abs(k)-1

        current = self.head
        for i in range(step_count):
            current = current.next
        return current.value






def merge_list(list1, list2):
    """
    MergeLists function which takes two linked lists as arguments. Zips them together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
    """
    list1_length = list1.length_()
    list2_length = list2.length_()
    if list1_length == 0 and list2_length == 0:
        raise Exception("lists are empty")
    if list1_length == 0:
        return l_list2.__str__()
    if list2_length == 0:
        return l_list1.__str__()

    current1 = list1.head  #current1.val == a
    current2 = list2.head   #current2.val == e
    temp = current2.next    #temp.val - f temp.next -> g ->h


    if list1_length > list2_length:
        for _ in range(list2.length_()-1):
            current1.next, current2.next = current2, current1.next
            current1 = current2.next
            current2, temp = temp, temp.next

        current1.next, current2.next = current2, current1.next
        current1 = current2.next

        return l_list1.__str__()


    if list1_length < list2_length:
        for _ in range(list1.length_()-1):
            current1.next, current2.next = current2, current1.next
            current1 = current2.next
            current2, temp = temp, temp.next

        current1.next = current2
        return l_list1.__str__()

    return l_list1.__str__()





if __name__ == "__main__":
    l_list1 = LinkedList()
    val = ['c', 'b', 'a', 1, 4]
    for i in val:
        l_list1.insert(i)


    l_list2 = LinkedList()
    val = ['g','f','e']
    for i in val:
        l_list2.insert(i)
    print(merge_list(l_list1, l_list2))
