"""
#Normal if else statements
var1 = 50
print("Input Number to check : ")
var2 = int(input())

if var2>var1:
    print("Greater")
elif var2==var1:
    print("Equal")
else:
    print("Smaller")
"""

#"in" Function
list1 = [1, 2, 3, 4, 5]
print(3 in list1) #True if 3 is in list
if 3 in list1:
    print("Yes it is in list")

#"not in" Function
print(10 not in list1) #True if 10 is not in list
if 10 not in list1:
    print("No its not in list")

