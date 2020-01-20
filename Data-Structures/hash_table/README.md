# Implementation: Hash Tables.

## Author: Anastasia Lebedeva

## Challenge
Implement a Hashtable with the following methods:

add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
get: takes in the key and returns the value from the table.
contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
hash: takes in an arbitrary key and returns an index in the collection.

## Hashtables
Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value. In other words Hash table stores key-value pairs but the key is generated through a hashing function.

So the search and insertion function of a data element becomes much faster as the key values themselves become the index of the array which stores the data.

## Approach & Efficiency
* For .hash(self, key) method time Big O(n): n = the key length, space Big O(1)
* For .add(self, key, value) method time Big O(1) , space Big O(1)
* For .get(self, key) method time Big O(1), space Big O(1)
* For .contains(self, key) method time Big O(1), space Big O(1)


## API
* _Node:  Class for the Node instances
    - __init__(self, key, value): method to initiate the Node instance and store the ley and value in it.

* LinkedList: Class for creating the LinkedLists instances for hash table
    - __init__(self): method to initiat new linked list instance
    -  insert(self, key, value):  method to insert new node to the beginnig of the list
    -  includes(self, key): method to check if the given value in the liked list

* HashTable: Class to create a instance of Hash Table data structure
    -  __init__(self, size): method to initalise Hash table instance, takes the integer as a parameter to create a hash table based on the array of the given length
    -  hash(self, key): method that takes in an arbitrary key and returns an index in the collection.
    -  add(self, key, value): method that takes in both the key and value. This method hash the key, and add the key and value pair to the table, handling collisions as needed.
    -  get(self, key): method that takes in the key and returns the value from the table.
    -  contains(self, key): method that takes in the key and returns a boolean, indicating if the key exists in the table already

* KeyValueAlreadyExists(Exception):
    Raised when the given key already exists in the hash table
