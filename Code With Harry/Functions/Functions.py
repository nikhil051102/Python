#Built in Sum Function
# a = 9
# b = 8
# c = sum((a,b)) #Sum ke andar Iterable Function hona chahiye mtlb List, Tupple etc.
# print(c)

#User-Defined Function
def function1():    #Defining Function
    print("Hello ! You are in Function 1")
function1()  #Agr hum idhr print(function1()) likhe toh uska output "None" hoga kyunki Function1 koi bhi value return nhi kr rha 

def function2(a, b):
    print("Hello ! You are in Function 2", a+b)
function2(5, 7)  

def function3(a, b):
    average = (a+b)/2
    print(average)
x =function3(5, 7)    
print(x)             #The output of this line will be "None" bcz Function3 is not returning any value 

def function4(c, d):
    Mean = (c+d)/2
    print(Mean)
    return Mean
y = function4(6, 8)
print(y)          #This will give output as Function3 bcz we have defined in function4 that it will return Mean


