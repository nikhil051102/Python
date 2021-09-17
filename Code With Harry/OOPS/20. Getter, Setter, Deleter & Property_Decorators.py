# Decorators : Decorators are functions that take another function as an argument, and their purpose is to modify the other function without changing it.

#Property Decorator : @property along with getter method to access the value of the attribute

# Setter : We can set new values for a newer object, or we can update values for an older one.
# @function_name.setter is a setter method with which we can set the value of the attribute
#Syntax : 
#@function_name.setter
#def function

# Deleter : Deleter is used to delete the values passed as a parameter before. We can use a setter if we want to update or change the value, but we can not use it to delete the value. This is where deleter comes in; it removes the previous value and sets the variable equal to none. As in Oop we do not completely erase the existence of some variable but sets it equal to none.
# @function_name.deleter is a deleter method which can delete the assigned value by the setter method

#Syntax :
# Deleter method 
# @function_name.deleter


# Advantages of @property in Python:

# -> The syntax of defining @property is very concise and readable.
# -> We can access instance attributes while using the getters and setter to validate new values. This will avoid accessing or modifying the data directly.
# -> By using @property, we can reuse the name of a property. This will prevent us from creating new names for the getters, setters, and deleters.


#Example :

class Employee:
    def __init__(self, fname, lname):  #This Constructor will take input from the user
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):     #This function is to return the details of Employee
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter     #If we input mail, then this will extract firest name and last name from the email and Return it.
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter    #This will delete the fname and lname
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")    #This is the input to constructor

print(hindustani_supporter.email)      #will print email from line 38

hindustani_supporter.fname = "US"   #We have changed the value of fname

print(hindustani_supporter.email)    #Now with the help of setter this will give US.Supporter@codewithharyy.com bcz we have applied setter property without setter property we cant change the value of setter bcz while calling from line 56 that will set "Hindustani" as fname so we have to use the setter to change value of name 
hindustani_supporter.email = "this.that@codewithharry.com"  #This is reverse of upper program, This line will take email as input and will return fname, lname as output.
print(hindustani_supporter.fname)

del hindustani_supporter.email   #Deleting the email of "hindustani supporter."
print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.Perry@codewithharry.com"
print(hindustani_supporter.email)