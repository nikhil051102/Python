# Comprehensions : Pythonic way of writing code. Using comprehension, we compress the code so it takes less space
# There are many comprehensions in python like List Comprehension, Dictionary Comp., Set Comp. Generator Comp.

# 1. List Comprehension
listA = [a for a in range(50) if a%5==0]
print(listA)

# 2. Dictionary Comprehension
dict1 = {i:f"item {i}" for i in range(1, 1000) if i%100==0}
print(dict1)
# 2.1  Dictionary Comprehension is used to reverse the order of key:value pairs.
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n", dict2)


# 3. Set Comprehension
dresses = [dress for dress in ["dress1", "dress2","dress1",
                               "dress2","dress1", "dress2"]]
print(dresses)  #Here, dress1, dress2 will be printed only values will not be repeated because it is Set Comprehension

# 4. Generator Comprehension
evens = (i for i in range(100) if i%2==0)
print(evens.__next__())