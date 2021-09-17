List = ["Bitcoin", "Tether", "Dogecoin", "Ethereum", "Tron"]

# By Normal Method
# i = 1
# for item in List:
#     if i%2 != 0:
#         print(f"Buy {item}")
#     i += 1

# Using Enumerate Function
for index, item in enumerate(List):    
    if index%2==0:
        print(f"Buy {item}")

# We dont need to Declare iterators Separately in this Function, this function will automatically increase those iterators.