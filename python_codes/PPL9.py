class AnimalShelter:
    def __init__(self):
        self.animal_shelter = []
 
    def new_entry(self, animal):
        self.animal_shelter.append(animal)
        return animal.name
 
    def adopt_animal(self, animal_type):
        count = 0
 
        for i in self.animal_shelter:
            if animal_type == i.animal_type:
                self.animal_shelter.pop(count)
                return i.name
        count = count + 1
        return "Sorry! If you don't have that type of animal."
 
    def get_animal(self, animal):
        count = 0
        for i in self.animal_shelter:
            if animal.type == i.animal_type:
                print(f"Animal {count}")
                print(f"Name: {animal.name}")
                print(f"Age: {animal.age}")
                print(f"Type: {i.animal_type}")
                count = count + 1
 
            print("===========================================================================================")
 
    def all_animals(self):
        for i in self.animal_shelter:
            print(f"Name: {i.name}")
            print(f"Age: {i.animal_type}")
            print(f"Animal Type: {i.animal_type}")
 
            print("=====================================================================")
 
 
class Animal:
    def __init__(self, id_, name, age, animal_type):
        self.animal_id = id_
        self.name = name
        self.age = age
        self.animal_type = animal_type
 
 
a1 = Animal(1, "Tommy", 8, "Dog")
a2 = Animal(2, "Johnny", 2, "Cat")
a3 = Animal(3, "Richard", 4, "Tiger")
a4 = Animal(4, "Simba", 5, "Lion")
 
animal_shelter = AnimalShelter()
 
animal_shelter.new_entry(a1)
animal_shelter.new_entry(a2)
animal_shelter.new_entry(a3)
animal_shelter.new_entry(a4)
 
animal_shelter.all_animals()
animal_shelter.adopt_animal("Dog")
animal_shelter.all_animals()
