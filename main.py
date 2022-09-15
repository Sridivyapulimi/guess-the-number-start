#Number Guessing Game Objectives
from art import logo
import random
easy_turns =10
hard_turns=5


def caluclate(number,Customer_no,turn):
    if Customer_no == number:
        print("you won")
        
    elif Customer_no > number: 
        print("too high")
        return turn-1
    elif Customer_no < number:
        print("too low")
        return turn-1
    
def difficulty():
    level = input("chose a difficultytype'easy'or'hard':").lower()
    if level== "easy":
        return easy_turns
    elif level == "hard":
        return hard_turns
def game():
    print(logo)
    print("Welcome to the number guessing game")
    print("I'm Thinking of a number betweern 1 and 100")           
    number = random.randint(1, 100) 
    turn = difficulty()
    Customer_no = 0
    while Customer_no != number:
        print(f"You have {turn} attempts remaining to guess the number.")

        Customer_no =int(input("Make a guess:"))
        turn = caluclate(number,Customer_no, turn)
        if turn == 0:
            print("you dont have turns ,you lose the game")
            return
        elif Customer_no != number:
            print("guess agian")
game()
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
