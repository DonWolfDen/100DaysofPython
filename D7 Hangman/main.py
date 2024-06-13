import random
from hangman_art import stages, logo
from hangman_words import word_list
#from replit import clear
import os
clear = lambda: os.system('clear')

print(logo)
start_of_game = True
end_of_game = False

chosen_word = random.choice(word_list).upper()
lives = len(stages) - 1
wrong = []
full_guesses = []
right = []
for _ in chosen_word:
    right += "_"

while not end_of_game:
    if start_of_game:
        guess = input("\nPress Enter to Start ").upper()
    else:
        guess = input("Guess a letter or the whole word: ").upper()

    clear()
    start_of_game = False
    wrong_word_print = ""
    already_print = ""
    win = ""
    
    if len(guess) != 1:
        if guess == chosen_word:
            right = list(guess)
            end_of_game = True
        elif guess != "":
            wrong_word_print = f"{guess} is not the word you're looking for"
            if guess not in full_guesses:
                full_guesses += [guess]
                lives -=1
    elif guess != "":
        guess = guess[0]

    if guess in right:
        already_print = f"You have already guessed {guess}."

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            right[position] = guess            
    print(f"{''.join(right)}")
    
    if guess not in chosen_word and len(guess) == 1:
        if guess in wrong:
            already_print = f"You have already guessed {guess}."
        else:
            wrong += guess
            lives -= 1
            
    if lives == 0:
        print("\nYou have no lives remaining.")
        win = f"You Lose!\nThe word was {chosen_word}"
        end_of_game = True
    if "_" not in right:
        end_of_game = True
        win = "You win!"
        
    print(win)
    print(already_print)
    print(wrong_word_print)
    print(f"\nIncorrect words: {full_guesses}")
    print(f"Incorrect letters: {wrong}")
    print(stages[lives])
