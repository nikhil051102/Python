#string slicing for only one letter
str1 = "Python is Easy Language"
print(str1[5])

#string slicing for an defined interval
str2="Python is one of the best language"
print(str2[0:6])

#Length of String 
str3="Python is Good Language"
print(len(str3))

#Extended Slicing of String
# print(str[x:y:z]) Here x-starting point, y-end point, z-Interval in which u want to print
# The default value of x is 0, y is length of string & z is 1
str4="Python is Good for Machine Learning and Artificial Intelligence"
print(str4[0:10:2])
#print(str[0:]) Whole string will be printed in this case
#print(str[ :y]) String will be printed till y
#print(str[::]) String will be printed as it is

#Slicing with Negative numbers
str5="Python is very fast language"
print(str5[::-1]) #This technique is used to reverse the string
str6="Python is very fast language"
print(str6[-1:-13:-1])

#Other Functions

# 1)
str7="Macbook air is one of best machine"
print(str7.isalnum())
# False : If there are spaces between string and Alphabets and Numerics should be present in it
# True : If there are no spaces between string 

# 2)
str8="Macbook is very strong machine"
print(str8.isalpha())
# True : If all characters are alphabets
# False : If there are any spaces, numericals etc present

# 3)
str9="7218924290"
print(str9.isnumeric())
# True : If all characters are Numeric

# 4)
str10="Mumbai is financial capitai of India"
print(str10.endswith("India"))
#It is case sensitive means if we write INDIA instead of India then ouput will be False

# 5)
str11="Doge is Meme Currency"
print(str11.count("m"))
#It is Case Sensitive
#Used to count the frequency of character, number etc in string

# 6) 
str12="bitcoin is biggest crypto in terms of Market Capitalization"
print(str12.capitalize())
#Capitalizes only first character of string

# 7) 
str13="Ethereum is major competitor of Bitcoin"
print(str13.find("Bitcoin"))
#Tells position of character from which it is starting

# 8)
str14="Tron is my Favourite Crypto"
print(str14.upper())
#Capitalizes whole string

# 9)
str15 = "BAT is also good Crypto asset"
print(str15.lower())
#Changes whole string to lower case

# 10)
str16="HDFC is good bet for long term"
print(str16.replace("bet", "stock"))


#If u want to explore more function then visit (https://www.w3schools.com/python/python_ref_string.asp)