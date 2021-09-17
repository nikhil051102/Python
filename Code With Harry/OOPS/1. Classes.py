class Student():    #Declared Class  #Start class name with Capital Letter
    pass

Nikhil = Student()    #Assigned Objects or Instance of Class
Sarthak = Student()

#These are instance variables not class variables
Nikhil.surname = "Deore"        #Assigned Some values to Objects
Nikhil.University = "Lovely Professional University"  
Sarthak.surname = "Chavan"
Sarthak.University = "Loni College"

print(Nikhil.University)     #Calling Objects of Class

# Notes
# 1) If we call instance variable by "Nikhil.surname()" like this then Interpreter will throw error because it is variable not object.