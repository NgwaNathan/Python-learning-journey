# this design pattern allows us to create a class called the factory which hangles the creation of different object instances with some similar properties, 
# we mainly use this pattern if the object types are going to scale in the future and we are not sure if some different types of the object are going to be added 
# examples include an e-commerce app with different types of products

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        return None

# Usage
factory = AnimalFactory()
dog = factory.get_animal("dog", "Rex")
cat = factory.get_animal("cat", "Whiskers")

print(dog.speak())
print(cat.speak())
