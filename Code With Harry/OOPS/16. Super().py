# Super : When we want to call an already overridden method, then the use of super function comes in. It is a built-in function, so no requirement of any module import statement. What super does is, it allows us to use of the method of our superclass, that in the case of inheritance is the parent class
# super() returns a temporary object of the superclass that then allows you to call that superclass’s methods. The primary use case of super() is to extend the functionality of the inherited method.


#Syntax :
# class Parent_Class(object):
#       def __init__(self):
#             pass

# class Child_Class(Parent_Class):
#      def __init__(self):
#            super().__init__()


class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        super().__init__()  #Super() is used to call the constructor of inherited class if it has been overwritten.
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)