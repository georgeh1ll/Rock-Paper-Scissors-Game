#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:06:25 2021

@author: Georgehill
"""
import random

computer_wins = 0
player_wins = 0
draw_count=0

#defining player's choice in natural language
def player_choice():
    user_input = input("Choose Rock, Paper or Scissors: ")
    if user_input in ["Rock", "rock", "r", "R"]: 
        user_input = "Rock"
    elif user_input in ["Paper", "paper", "p", "P"]:
        user_input = "Paper"
    elif user_input in ["Scissors", "scissors", "s", "S"]:
        user_input = "Scissors"
    else:
        print("I don't understand, try again.") #input is not rock, paper or scissors
        player_choice()
    return user_input #returns which option user picked 

def computer_choice():
    computer_input = random.randint(1, 3) #computer randomly selecting an option
    if computer_input == 1:
        computer_input = "Rock" #computer chooses rock
        return computer_input
    elif computer_input == 2:
        computer_input = "Paper" #computer chooses paper
        return computer_input
    else:
        computer_input = "Scissors" #computer chooses scissors
    return computer_input


while True:
 
    user_input = player_choice()
    computer_input = computer_choice()
    
    if user_input == "Rock": #user enters rock
        if computer_input == "Rock":
            print("You: Rock. Computer: Rock. You draw.")
            draw_count += 1
        
        elif computer_input == "Paper":
            print("You: Rock. Computer: Paper. You lose.")
            computer_wins += 1
            
        elif computer_input == "Scissors":
            print("You: Rock. Computer: Scissors. You WIN!")
            player_wins += 1

    elif user_input == "Paper": #user inputs paper
        if computer_input == "Rock":
            print("You: Paper. Computer: Rock. You WIN!")
            player_wins += 1
        
        elif computer_input == "Paper":
            print("You: Paper. Computer: Paper. You draw.")
            draw_count += 1
            
        elif computer_input == "Scissors":
            print("You: Paper. Computer: Scissors. You lose.")
            computer_wins += 1

    elif user_input == "Scissors": #user inputs scissors
        if computer_input == "Rock":
            print("You: Scissors. Computer: Rock. You lose.")
            computer_wins += 1
        
        elif computer_input == "Paper":
            print("You: Scissors. Computer: Paper. You WIN!")
            player_wins += 1
            
        elif computer_input == "Scissors":
            print("You: Scissors. Computer: Scissors.You draw.")
            draw_count += 1
        
    #printing win counts
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(computer_wins))
    print("Draw count:" +str(draw_count))
    
    #end game or continue to play
    user_input = input("Play again? (Yes/No):")
    if user_input in ["yes", "Yes"]:
        pass #run game again
    elif user_input in ["no", "No"]:
        break #end game
    else:
        print("Game ended, Invalid user input. Please use Yes or No next time.")
        break #end game if invalid text entered 