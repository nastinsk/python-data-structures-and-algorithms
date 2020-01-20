
class _Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    """ Class for the LInkedLists instances"""

    def __init__(self):
        """method to iniate a LinkedList"""

        self.head = None


    def insert(self, key, value):
        """method to insert new node to the beginnig of the list"""

        node = _Node(key, value)
        node.next = self.head
        self.head = node

    def includes(self, key):
        """method to check if the given value in the liked list"""
        current = self.head
        while current:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return False

# add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
# get: takes in the key and returns the value from the table.
# contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
# hash: takes in an arbitrary key and returns an index in the collection.

class HashTable:
    """Class to create a instance of Hash Table data structure"""

    def __init__(self, size):
        """method to initalise Hash table instance, takes the integer as a parameter to create an hash table based on the array of the given length"""

        self._array = [0 for i in range(size)]
        self.size = size


    def hash(self, key):
        """takes in an arbitrary key and returns an index in the collection."""

        key_chars = list(str(key))

        char_sum = 0

        for char in key_chars:
            char_sum += ord(char)

        index = (char_sum * 599) % self.size

        return index


    def add(self, key, value):
        """Method that takes in both the key and value. This method hash the key, and add the key and value pair to the table, handling collisions as needed."""

        index = self.hash(key)

        if self._array[index] == 0:
            ll = LinkedList()
            ll.insert(key, value)
            self._array[index] = ll
        else:
            ll = self._array[index]

            # Check if we want to give user ability to change the value in key value pair

            if ll.includes(key):
                return "Current key for key-value pair already exists in the table"
            else:
                ll.insert(key, value)

    def get(self, key):
        """Method that takes in the key and returns the value from the table."""
        index = self.hash(key)

        if self._array[index] != 0 and self._array[index].includes(key):
            return self._array[index].includes(key)
        else:
            return "No data found for the given key"


    def contains(self, key):
        



if __name__ == "__main__":
    hash_table = HashTable(1024)

    hash_table.add("Cat", "Frodo")


    hash_table.add("Cat", "Marsik")

