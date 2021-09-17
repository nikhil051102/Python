# watch this video for more details : https://youtu.be/pxEhxWhvIik
#Summary : Interpreter will enter into "try" at first, if function in this fails or gives error then this will run "except" but if "try" runs without throwing error then Interpreter will go into "else" without going to "except" and Whatever has been happened aboe "finally" will be run compulsory.

f1 = open("harry.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
