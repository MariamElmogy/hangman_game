#HANGMAN
import random
import time
from random import choice
import sys


def player():
    print("Hello !")
    time.sleep(0.)
    name = input("What is your name?")
    time.sleep(0.2)
    print("Good Luck ,", name)
player()

def main():
    global words
    global player_guess
    global play_again
    global alphabet
    global counter
    global tries
    words = choice(["apple","zombie","bingo","agree"])
    counter = 0
    play_again=''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    tries = 6
    player_guess = " "
main()


def ask_player():
    time.sleep(0.5)
    while True:
        time.sleep(0.5)
        ask_player = input("Are you ready to play?")
        if ask_player == "Yes" or ask_player == "yes":
            print("let's start to play...")
            break
        elif ask_player == "No" or ask_player =="no":
            sys.exit(print("You disappoint me :'(\n Have a good day"))
        else:
            print("You should answer with yes or no")
            
ask_player()



def guessing():
    global words
    global alphabet
    global guess 
    global player_guess
    tries = 6
    
    while tries > 0 :
        time.sleep(0.5)
        counter = 0
        for chr in words:
            if chr in player_guess:
                print (chr)
            else:
                print(" _ ")
                counter += 1
        if counter == 0:
            print("Congrats You Won!!") 
            break   
        time.sleep(0.4)
        guess = input ("Enter Your Guess= ")
        player_guess += guess
        time.sleep(0.3)
        if guess not in words:
            tries = tries - 1
            print("It's Wrong..Try again")
            print("Now You have",+tries,"Try")
        else:
            print("You put correct",guess)
        time.sleep(0.3)
        if tries == 0:
            print("sorry ! you lose :'(","The secret word is",words)

guessing()

def again_play():
    global play_again
    time.sleep(0.7)
    play_again=input("Do you want to play again? 1-Yes , 2-No")
    if play_again =="1" or play_again == "yes" or play_again == "Yes":
        print("let's Start again")
        main()
    elif play_again =="2" or play_again == "no" or play_again == "No":
        sys.exit(print("Good Bye"))
    else :
        print("Please enter correct answer")
again_play()