# Basic Game of Rock, Paper, Scissors

from random import randint

# Play Options
player_ops = ["Rock", "Paper", "Scissors"]

# Assign random numbers to computer
comp = player_ops[randint(0, 2)]

# Player set to None to stop infinite loop
player = None
while player != "done" or "Done":
    player = input("Rock, Paper, Scissors?\n ")
    if player == comp:
        print("Tie!")
    elif player == "Rock":
        if comp == "Paper":
            print("You lose!", comp, " covers ", player, ".")
        else:
            print("You win!", player, " smashes ", comp, ".")
    elif player == "Paper":
        if comp == "scissors" or comp == "Scissors":
            print("You lose!", comp, " cut ", player, ".")
        else:
            print("You win!", player, " covers ", comp, ".")
    elif player == "Scissors":
        if comp == "rock" or comp == "Rock":
            print("You lose!", comp, " smashes ", player, ".")
        else:
            print("You win!", player, " cut ", comp, ".")
    elif player == "done" or player == "Done":
        break
    else:
        print("Invalid input. Check spelling or case.")



