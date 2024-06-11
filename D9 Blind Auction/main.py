from replit import clear
from art import logo
print(logo)

bids = {}
still_bidding = "" #bidding_finished = False

def find_highest_bidder(): # def find_highest_bidder(bidding_record):
    #   highest_bid = 0
    winner = ""
    for bidder in bids: #   for bidder in bidding_record:
        bid_amount = bids[bidder]
        if winner == "":  ## delete
            winner = bidder  ## delete
        elif bids[bidder] > bids[winner]: #if bid_amount > highest_bid: 
            winner = bidder
            highest_bid = bid_amount
    results = "*"
    while results not in {""}:
        results = input("Hit enter to see the winner.\n").lower()
    print(f"The winner is {winner.capitalize()} with a bid of ${highest_bid}")

while still_bidding != "done": # while not bidding_finished:
    name = input("What is your name?\n")
    price = input("What is your bid?\n$")
    bids[name] = price
    still_bidding = input("\nHit enter to add more bids. Type \"done\" to finish.\n").lower()
    clear()    ## indent
    print(logo)

find_highest_bidder() #(bids)
