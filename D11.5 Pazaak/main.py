import random
#from replit import clear
import os
clear = lambda: os.system('clear')

print("Pazaak")
main = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
side = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6]

# UI
def update_ui():
    clear()
    print(f"User score: {user_score}")
    print(f"Computer score: {comp_score}")
    print(f"\nComp total: {sum(comp_board)}")
    print(f"comp board: {comp_board}")
    print(f"Comp hand: {comp_hand}")
    # comp_disp = []
    # for i in range(len(comp_hand)):
    #     comp_disp.append("X")
    # print(f"Comp hand: {comp_disp}")
    print(f"\nUser total: {sum(user_board)}")
    print(f"User board: {user_board}")
    print(f"\nUser hand: {user_hand}\n")

    if cont_user == "stand":
        if user_score > 20:
            print("You busted")
        else:    
            print(f"You stand with {sum(user_board)}")
    if cont_comp == "stand":
        if comp_score > 20:
            print("Computer busted")
        else:
            print(f"Computer stands with {sum(comp_board)}")

def card_choice(hand, board):
    card = int(input("Type a card from your hand: "))
    if card in hand:
        symbol = ""
        while symbol != "-" and symbol != "+":
            symbol = input("Type + or - to add or subtract it: ")
        hand.remove(card)
        if symbol == "-":
            card *= -1
            board.append(card)
        if symbol == "+":
            board.append(card)
        # cont = input("Enter to pass or 2 to stand: ")
        # if cont == "2":
        return "stand"
    else:
        card_choice(hand, board)

def user_turn():
    user_board.append(random.choice(main))
    if sum(user_board) == 20:
        return "stand"
    update_ui()
    choice = input("Press enter to pass, 1 to play a card from your hand, or 2 to stand: ")
    if choice == "1":
        return card_choice(user_hand, user_board)
    elif choice == "2":
        return "stand"


def comp_turn():
    comp_board.append(random.choice(main))
    update_ui()
    total = sum(comp_board)  
    if sum(user_board) <= sum(comp_board) and cont_user == "stand":
        return "stand"
    # if total < 18 or total > 20:
    for i in comp_hand:
        check_add = i + sum(comp_board)
        check_sub = i - sum(comp_board)
        if check_add == 20 and check_add >= sum(user_board):
            comp_hand.remove(i)
            comp_board.append(i)
            update_ui()
            input("Computer plays a card from hand. Press enter")
            break 
        elif check_add == 19 and check_add >= sum(user_board):
            comp_hand.remove(i)
            comp_board.append(i)
            update_ui()
            input("Computer plays a card from hand. Press enter")
            break 
        elif check_sub == 20 and check_sub >= sum(user_board):
            comp_hand.remmove(i)
            flip = i * -1
            comp_board.append(flip)
            update_ui()
            input("Computer plays a card from hand. Press enter")
            break
        elif check_sub == 19 and check_sub >= sum(user_board):
            comp_hand.remmove(i)
            flip = i * -1
            comp_board.append(flip)
            update_ui()
            input("Computer plays a card from hand. Press enter")
            break
        elif check_sub == 18 and check_sub >= sum(user_board):
            comp_hand.remmove(i)
            flip = i * -1
            comp_board.append(flip)
            update_ui()
            input("Computer plays a card from hand. Press enter")
            break
        
            #apply that card
    total = sum(comp_board) 
    if total >= 18 and total <= 20 and total >= sum(user_board):
        return "stand"
    return ""

def compare():
    global user_score
    global comp_score
    if sum(comp_board) > 20:
        user_score += 1
        update_ui()
        print("You win the round")
    if sum(user_board) > 20:
        comp_score += 1
        update_ui()
        print("You lose the round")
    if sum(user_board) == sum(comp_board):
        update_ui()
        print("You draw. No points awarded")
    elif sum(user_board) > sum(comp_board) and sum(user_board) <= 20:
        user_score += 1
        update_ui()
        print("You win the round")                
    elif sum(user_board) < sum(comp_board) and sum(comp_board) <= 20:
        comp_score += 1
        update_ui()
        print("You lose the round")


while True:
    input("Press enter to begin the game ")
    user_score = 0
    comp_score = 0
    user_hand = []
    comp_hand = []
    for _ in range(4):
        user_hand.append(random.choice(side))
        comp_hand.append(random.choice(side))
        
    while True:
        comp_board = []
        user_board = []
        cont_user = ""
        cont_comp = "" 
        update_ui()
        input("Press enter to begin the round and draw a card ")
        
        while cont_user != "stand" or cont_comp != "stand":
            # User turn
            if cont_user != "stand":
                # input("Press enter to draw yourself a card ")
                cont_user = user_turn()
                if sum(user_board) > 20:
                    cont_user = "stand"
                    cont_comp = "stand"
                    break
            update_ui()
            # Computer turn
            if cont_comp != "stand":
                input("Press enter to draw the computer a card ")
                cont_comp = comp_turn()
                if sum(comp_board) > 20:
                    cont_user = "stand"
                    cont_comp = "stand"
                    break
                if cont_user != "stand":
                    input("Press enter to draw a card ")
 
        # Compare totals
        if cont_user == "stand" and cont_comp == "stand":
            compare()
            update_ui()

                
        if user_score == 3:
            input("You win the game! Press enter to play another")
            break
        elif comp_score == 3:
            input("You lose the game! Press enter to play another")
            break
        input("Press enter to begin the next round ")
