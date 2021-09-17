f = open("File.txt", "rt")  #open("FileName", "Mode") here "rt" is the default text mode 
content = f.read()
print(content)
f.close()    #We Must close the file after Use to Free RAM or For Optimisation

f = open("File.txt", "rt")  
content = f.read(3)  #Here 3 means it will read only 3 characters of file
print(content)
f.close() 

f = open("File.txt", "rt")  
content = f.read()
print("1.",content)   #This will print "1. " at the start of file
f.close() 

f = open("File.txt", "rb") #"rb" means read file in binary form
content = f.read()
print(content)
f.close()  

f = open("File.txt", "rt")
content = f.read()
for line in content:
    print(line)         #This will print lines by character by character          
f.close()  

f = open("File.txt", "rt")
for line in f:
    print(line)    #This will print file by line by line       
f.close()  