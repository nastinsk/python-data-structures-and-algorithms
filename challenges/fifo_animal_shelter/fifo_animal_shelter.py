import copy

class Node:
    """ Class for the Node instances"""
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """class Queue which implements Queue data structure with its common methods"""

    def __init__(self):
        """Initiate class"""

        self.front = None
        self.rear = None

    def is_empty(self):
        """method to check if Queue is empty"""

        if self.front == None:
            return True
        return False


    def enqueue(self, new_node):
        """Method that takes any value as an argument and adds a new node with that value to the back of the queue """

        # new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Method that removes the node from the front of the queue, and returns the node’s value."""

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            return None

    def peek(self):
        """Method that returns the value of the node located in the front of the queue, without removing it from the queue."""

        if not self.is_empty():
            return self.front.value
        return None

class Animal:
    def __init__(self, pet_name):
        self.value = pet_name
        self.next = None

class Cat(Animal):
    type = 'cat'

class Dog(Animal):
    type = 'dog'


class AnimalShelter:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def enqueue(self, animal):
        self.queue1.enqueue(animal)

    def dequeue(self, pref):
        adopted_animal = None
        # while self.queue1.front:
        #     moved_animal = copy.deepcopy(self.queue1.front)
        #     # moved_animal.next = None
        #     if moved_animal.type == pref:
        #         adopted_animal = moved_animal
        #         self.queue1.dequeue()
        #     else:
        #         moved_animal.next = None
        #         self.queue1.dequeue()
        #         self.queue2.enqueue(moved_animal)

        # while self.queue2.front:
        #     moved_animal = copy.deepcopy(self.queue2.front)
        #     print("this is 2nd loop", moved_animal)
        #     moved_animal.next = None
        #     self.queue2.dequeue()
        #     self.queue1.enqueue(moved_animal)
        #     print("this is 2nd loop", self.queue1.front)
        if self.queue1.front == pref:
            adopted_animal = self.queue1.front
            self.queue1.dequeue()
            return adopted_animal
        else:
            while self.queue1.front !=pref:
                moved_animal =  self.queue1.front
                self.queue2.enqueue(moved_animal)
                self.queue1.dequeue()

                adopted_animal = self.queue1.front
            while self.queue2.front:
                moved_animal =  self.queue2.front
                self.queue1.enqueue(moved_animal)
                self.queue2.dequeue()

        return adopted_animal






if __name__ == "__main__":

    shelter = AnimalShelter()

    shelter.enqueue(Cat("1"))
    shelter.enqueue(Dog("2"))
    shelter.enqueue(Cat("3"))
    shelter.enqueue(Cat("a"))
    shelter.enqueue(Dog("4"))


    print('rear', shelter.queue1.rear.value)
    print('front', shelter.queue1.front.value)
    pet_adopted = shelter.dequeue('cat')
    print(pet_adopted.type)
    print(pet_adopted.value)

    print('rear', shelter.queue1.rear.value)
    print('front', shelter.queue1.front.value)
    pet_adopted = shelter.dequeue('cat')
    print(pet_adopted.type)
    print(pet_adopted.value)

    # shelter.enqueue(Dog("b"))

    print('rear', shelter.queue1.rear.value)
    print('front', shelter.queue1.front.value)
    pet_adopted = shelter.dequeue('dog')
    print(pet_adopted.type)
    print(pet_adopted.value)
