# Overriding is an essential part of object-oriented programming since it makes the inheritance utilize its full power. Overriding avoids duplication of code, and at the same time enhance or customize the part of it. It is a part of the inheritance mechanism.

# Overriding occurs when a derived class or child class has the same method that has already been defined in the base or parent class. Being the same methods with the same name and number of parameters, when called checks for the method first in a child class, and runs it ignoring the method in the parent class because it is already overridden. In the case of Instance variables, the case is a little different. When the method is called, the program will look for any instance variable having the same name as the one that is called in the child, then in the parent, and after that, it comes again into child class if not found.

# Example:
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):  #Here, B(A) means B is inherited from A.
    classvar1 = "I am in class B"

    def __init__(self): #This function has overriden the constructor of inherited class therefore we will not be able access the Constructor of class A at any extent but still If we want to access then we will super().__init__ to access the constructor of class A.
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"


a = A()
b = B()

print(b.var1, b.classvar1)

#Most IMP Notes.
# 1).If we call self.classvar1 then Instance of object of Inherited class will be printed i.e "Instance var in class A" bcz If we call any function, object, etc then Interpreter will first find for Instance variables which are inside constructor, if he didnt find then he will find for Class Variable. 
# 2).