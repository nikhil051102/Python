# Inspired by Mathematics's Sets
#Elements in Set are Unordered
s1 = set()  # Empty Set
print(s1)
print(type(s1))  # Assuring its type

s2 = set([1, 2, 3, 6, 5, 7, 9])  # Defining elements in set - This method is called defining set from list

s3 = (11, 22, 33,44, 55)   #We can transform list to set via typecasting.
list = list(s3)
print(list)
print(type(list))  

l1 = [12, 13, 2, 4, 24, 5, 60]
s3 = set(l1) #Another method of defining elements in set

s1.add(1) #Adding elements in set1
s1.add(1) #Here we have proved that set retains only unique values
s1.add(4)
print(s1)
print(len(s1)) #Length of Set
print(min(s1)) #Minimum Element of set
print(max(s1)) #Maximum element of set
s1.remove(4) #Removing element of s1
# s1.clear() #Clears all the elements from set s1
# s1.cop() #Returns shallow copy of set s1


s4 = s1.union({1, 2, 3})
print(s4) #Union will be printed
s5 = s1.intersection({1,3, 4})
print(s5) #Intersection will be printed
s6=s1.isdisjoint(s5)
print(s6) #True if s1 & s5 are disjoint and False if they arent
s7 = s1.symmetric_difference(s2) #Symmetric Difference - 2 sets will be merged but common elements will not be printed
print(s7)

# Objects of Set
# (https://docs.python.org/2/library/sets.html)