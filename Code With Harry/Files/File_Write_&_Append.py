# File Writing - "w" ka mtlb jo pehle likha hai usko saaf krdo aur jo abhi write kr rha hu vo likho
f = open("File_Write1.txt", "w") #Here "w" means write mode means File will be open in Write mode
f.write("Python is best Language i have ever seen")
f.close()

# File Appending = "a" ka mtlb jo pehle likha hai uske sath jo ab likh rha hu vo jod do
f = open("File_Write2.txt", "a") #Here "a" means append mode means file will open in append mode
f.write("\nPython is very Fast Language")
f.close()
#Hum is Program ko jitni bar run karenge utni bar Line uss file mein judti jayegi

f = open("File_Write2.txt", "a") 
a = f.write("\nPython is very Fast Language")  #Here this will print that How many words we have wrote in file after append
print(a)
f.close()

