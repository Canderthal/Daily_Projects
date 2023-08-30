import os
os.system('cls')

bidder = {}

print("Today we will be doing a silent auction on a first eddition mystery Pokemon card")
def new_bidder():
    name = input("What is your name?")
    value = int(input("How much are you bidding? $"))
    bidder[name] = value
    os.system("cls")

def top_bidder():
    winner = ""
    top_bid = 0
    for bid in bidder:
         if bidder[bid] > top_bid:
             top_bid = bidder[bid]
             winner = bid
    print(f"{winner} won with a bid of ${top_bid}")

bidding = True
while bidding:
    new_bidder()
    cont = input("Is there another bidder? yes or no.\n")
    if cont == "yes":
        new_bidder
    else:
        bidding = False
        top_bidder()
        