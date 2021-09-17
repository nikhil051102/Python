# Take any number as input from user and tell user that his input number is less than or greater than our number. There should be limited number of guesses and if guesses gets over then we must print "Game Over"

n = 17
number_of_guesses = 1
print("You will get only 9 guesses to complete Game")
while(number_of_guesses<=9):
    input_number=int(input("Guess the Number : "))
    if input_number<17:
        print("Your Number is lesser than our Number. \n") 
    elif input_number>17:
        print("Your Number is greater than our Number. \n")
    else:
        print("Congratulations !! You Won\n")
        print(number_of_guesses, "Number of Guesses you tokk to finish.")
        break
    print(9-number_of_guesses, "Number of guesses left")
    number_of_guesses=number_of_guesses+1

if(number_of_guesses>9):
    print("Game Over !")