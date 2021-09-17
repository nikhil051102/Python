# A class in python can have only one constructor so we can use class method as ALTERNATIVE Constructor.

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod        #This ClassMethod will work as Constructor
    def from_dash(cls, string):
        # 1.Method
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])

        # 2.Method
        return cls(*string.split("-"))    #Here, we will split that string and return argument


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")   #We will pass this string to classMethod

print(karan.no_of_leaves)
print(karan.salary)


# Notes :
# 1) Understanding Line 27 : from_dash is a classmethod which is spliting the input string into 3 variable then Employee will take those variable to pass them to constructor i.e we can use classmethod as alternative constructor. 