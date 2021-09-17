# Object Introspection - Introspection can be said as the ability to recognize the object along with all its details, such as id or location at runtime.

# 1) type() - We use it to see the type of our object, that whether it is int, float or string
# 2) id() - Id provides us with the id allocated to the particular object. The id of each object is unique, meaning it is different, and no two objects can have the same id. 
# 3) dir() - dir() returns us a list of attributes and methods associated with an object. By using dir(), we can check the attributes that our object is composed of. It is mostly executed before and after updating our object by inserting more attributes or methods.

# Types of introspects:-
# Some of the other common Introspects:

# Functions	             Working
# hasattr()	    It checks if an object has an attribute.
# getattr()	    It returns the contents of an attribute if there are some.
# repr()	        It returns the string representation of an object
# vars()          It checks all the instance variables of an object
# issubclass()	This function checks that if a specific class is a derived class of another class.
# isinstance()	It checks if an object is an instance of a specific class. 
# __doc__	        This attribute gives some documentation about an object 
# __name__	    This attribute holds the name of the object
# callable()	    This function checks if an object is a function
# help()	        It checks what other functions do


#Example :

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"


skillf = Employee("Skill", "F")
print(skillf.email)   #This will print email
o = "this is a string"
print(id(o))         #id of that line will be printed
print(dir(skillf))   #dir will be printed

import inspect
print(inspect.getmembers(skillf))
