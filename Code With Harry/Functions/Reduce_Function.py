from functools import reduce

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Sum of all numbers in list using normal method
sum1 = 0
for i in List:
    sum1 = sum1 + i

print(sum1)

# Reduce Function 
#Syntax : 
#Sum of all numbers in list using lambda and Reduce Function
sum2 = reduce(lambda x, y: x+y, List)
print(sum2)