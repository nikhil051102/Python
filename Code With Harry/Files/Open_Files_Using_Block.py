with open("File2.txt") as f:
    a = f.read(4)
    print(a)
#We dont need to openfile function and closing function, "with" function will handle it