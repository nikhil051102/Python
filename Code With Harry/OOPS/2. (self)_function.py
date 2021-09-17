class Employee():
    no_of_leaves = 9   #Class Variable
    
    def printdetails(self):   #Here If self is present in bracket, if we call this function by Virat.printdetails then self means Virat it will automatically assign all self values to Virat
        return f"Name is {self.name}, Score is {self.score}, City is {self.city}"

Rohit = Employee()
Virat = Employee()

#Instance Variables
Rohit.name = "Rohit Sharma"  
Rohit.score = "101"
Rohit.city = "Mumbai"

Virat.name = "Virat Kohli"
Virat.score = "200"
Virat.city = "Delhi"

print(Rohit.printdetails())