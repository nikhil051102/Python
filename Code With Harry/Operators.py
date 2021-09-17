# 1) Arithmetic Operator
print("5 + 6 is", 5+6) #Addition
print("5 - 6 is", 5-6) #Substraction
print("5 * 6 is", 5*6) #Multiplication
print("5**6 is", 5**6) #Exponential
print("5 / 6 is", 5/6) #Division operator which has Float output
print("15 // 6 is", 15//6) #Division Operator which has Integer output
print("5 % 3 is", 5%3) #Modulus Operator which gives "Remainder" as Output

# 2) Assignment Operator
x = 5  #Here, '=' puts 5 in x
print(x)
x += 7 #Adds 7 to x
x -= 7 #Substracts 7 from x
x /= 7 #Divides x by 7
x %= 7 #Remainder of x/7
x **= 7 #x to the power 7

# 3) Comparison Operator
i = 5
print(i==8) #Output is False because 5==8
print(i!=8)
print(i>=8)
print(i<=8)


# 4) Logical Operator
a =True
b = False
print(a and b) #True if both are same and False if any one them if different
print(a or b) #Always True 


# 5) Identity Operator
print(a is b) #True if both are same and False if they aren't
print(a is not b) 


# 6) Membership Operator
list = [1, 2, 3, 4,5, 6, 7]
print(2 in list) #True if 2 is in list and False if not


# 7) Bitwise Operator
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11
print(0 & 1) #It does AND(^) Operation of binary codes of 0 and 1
print(0 | 1)