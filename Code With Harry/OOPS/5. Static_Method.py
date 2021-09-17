class Employee:
    no_of_leaves = 8


    @staticmethod     #This method dont know anything about the Class 
                      #It doesnt take any cls and modify it...it just takes any argument and works upon it
                      #If we want any function which can be called only from specific class then we will use static method and this is used for optimisation.
    def printgood(string):
        print("This is good " + string)


Employee.printgood("Rohan")


#Notes :
# 1) staticmethod is just a function inside the class. 
# 2) We can access staticmethod with Class only not with its Objects. 
