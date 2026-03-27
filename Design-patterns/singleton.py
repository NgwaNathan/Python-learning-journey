#  This pattern ensures that only one instance of a class exist no matter how many times the class is initiallized

class Animal:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            print("Creating new clas")
            cls._instance = super().__new__(cls)
        return cls._instance
    
animal1 = Animal()
animal2 = Animal()
animal3 = Animal()

print(animal1 == animal2 == animal3) 