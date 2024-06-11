################### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###############################################################
        ## Define Functions ##

## Draw a card
def deal_card(): ####
    faces = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    return faces[random.randint(0, len(faces)-1)]  
## Calculate totals
def calculate_total(target): ####
    faces = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "X"]
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 0]
    cards = []
    cards += target
    for i in range(len(target)):
        cards[i] = deck[faces.index(cards[i])]
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)    
## Keep ui clean, check Blackjack and declare winners
def update_ui(): ##
    clear()
    print(logo)
    print(f"Dealer's hand: {dealer_faces}\nDealer's total: {dealer_total}\n")
    print(f"Your hand: {player_faces}\nYour total: {player_total}\n")
    if player_total == 21 and len(player_faces) == 2:
        print("Blackjack!")
    if dealer_total == 21 and len(dealer_faces) == 2:
        print("Dealer has Blackjack!")
    if cont_play == "stand" and player_total <= 21:
        print(f"You stand with {player_total}")
    if player_total > 21:
        print("Busted!\nYou Lose!")
        restart()
    elif dealer_total > 21:
        print("Dealer busts! You Win!")
        restart()
    elif not cont_game:
        if dealer_total == player_total:
            print(f"Dealer stands with {dealer_total}")
            print("Push")
        elif dealer_total > player_total and player_total < 21:
            print(f"Dealer stands with {dealer_total}")
            print("You Lose!")
        elif dealer_total < player_total and dealer_total < 21:
            print(f"Dealer stands with {dealer_total}")
            print("You Win!")   
        restart()
## Inputs
def dealer_input(): ##
    input("Press enter to continue dealing ")

def player_input():
    return input("Press enter to Hit, or type 'stand': ").lower() 
    
def restart(): ##
    print("\n##################################################")
    start_game = input("\nPRESS ENTER TO PLAY AGAIN, TYPE EXIT TO TERMINATE").lower()
###############################################################
        ## Import, Start Game ##

import random
from replit import clear
from art import logo
start_game = ""

while start_game != "exit":
    ## Set variables
    cont_game = True
    cont_play = ""
    dealer_faces = []
    player_faces = []
    ## Draw first two cards for Dealer and Player
    dealer_faces.append(deal_card())
    dealer_total = calculate_total(dealer_faces)
    dealer_faces.append("X")
    for _ in range(2):
        player_faces.append(deal_card())
    player_total = calculate_total(player_faces)
    ## Check if Player has Blackjack and stand so they dont get locked into a 3rd card
    if player_total == 21:
        cont_play = "stand"
    else:
        update_ui()
        cont_play = player_input()    
###############################################################
        ## Player's turn ##        
        
    while cont_play != "stand":
        player_faces.append(deal_card())
        player_total = calculate_total(player_faces)
        ## Hit the Player until they stand, bust, or Blackjack
        if player_total > 21:
            cont_play = "stand"
            cont_game = False
            update_ui()
        elif player_total == 21:
            cont_play = "stand"
            update_ui()
        else:
            update_ui()
            cont_play = player_input()
###############################################################
        ## Dealer's turn ##
        
    if cont_game:
        update_ui()
        ## Reveal the dealer's second card
        dealer_faces.pop(1)
        ## Hit the Dealer until over 18 or they bust    
        while dealer_total < 17:
            dealer_input()
            dealer_faces.append(deal_card())
            dealer_total = calculate_total(dealer_faces)
            if dealer_total >= player_total:
                cont_game = False
                update_ui()
                break
            elif dealer_total > 21:
                cont_game = False
                update_ui()
            elif dealer_total == 21:
                cont_game = False
                update_ui()
            ## Stand if over 18 and not busted
            elif dealer_total >= 17:
                cont_game = False
                update_ui() 
            else:
                update_ui()
###############################################################
