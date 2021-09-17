#Lambda Function is also known as Anonymous Function
#Lambda function is used for convenience means if we want to write program without defining function then lambda function is used there 
#This function is One liner Function

def add(a, b):     #This is normal function for to add two numbers
    return a+b

add = lambda a, b: a+b   #This is alternative of above function with help of lambda function

print(add(4,5))