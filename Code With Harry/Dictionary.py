# Dictionary is nothing but key value pairs
# Elements of Dictionary functions are defined in "{}"
# If d3=d2 and we change elements of d3 then elements of d2 will be changed automatically because we havent used "copy" function

d1 = {}  # Blank Dictionary
print(type(d1))  # This function will define type of datatype
d2 = {"Bitcoin": "LongTerm",
      "Dogecoin": "ShortTerm",
      "Ethereum": "Trading",
      "Tether":"Stable",
      "Polygon": "200",  # We can add Numbers also
      "Crypto": {"Tron": "Good", "VeChain": "Perfect"}}  # Here we have defined dictionary in dictionary
print(d2)  # Printing Elements of Dictionary
print(d2["Dogecoin"])  # Calling Specific Element of Dictionary
print(d2.get("Ethereum"))  # Another method of calling elements
print(d2["Crypto"]["Tron"])  # Calling Elements of Another Dictionary in d2

d2["Cardano"] = "ShortTerm"  # Adding new elements to dictionary
print(d2)                    #If cardano named key is present in dict. already then it will be overwritten means first value will   a                            #erased and new will be written

d2.update({"Tether": "Transactions"})  # Another method of adding elements 
print(d2)                              #If Tether named key is present already then it will be overwritten

del d2["Cardano"]  # Deleting elements
print(d2)

d3 = d2.copy()  # Copying elements of one dictionary to another
print(d3)       

print(d2.keys())  # Only Keys will be printed
print(d2.items())  # All elements will be printed
