i=0

while (True):
    if i+1<5:
        i=i+1
        continue  #When this condition is false then compiler will exit loop without checking its successive conditions
                  #It doesnt terminates the loop

    print(i+1, end=" ")
    if(i==44):
        break  #When this condition becomes false then compiler will exit loop
               #It terminates the loop

    i=i+1