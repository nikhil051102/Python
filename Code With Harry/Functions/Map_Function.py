from typing import List


# Map Function - If we want to apply any specific function, datatype or anything in one go then we use Map Function
# Syntax : map("Function we want to apply", "Apply to whom")

List1 = ["1", "2", "3", "4", "5"] 
#Above Numbers are in String Form, If we want convert them into Integer in one go then we will use "map function"
integer = list(map(int, List1))
# If we write only map(int, List1) with typecasting it to List then it will return Object means map function returns object
print(integer)


# Squaring numbers using Map Function
def sq(a):
    return a*a

List2 = [1, 2, 3, 4, 5, 6, 7]
square = list(map(sq, List2))   #Here we are applying "sq" function to all the numbers in List
print(square)

# Squaring numbers using lambda and map function
List3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
function = list(map(lambda x:x*x, List3))
print(function)