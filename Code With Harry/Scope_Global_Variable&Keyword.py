#Global and Local Variable

a = 10  #Global Variable "a"
def function1(n):
    a = 5  #Local Variable "a"
    b = 8  
    print(a, b)  #Here, This will print 5 as value of 'a' because we called it in function so it will call its local variable
    print(n, "I have Printed n")

function1("This is 'n' i'm printing")
print(a)  #Here, Global value of a will be printed bcz we have called it outside function1 so it will not have access to local variable
#We can access global variable from inside function but we cant access local variable of any function from global


#Global Keyword
i = 15
def function2():
    global i  #We have got permission to change global variable from this function
    i = i + 15
    print(i)

function2()
print(i)  #Here, we can see that function2() have changed value of i globally


#Nested Function with Local and Global Variable
def f1():
    x = 20  #This is the local variable of f1()
    def f2():
        global x
        x = 100  #Here, we are changing global value of x, if x is not present globally then this will make variable x globally and assign it
        print(x)
    print("Before calling f2", x)   #Here, we wrote this lines in f1() not in f2() if u get doubt check Identation
    # print(x) This line will give error, we are calling value of x in f2(), but there is no x present locally
    f2() #If we dont call this function then value of x will not be assigned, and this will give error if we try to print x from globally in line 38
    print("After Calling f2", x)
f1()
print(x)   #Global value of x will be printed