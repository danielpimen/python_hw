# Program Name: IT5413_A2_Prob2_dpiment1.py 
# Course: IT5413/Section W01
# Student Name: Daniel Pimentel-stein
# Assignment Number: 2
# Problem Number: 2
# Last Update: 1/28
# Purpose: Create a game where a random number between 1-100 is generated ask players to guess the number

##import library to generate random number
import random
##Generate Random Number
secret_num = random.randint(1,100)

##Intro Text 
print('')
print('Welcome to the Hi-Lo Game -- Five playing chances in winning')
print('--------------------------------------------------------------')
print('')

##Counter for how many tries a player has left 
tries = 5

##For Loop to to give 5 chances to guess 
for x in range(5):

    ##player input with number, player guess is automatically turned into an integer 
    player_guess = int(input("Please enter a number between 1 and 100: "))

    ##First Condition, if player guesses correct number 
    if player_guess == secret_num : 
        print('Great Job!! You won!')
        print('')
        print('Thank you for playing our Hi-Lo Game, please come again.')
    ##exit program when the player wins 
        exit()

    ##Second condition, if player guess is too high
    elif player_guess > secret_num : 
        tries -= 1 
        print('Too High! You have', tries, 'guess chances remaining.')
        print('')
        ## if there are no more tries left, loop is exited and game ends 
        if tries == 0: 
            print('Sorry you lost! You used up all the five playing chances in the game.')
            print('')
            print('The secret number is:', secret_num)
            print('')
            print('Thank you for playing our Hi-Lo Game, please come again.')          

    ##Third condition, if player guess is too low
    elif player_guess < secret_num : 
        tries -= 1 
        print('Too Low! You have', tries, 'guess chances remaining.')
        print('')
        ## if there are no more tries left, loop is exited and game ends 
        if tries == 0: 
            print('Sorry you lost! You used up all the five playing chances in the game.')
            print('')
            print('The secret number is: ', secret_num)
            print('Thank you for playing our Hi-Lo Game, please come again.')
    
