# # *args and **kwargs are used to make function flexible

# # *args - Takes any non-keyword as input 
# # *args passes variable number of non-keyworded arguments list and on which operation of the list can be performed.
# def adder(*num):
#     sum = 0
    
#     for n in num:
#         sum = sum + n

#     print("Sum:",sum)

# adder(3,5)
# adder(4,5,6,7)
# adder(1,2,3,5,6)

# # **kwargs - Takes any Keyword as input
# # **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
# def intro(**data):
#     print("\nData type of argument:",type(data))

#     for key, value in data.items():  #Here there is lot type of data type there we have targeted elements with data.items()
#         print("{} is {}".format(key,value))

# intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
# intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

