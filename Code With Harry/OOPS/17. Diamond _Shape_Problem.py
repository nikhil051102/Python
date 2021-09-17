# Diamond Shape Problem is a problem of Multiple Inheritance.
# where, B and C are derived from A and D is derived from B, C
# for Diagram : https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/python-tutorials-for-absolute-beginners-66/base64.png

#Syntax :
"""
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D( B, C ):
    pass
"""

#Example :
"""

class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(C, B):
    def met(self):
        print("This is a method from class D")


a = A()
b = B()
c = C()
d = D()

d.met()
"""