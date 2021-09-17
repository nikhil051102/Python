# Docstring in Function : In Simple words, it is description of any function

def function1(c, d):
    """This function will calculate average or mean of any two numbers"""   #Declaration of docstring
    Mean = (c+d)/2
    print(Mean)
    return Mean
y = function1(6, 8)
print(y)
print(function1.__doc__)                               #Calling of Docstring

