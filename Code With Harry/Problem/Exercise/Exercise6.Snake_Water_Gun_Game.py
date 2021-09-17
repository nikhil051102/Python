# Snake Water Gun
import random

user_score = 0
computer_score = 0
i = 0

list1 = ["Snake", "Water", "Gun"]
Computer = random.choice(list1)

while(i < 5):
    User = input("Enter Your Choice : ")
    if User == "Snake":
        if Computer == "Water":
            user_score = user_score+1
            print("You Won")
        elif Computer == "Gun":
            computer_score = computer_score + 1
            print("You Lost")
        elif Computer == "Snake":
            user_score = user_score+0
            computer_score = computer_score + 0
            print("Tie")
    elif User == "Water":
        if Computer == "Snake":
            computer_score = computer_score + 1
            print("You Lost")
        elif Computer == "Gun":
            user_score = user_score + 1
            print("You Won")
        elif Computer == "Water":
            user_score = user_score+0
            computer_score = computer_score + 0
            print("Tie")
    elif User == "Gun":
        if Computer == "Water":
            computer_score = computer_score + 1
            print("You Lost")
        elif Computer == "Snake":
            user_score = user_score + 1
            print("You Won")
        elif Computer == "Gun":
            user_score = user_score+0
            computer_score = computer_score + 0
            print("Tie")
    else:
        print("Enter Valid Input !")
    i = i+1

if (user_score>computer_score):
    print("Congratulations, You Won !")
    print("Your Score is ", user_score)
    print("Computer Score is", computer_score)
elif (user_score<computer_score):
    print("You Lost the Game, Try Again !")
    print("Your Score is ", user_score)
    print("Computer Score is", computer_score)
else:
    print("Tie !")
