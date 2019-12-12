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

    def insert(self, value):
        """method to insert new node to the beginnig of the list"""

        node = Node(value)
        node.next = self.head
        self.head = node

    def __str__(self):
        """method that returns a string that represents all list elements"""

        list_str = ''
        current = self.head
        while current:
            # print(current, "current")
            list_str += str(current.value ) + ', '
            current = current.next
        return list_str[:-2]


    def length_(self):
        """method to get lenght of the list"""

        length = 0
        current = self.head
        while current:
            length+=1
            current = current.next
        return length


def merge_list(list1, list2):
    """
    Merge_lists function which takes two linked lists as arguments. Zips them together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.
    """

    list1_length = list1.length_()
    list2_length = list2.length_()

    if list1_length == 0 and list2_length == 0:
        raise Exception("lists are empty")
    if list1_length == 0:
        list1.head = list2.head
        return list1.head
    if list2_length == 0:
        return list1.head

    current1 = list1.head  #current1.val == a
    current2 = list2.head   #current2.val == e
    temp = current2.next    #temp.val - f temp.next -> g ->h


    if list1_length > list2_length:
        for _ in range(list2_length-1):
            current1.next, current2.next = current2, current1.next
            current1 = current2.next
            current2, temp = temp, temp.next

        current1.next, current2.next = current2, current1.next


        return list1.head


    if list1_length < list2_length:
        for _ in range(list1_length-1):
            current1.next, current2.next = current2, current1.next
            current1 = current2.next
            current2, temp = temp, temp.next

        current1.next = current2
        return list1.head

    else:
        for _ in range(list1_length-1):
            current1.next, current2.next = current2, current1.next
            current1 = current2.next
            current2, temp = temp, temp.next
        current1.next = current2

        return list1.head



def create_list(vals):
    """helperfunction to create list with given values,, used in test module"""
    my_list = LinkedList()
    for i in vals:
        my_list.insert(i)
    return my_list

l_list1 = create_list(['d', 'c', 'b', 'a'])
l_list2 = create_list(['h','g','f','e', 'z'])
ref_to_head = merge_list(l_list1, l_list2)
print(ref_to_head.value)

if __name__ == "__main__":

    l_list1 = create_list(['c', 'b', 'a', 1, 4])
    l_list2 = create_list(['g','f','e'])

    print(merge_list(l_list1, l_list2))
