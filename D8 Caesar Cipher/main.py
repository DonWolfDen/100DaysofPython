alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
from replit import clear

def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1       
        
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)               
            if cipher_direction == "encode":
                if position + shift > 0:
                    position -= len(alphabet)                    
            new_position = position + shift_amount
            end_text += alphabet[new_position]
            
        else:
            end_text += letter
            
    print(f"\nHere's the {direction}d result: {end_text}")
 
restart = ""
while restart != "exit":
    print(logo)
    
    direction = ""
    while direction != "encode" and direction != "decode":
        direction = input(
            "\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
        if direction != "encode" and direction != "decode":
            print("Looks like a typo. Try again")
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)
    
    caeser(text, shift, direction)
    
    restart = input(
        "\nHit enter to decode another message, or type \"exit\" to terminate.")
    clear()
    
print("Program terminated.")
