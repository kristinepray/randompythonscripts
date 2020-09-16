#!/usr/bin/python

from random import randint

t = ["rock", "paper", "scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input ("Rock, Paper, Scissors?")
    if player == computer:
        print("Tied!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer) 
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose", computer, "cuts", player)
        else:
            print("You win", player, "smashes", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
            print("That is not a valid play please try again")
    
    player == False
    computer == t[randint(0,2)]
