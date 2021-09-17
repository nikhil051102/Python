#Multiple Inheritance : One Child Classes derived from Multiple Base Class

#Syntax
"""
class Base1:
      def func1(self):
            print("this is Base1 class")
class Base2:
      def func2(self):
            print("this is Base2 class")

class Child(Base1 , Base2):
      def func3(self):
            print("this is Base3 class")

obj = Child()
obj.func1()
obj.func2()
obj.func3()
"""

# Example

class Employee:            #Base Class 1
    no_of_leaves = 8
    var = 8

    def __init__(self, aname, asalary, arole):     #Contructor of Base Class 1
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

class Player:              #Base Class 2
    var = 9
    no_of_games = 4
    def __init__(self, name, game):             #Constructor of Base Class 2
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class CoolProgramer(Player, Employee):         #Child Class...Here, Order Matters means Player is Written First so Child Class Will use Constructor of Player.

    language = "C++"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgramer("Karan",["Cricket"])
det = karan.printdetails()
print(det)
karan.printlanguage()
print(karan.var)