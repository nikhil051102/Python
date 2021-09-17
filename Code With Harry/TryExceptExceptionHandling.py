#Try and Except is used to handle error in program means if user inputs wrong variable then program will not throw error and exit program. Program after this will be execute fairly 

# 1)
print("num1 : ")
num1 = input()
print("num2 : ")
num2 = input()

try:
    print("The sum of these two numbers is", int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very Important")    

# 2)
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# We put print(5/0), the line that caused the error, inside a try block. If the code in a try block works, Python skips over the except block. If the code in the try block causes an error, Python looks for an except block whose error matches the one that was raised and runs the code in that block.
# In this example, the code in the try block produces a ZeroDivisionError, so Python looks for an except block telling it how to respond. Python then runs the code in that block, and the user sees a friendly error message instead of a traceback:
