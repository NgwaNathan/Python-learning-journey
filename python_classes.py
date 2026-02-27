class Student:
    def __init__(self, name, matt= "FE22A268"):
        self.name = name
        self.matt = matt
    
    def display_info(self):
        print(f"my name is {self.name} and my matricule {self.matt}")
    

studen1 = Student("Ngwa Nathan")
studen2 = Student("Boss Man", "F22A345")
studen1.display_info()
studen2.display_info()

# class properties belongs to all objects where as properties defined in the init method belongs to each  object only

class Cars:
    object = "cars only" #this is a class property accesible by all objects 

    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def __str__(self):
        return f"{self.name} {self.model}"
    
    def description(self):
        print(f"This is a {self.name} and its a \n {self.model}")
    



first_car = Cars("Toyota", 2025)
# there class instance can be printed bcs of the __str__() method 


print(first_car)

second_car = Cars("Audi", 2011)
print(first_car.object)

first_car.description()
print(second_car.object)
second_car.description()

second_car.model = 2039
second_car.description()

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

compute = Calculator()
print(compute.add(10, 5))