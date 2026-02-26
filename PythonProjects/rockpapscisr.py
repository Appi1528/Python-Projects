"""
workflow of project rockpapscisr.py

1- input form user (Rock , Paper, Scissor)
Computer Choice (Computer will randomly choose one option from Rock, Paper, Scissor)
3 - Results (decide who win)

Cases:
A ROCK
Rock vs Rock = Tie
Rock vs Paper = Paper wins
Rock vs Scissor = Rock wins

B PAPER

Paper vs Rock = Paper wins
Paper vs Paper = Tie
Paper vs Scissor = Scissor wins

C SCISSOR
Scissor vs Rock = Rock wins
Scissor vs Paper = Scissor wins
Scissor vs Scissor = Tie


"""

import random 
item_List = ["Rock", "Paper", "Scissor"]
user_choice = input("Enter your move  = Rock,Paper,Scissor = ")
computer_choice = random.choice(item_List)
print(f"User choice  = {user_choice} , Computer choice  = {computer_choice}")

if user_choice == computer_choice:
    print("It's a Tie")
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Paper covers Rock = Computer wins")
    else:
        print("Rock crushes Scissor = User wins")
elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Scissor cut Paper = Computer wins")
    else:
        print("Paper covers Rock = User wins")


elif user_choice == "Scissor":
    if computer_choice == "Paper":
        print("Scissor cuts Paper = User wins")
    else:
        print("Rock crushes Scissor = Computer wins")
