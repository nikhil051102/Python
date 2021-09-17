# Multilevel Inheritance : Class that is already derived from another class is derived by a third class

#Syntax
"""
class level1:
      def first(self):
            print ('code')

class level2(level1): #inherit level1
      def second(self):
             print ('with')

class level3(level2): #inherit level2
      def third(self):
            print ('harry')

obj=level3()
obj.first()
obj.second()
obj.third()
"""

#Example 

class Dad:             #Parent Class
    basketball =6

class Son(Dad):       #Derived Class 1
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):   #Derived Class 2
    dance =6
    guitar = 1

    def isdance(self):    #This function will overwrite the function of Son's Class.
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.guitar)

#Notes
# 1. We can access all the variables, Function etc of Parent Class because it will inherited.