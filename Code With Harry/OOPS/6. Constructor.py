# Constructors are used to give argument to the class
# Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of class is created.In Python the __init__() method is called the constructor and is always called when an object is created.
# If there are common instance variables in the Objects of the class then we will use constructor to assign them in one go.

class Employee():
    no_of_leaves = 9
    
    def __init__(self, N, S, C):  #__init__ function works as constructor #Here Firstly "Rohit Sharma" value will be assigned to N then N will assign this value to self.name and same like for S and C
        self.name = N
        self.score = S
        self.city = C

Rohit = Employee("Rohit Sharma", 100, "Mumbai")  #This values goes only to the "__init__" function
Virat = Employee("Virat Kohli", 200, "Delhi")

print(Rohit.name)

#Notes 
# 1) A class in python can have ONLY ONE constructor.
# 2) We must give arguments to constructor if needed because constructor is helping in building class. 