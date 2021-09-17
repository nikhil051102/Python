# Class Method : It is used to access the class variable with instances and change them.
# ClassMethod is type of decorator.

#Syntax 
# class myClass:
#     @classmethod
#     def myfunc (cls, arg1, arg2, ...):
#                           ....

class Employee:
    no_of_leaves = 8

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

harry = Employee()
rohan = Employee()

harry.change_leaves(98)  #This is changing class variable so this value will change for all 
print(rohan.no_of_leaves)



#Notes :
# 1) We can change class variable by "Employee.no_of_leaves = 34", what is Special use of classmethod ?
# -> By using class Method, we can change class variable with objects of class also means like "harry.no_of_leaves(45)"