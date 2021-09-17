class Employee():
    no_of_leaves = 9   #This is Class variable. We can access this variable from any object of class or by class Name also but We can change class variable's value only by class not by its objects
    pass             

John = Employee()    #Declaring Objects
Smith = Employee()

John.name = "John Tesla"
John.id = 12013292

Smith.name = "Smith Williamson"
Smith.id = 12032912

#__dict__ function returns dictionary of variables and values that are assigned to that object
print(Employee.no_of_leaves)  #We are accessing Class variable with class name
print(Employee.__dict__)      #Getting that which elements are present in that class
Employee.no_of_leaves = 12    #Changing the value of class variable with the help of class name but we cant do this with Objects
print(Employee.__dict__)      #We can see change here that value has been changed
print(Employee.no_of_leaves)

print(Smith.__dict__)       #All elements present in dict will be printed
Smith.no_of_leaves = 10     #Here this will not change the value of class variables this will assign new instance variable to this object so that we have proved here that we cant change value of class variable from objects
print(Smith.__dict__)      #We can see change here