# Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the 
# entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

# Here are a few instructions that you must have to follow:
# -> Do not use any type of modules like DateTime or date utils. (-5 points)
# -> Users can optionally provide a year, and your program must tell their age in that particular year. (3points)

# Your code should handle all sort of errors like:                       (2 points)
# -> You are not yet born
# -> You seem to be the oldest person alive
# -> You can also handle any other errors, if possible!


def age(input):
    if len(input) == 4:
        if int(input)<1900 or int(input)>2021:
            print("Its Wrong Input !")
        else:
            x = int(input)+100
            print(f"You will be 100 year old in {x}")
    elif len(input) == 2:
        if int(input)>99 or int(input)<1:
            print("Its Wrong Input !")
        else:
            y = (2021-int(input)) + 100
            print(f"You will be 100 year old in {y}")
    else:
        print("Invalid Input")

if __name__ == '__main__':
    input = input("Enter your age or Year or Birth : ")
    age(input)
    # z = int(input("1 to Continue Program and 0 to exit Program"))
    # if z==1:
    #     year = input("Enter the year in which you want to know your age : ")