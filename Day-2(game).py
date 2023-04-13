# Rock, Paper and Scissors

import random

option_list = ['rock', 'paper', 'scissor']
# make a random choice
random_choice = random.choice(option_list)

user_input = input("Enter your choice (Rock, Paper or Scissor): ").lower()

while user_input not in ['rock', 'paper', 'scissor']:
    print("Invalid Input please try again  :(")
    user_input = input("Enter your choice (Rock, Paper or Scissor): ").lower()

#compare results
if user_input == random_choice:
    print("It's a DRAW..")
elif user_input == 'rock' and random_choice == 'scissor':
    print("Great.. You WON..!!")
elif user_input == 'paper' and random_choice == 'rock':
    print("Great.. You WON..!!")
elif user_input == 'scissor' and random_choice == 'paper':
    print("Great.. You WON..!!")
else:
    print("Oops.. The Computer WON..!!")