#tell() : This function tell about where the file pointer is printed currently
#seek() : This function takes the pointer wherever we wants to move it
f = open("File2.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
f.seek(10)    #This function will move file pointer to 10th place
print(f.tell())
f.close()    #Closing file after operation  is good Practise