# Single Inheritance : Child class Inheriting the Elements of Base Class.

#Syntax:
# class Parent_class_Name:
# #Parent_class code block
# class Child_class_Name(Parent_class_name):
# #Child_class code block

class Parent():
    def first(self):                #Function of Parent Class
        print('Parent function')
        
class Child(Parent):                #Function of Child Class
    def second(self):
        print('Child function')

object1 = Child()                   #Assigning Object1 as Child Class Variable, Here Object1 has inherited all the Variables of Parent Class and Child Class. So we can access all the variables from Object1 variable.
object1.first()                     #Accessing Parent Class Variable.
object1.second()                    #Accessing Child Class Variable.

object2 = Parent()                  #This is object of parent class only so we can't access variables of child class.
object2.first()
