class Employee():
    Company = "Multiwalls"
    Place = "US"

    def __init__(self, id, city):
        self.id = id
        self.city = city

    def printdetails(self):
        return f"Employee id : {self.id}, Employee City : {self.City}"


Vivek = Employee(12013292, "Mumbai")
Hardik = Employee(12013275, "Pune")

