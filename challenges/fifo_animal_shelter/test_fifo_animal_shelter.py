from fifo_animal_shelter import Node, Queue, Animal, Cat, Dog, AnimalShelter

def test_cat():
    cat = Cat("Frodo")
    assert cat.value == 'Frodo'
    assert cat.type == 'cat'
    assert cat.next == None

def test_dog():
    dog = Dog("Sam")
    assert dog.value == 'Sam'
    assert dog.type == 'dog'
    assert dog.next == None


shelter = AnimalShelter()

def test_shelter_enqueue():


    shelter.enqueue(Cat("1"))
    assert shelter.queue1.front.value == "1"
    assert shelter.queue1.rear.value == "1"
    shelter.enqueue(Dog("2"))
    assert shelter.queue1.rear.value == "2"
    shelter.enqueue(Cat("3"))
    assert shelter.queue1.rear.value == "3"
    shelter.enqueue(Dog("4"))
    assert shelter.queue1.rear.value == "4"
    assert shelter.queue1.front.value == "1"

def test_shelter_dequeue():
    shelter = AnimalShelter()
    
    shelter.enqueue(Cat("1"))
    shelter.enqueue(Dog("2"))
    shelter.enqueue(Cat("3"))
    shelter.enqueue(Cat("a"))
    shelter.enqueue(Dog("4"))

    pet_adopted = shelter.dequeue('cat')
    assert pet_adopted.type == 'cat'
    assert pet_adopted.value == '1'

    pet_adopted = shelter.dequeue('cat')
    assert pet_adopted.type == 'cat'
    assert pet_adopted.value == '3'
    shelter.enqueue(Dog("b"))

    pet_adopted = shelter.dequeue('dog')
    assert shelter.queue1.front.value == "2"
    assert pet_adopted.type == 'dog'
    assert pet_adopted.value == '2'
