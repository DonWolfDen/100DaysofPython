import random

def compare():
    global lives
    print(f"You have {lives} attempts remaining")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too High")
        lives -= 1   
    elif guess < number:
        print("Too Low")
        lives -= 1
    elif guess == number:
        print(f"Correct! The number was {number}")
        return False
    if lives == 0:
        print(f"You ran out of attempts, you lose. The number was {number}")
        return False
        
print("Welcome to the guessing game")
play = ''
while play != exit:
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
    
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    number = random.randint(1, 100)
    
    cont = True
    while cont:
        k = compare()
        if k is False:
            cont = False
    play = input("Press enter to play again, type 'exit' to terminate")
