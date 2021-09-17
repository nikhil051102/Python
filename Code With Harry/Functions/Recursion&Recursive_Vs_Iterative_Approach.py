# Recursion - Using Function within function
# We are going to find factorial using Iterative and Recursive Approach

# Iterative Approach
"""
def iterative(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac

number1 = int(input("Factorial of : "))
print(iterative(number1))
"""

# Recursive Approach
def recursive(n):
    if n == 1:
        return 1
    elif n==0:
        return 1
    else:
        return n*recursive(n-1)


number2 = int(input("Factorial of : "))
print(recursive(number2))
