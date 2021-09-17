# List
Crypto = ["Bitcoin", 45, "Ethereum", "Ripple", "Dogecoin", "Tether", 33]
print(Crypto[4])

# Function in Lists -  If we do any operation on original list then changes are applied permanently
Numbers1 = [34, 57, 78, 54, 90]
Numbers1.sort()
print(Numbers1)  # Numbers are sorted in ascending order by default

Numbers2 = [49, 67, 90, 76, 12]
Numbers2.reverse()
print(Numbers2)  # Numbers are reversed first and then printed

Numbers3 = [2, 56, 32, 57, 65]
print(max(Numbers3))  # Maximum number in the list will be printed
print(min(Numbers3))  # Minimum number will be printed
print(len(Numbers3))  # Lenght of list will be printed

#Append in list
Numbers4 = [45, 67, 89, 65, 78]
Numbers4.append(90)  # 90 will be added at the end of list
Numbers4.append(90)  # Again 90 will be added
print(Numbers4)

Numbers4.insert(1, 42)  # 42 will inserted at position 1 permanently
print(Numbers4)
# 65 will be removed permanently (If more than one 65s are present in list then very first from left will be removed means this function removes only one number)
Numbers4.remove(65)
print(Numbers4)

Numbers4.pop()
print(Numbers4)  # Last element of the list will be removed permanently

# Mutability(Can be Changed) and Immutability(Cannot be Changed)
# Immutable = Here elements in () are called tuple means they cannot be changed
List1 = (23, 56, 87, 90, 76)
# If only one element is present in tuple output will be that number without parenthesis or brackets
# If we put "," after only one element of tupple like list = (1,) then (1,) will be printed

# Swapping of two numbers : Below technique is applicable to only 2 numbers
a = 1
b = 4
a, b = b, a
print(a, b)

# Slicing of List - Slicing doesnt impact original list unlike function
Numbers5 = [23, 54, 56, 87, 30]
print(Numbers5[2:4:1])
# print(str[x:y:z]) Here x-starting point, y-end point, z-Interval in which u want to print
# The default value of x is 0, y is length of string & z is 1
# print(str[0:]) Whole list will be printed in this case
# print(str[ :y]) String list be printed till y
# print(str[::]) String list be printed as it is


# Slicing in negative numbers : It is same like slicing in String Functions
