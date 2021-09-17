# Abstract Method : @abstractmethod comes in abc module. If we inherit any class by Abstract Method then the functions declared in this class must be included in its child classes.
# -> “An abstract class is a class that holds an abstract method.”

# Important points about abstract class in Python:
#1. Abstract methods are defined in the abstract class. Mostly they do not have the body, but it is possible to have abstract methods with implementation in the abstract class. Any subclass deriving from such abstract class still needs to provide an implementation for that abstract methods.
#2. An abstract class can have both abstract methods as well as concrete methods.
# The abstract class works as a template for other classes. 
#3. By using the abstract class, we can define a structure without providing a proper implementation of every method. 
#4. It is not possible to create objects of an abstract class because Abstract class cannot be instantiated.
#5. An error will occur if the abstract method has not been implemented in the derived class.


from abc import ABC, abstractmethod

class Shape(ABC):   #We have inherited this class by ABC(imported from abc) so the function in this class with @abstractmethod "MUST" be included in its child class.
    @abstractmethod    #Abstrac
    def printarea(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):   #This Function is must in this class because this class is inheriting Shape class.
        return self.length * self.breadth

class Square(Shape):
    def __init__(self):
        self.side = 4
    
    def printarea(self):  #This Function is must in this class because this class is inheriting Shape class.
        return self.side*self.side

rect1 = Rectangle()
sq = Square()
print(rect1.printarea())
print(sq.printarea())