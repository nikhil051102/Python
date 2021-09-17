list1 = ["Nikhil", "Vijay", "Deore"]
for item in list1:
    print(item)  # Normal Printing of items

list2 = [["Nikhil", 1], ["Vijay", 2], ["Deore", 3]]
for item, position in list2:
    # If there is list in list then....
    print(item, "is in ", position, "position")

dict1 = dict(list2)
print(dict1)   #Typecasting list to dictionary 

for item, position in dict1.items(): #Here, only dict1() will not work we have to write dict1.items() to access its elements
    print(item, "is in ", position, "position")

for item in dict1:
    print(item)    #Only keys of dictionary will be printed not its pairs

#Range is used print numbers in specific range
for value in range(1,9):
    print(value)
numbers = list(range(1,8))
print(numbers)
even = list(range(0,15, 2)) #Here 0 : starting, 15 : ending, 2 : Gap
print(even)

#Writing Square of each number in specific range
Square = []
for value in range(1, 12):
    square = value**2
    Square.append(square)
print(Square)
