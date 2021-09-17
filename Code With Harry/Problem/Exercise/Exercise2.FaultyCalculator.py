# Design a calculator which will correctly solve all problems except 45*3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator and the two numbers as input from and then return the result

print("First Number :")
num1 = int(input())
print("Second Number : ")
num2 = int(input())
print("Which type of operation you want to do : ")
operation = input()
if num1 == 56 and num2 == 9 and operation == "+":
    print("77")
elif num1==45 and num2==3 and operation == '*':
    print("555")
elif num1==56 and num2==6 and operation == '/':
    print("4")
elif operation == "+":
    print(num1+num2)
elif operation=="-":
    print(num1-num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    print(num1/num2)
else:
    print("Enter valid Operation !")
