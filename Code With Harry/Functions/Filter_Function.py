# Filter Function : Filter function takes only True statements and Returns them

seq = [0, 1, 2, 3, 5, 8, 13]
  
result = filter(lambda x: x % 2 != 0, seq)  #Here, If lambda function gets true then only that number will be printed
print(list(result))

#Output will be all odd numbers in list
