# Public : Anyone Can access.
# Protected : Only Class and Its Subclasses can access this variables.
# Private : Only Its Class can access it.

#IMP NOTE : Python uses a convention of prefixing the name of the variable or method with a single underscore(_) or double underscore(__) to emulate the behaviour of protected and private access specifiers respectively.

"""
Public Access Specifier : all the functions, variables, methods can be used publicly. Meaning, every other class can access them easily without any restriction. Public members are generally methods declared in a class that is accessible from outside the class

Syntax: 
class employee:
      def __init__(self, name, age):
            self.name=name
            self.age=age
"""

"""
Protected Access Specifier : its members and functions can only be accessed by the classes derived from it, i.e. its child class or classes.
we use a single underscore “_” sign before the data members of the class.


Syntax:
class employee:
      def __init__(self, name, age):
            self._name=name # protected attribute 
            self._age=age # protected attribute
"""

"""
Private Access Specifier : the variables and functions can only be accessed within the class. The private restriction level is the highest for any class. 
we use a double underscore “_­_” sign before the data members of the class

Syntax
class employee:
      def __init__(self, name, age):
            self.__name=name # private attribute 
            self.__age=age # private attribute
"""


#Example

# Public -
# Protected -
# Private -

class Employee:            #Base Class
    no_of_leaves = 8       #Public
    var = 8                #Public
    _protec = 9            #Protected
    __pr = 98              #Private

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp = Employee("harry", 343, "Programmer")
print(emp._Employee__pr)     #Note syntax
