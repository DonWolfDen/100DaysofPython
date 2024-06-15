###############################################################
        ## Define Functions ##

def deal_card():
    
    '''Draw a card'''
    faces = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    return faces[random.randint(0, len(faces)-1)]  
    
def calculate_total(target):
    '''Calculate totals'''
    faces = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "X"]
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 0]
    cards = []
    cards += target
    for i in range(len(target)):
        cards[i] = deck[faces.index(cards[i])] # % 13
    for _ in range(len(cards)):
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)#pop(cards.index(11))
            cards.append(1)
    return sum(cards)    


def update_ui():
    '''Keep ui clean, check Blackjack and declare winners'''
    global bet
    global pool 
    clear()
    print(logo)
    print(f"Cash in hand: ${pool}")
    print(f"Current bet: ${bet}\n")
    print(f"Dealer's hand: {dealer_faces}\nDealer's total: {dealer_total}\n")
    print(f"Your hand: {player_faces}\nYour total: {player_total}\n")
    if player_total == 21 and len(player_faces) == 2:
        print("Blackjack!")
    if dealer_total == 21 and len(dealer_faces) == 2:
        print("Dealer has Blackjack!")
    if cont_play == "stand" and player_total <= 21:
        print(f"You stand with {player_total}")
    if player_total > 21:
        print("Busted!")
        print(f"You lose your bet of {bet}")
        restart()
    elif dealer_total > 21:
        print("Dealer busts!")
        print(f"You Win {bet*2}!")
        pool += bet * 2
        restart()
    elif not cont_game:
        if dealer_total == player_total:
            print(f"Dealer stands with {dealer_total}")
            print("Draw")
            print(f"Dealer pushes your bet of {bet} back to you")
            pool += bet
        elif dealer_total > player_total and player_total < 21:
            print(f"Dealer stands with {dealer_total}")
            print(f"You lose your bet of {bet}")
        elif dealer_total < player_total and dealer_total < 21:
            print(f"Dealer stands with {dealer_total}")
            print(f"You Win {bet*2}!")
            pool += bet * 2
        restart()
## Inputs
        
def place_bet():
    while True:
        bet = input(f"Cash in hand: ${pool}\nPlace your bet: $")
        if bet.isdigit():
            bet = float(bet)
            if bet <= pool:
                break
            elif bet > pool or bet < 0:
                print(f"Invalid bet. You cannot bet more than you have or less than 0")
        elif not bet.isdigit():
            print(f"You cannot bet letters or symbols\nTo bet nothing, enter 0")
    return bet
        
def dealer_input():
    input("Press enter to continue dealing ")

def player_input():
    return input("Press enter to Hit, or type 'stand': ").lower() 
    
def restart():
    global start_game
    print("\n##################################################\n")
    if pool == 0:
        print("You died")
        start_game = 'exit'
    else:
        start_game = input("\nPress enter to place another bet. Type 'exit' to cash out ").lower()
    
###############################################################
        ## Import, Start Game ##

import random
from replit import clear
from art import logo #, faces

while True:
    pool = 1000.00
    start_game = ""
    while start_game != "exit":
        clear()
        #print(logo)
        bet = place_bet()
        pool -= bet
        cont_game = True
        cont_play = ""
        dealer_faces = []
        player_faces = []
        dealer_faces.append(deal_card())
        dealer_total = calculate_total(dealer_faces)
        dealer_faces.append("X")
        for _ in range(2):
            player_faces.append(deal_card())
        player_total = calculate_total(player_faces)
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
            dealer_faces.pop(1)
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
                elif dealer_total >= 17:
                    cont_game = False
                    update_ui() 
                else:
                    update_ui()
    if pool != 0:    
        print(f"You cash out with ${pool}")
    input("Press enter to buy in for $1000")
###############################################################
