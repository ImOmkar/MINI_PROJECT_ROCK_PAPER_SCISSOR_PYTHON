#START

import random
import time 
import sys 

def PlayOrNot(): #Selection for user and computer
    player_choice = input("\t\t====*Enter Rock or Paper or Scissors*=====\n").capitalize()
    choices = {1:'Rock', 2:'Paper', 3:'Scissor'}
    computer_choice = choices[random.randint(1, 3)]

    print('\t\t\tBreathe-in...Breathe-out...!!..\t\t\t')

    time.sleep(4)#It Will take 4sec of time to display the result

    print('\t============================================================')

    print('\t\t\tComputer:-',computer_choice)

    print('\t============================================================')
   
    if player_choice == computer_choice:
        return print('\t\t*****WINNER WINNER PANEER DINNER**Win-Win Situation for both side, (GAME TIED)****')
        
    
    if compare(player_choice,computer_choice):
        return print('\t\t***WINNER WINNER CHICKEN DINNER**You have Won****')
    
    else:
        return print('\t*****Sorry buddy Computer Has Won This Battle, You Are Unlucky This Time****')
    
        
    
#comparing stage(Game Logic)
def compare(player_choice, computer_choice):
    results = {('Paper','Rock'): True, 
               ('Paper','Scissors'): False,
               ('Rock','Paper'): False,
               ('Rock','Scissors'): True,
               ('Scissors','Paper'): True,
               ('Scissors','Rock'): False}
    return results[(player_choice, computer_choice)]

#initial stage
def GameOn():
    init = input('=====*Are you Excited To Play Rock, Paper, Scissors Game ??? Type Yes or No*==== \n')
    while init != 'Yes':
        if init == 'No':
            print("Sorry to say, but you are Big Looser!!!")
            sys.exit()#You'll be nomore in this game..
        else:
            print("Please Try Again!!")
            init= input("Are you Excited To Play Rock, Paper, Scissors Game ???\n")
            
    PlayOrNot()#This stage will start the next attempt depend upon your Yes or No reply
    while True:
        init = input('\tGreat game that was! You want to play again??\n')
        while init != 'Yes':
            if init == 'No':
                print("Game is over!!!")
                sys.exit()
            else:
                print('Please try Again!')
                init = input('Dont worry! You want to play again??\n').capitalize()
        PlayOrNot()
GameOn()
    
    
#END
