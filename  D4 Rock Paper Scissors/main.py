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

#Write your code below this line 👇
import random

weapons = [rock, paper, scissors]

user_choice = int(
    input(
        "Choose your weapon! Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
if user_choice >= 3 or user_choice < 0:
    print("You suck.\nYou died.")
else:
    print(weapons[user_choice])

    computer_choice = random.randint(0, 2)
    print("You fool! I chose:")
    print(weapons[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("You suck.\nYou died.")
    elif user_choice == 0 and computer_choice == 2:
        print("CURSES!")
    elif computer_choice == 0 and user_choice == 2:
        print("You died")
    elif computer_choice > user_choice:
        print("You died")
    elif user_choice > computer_choice:
        print("CURSES!")
    elif computer_choice == user_choice:
        print("Run it back!")
