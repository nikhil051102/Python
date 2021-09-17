import time
initial1 = time.time()   #Taken Current time

i = 0
while(i<5):
    print("Python")
    i += 1
print("While loop ran in", time.time()-initial1, "seconds")
initial2 = time.time()  #Taken Current time after while loop

for j in range(5):
    print("Python")
print("For loop ran in", time.time()-initial2, "seconds")

k = 0
while(k<5):
    print("This is Nikhil Deore")
    time.sleep(2)   #This function will sleep this loop for 2 seconds
    k = k+1

currenttime = time.asctime(time.localtime(time.time()))
print(currenttime)