rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

player1 = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n")

if player1 == "0":
  print(rock)
elif player1 == "1":
  print(paper)
elif player1 == "2":
  print(scissors)
else:
  print("Invalid Input")

computer = random.randint(0,2)

print(f"Computer chose {computer}:")

list = [rock, paper, scissors]

if computer == 0:
  print(list[0])
if computer == 1:
  print(list[1])
if computer == 2:
  print(list[2])

if player1 == "0" and computer == 2:
  print("You win")
elif player1 == "1" and computer == 0:
  print("You win")
elif player1 == "2" and computer == 1:
  print("You win")
elif player1 == computer:
  print("It's a draw! Play again")
else:
  print("You lose")