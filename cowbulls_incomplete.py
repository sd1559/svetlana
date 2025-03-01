import random

def compare_numbers(number, user_guess):#Compares the number randomly generated and the number included by user.
    cows = 0#code added below-edited by svetlana
    bulls = 0

    for i in range(len(number)):
        if user_guess[i] == number[i]:  
            bulls += 1
        elif user_guess[i] in number:  
            cows += 1
    return cows,bulls #returns list but the cows and bulls are separated-edited by svetlana

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number #four digit number has been added as 1000-edited by svetlana
guesses = 0
print (number)#parenthesis added-edited by svetlana

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")#raw_input has been changed to input-edited by svetlana
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
