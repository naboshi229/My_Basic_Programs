import os
import sys

from Blind_Auction_ART import logo
print(logo)

Bids = {}
Bidding_Finished = False
def Find_Highest_Bidder(Bidding_Record):
    Highest_Bid = 0
    Winner = ""
    for Bidder in Bidding_Record:
        Bid_Amount = Bidding_Record[Bidder]
        if Bid_Amount > Highest_Bid:
            Highest_Bid = Bid_Amount
            Winner = Bidder
    print(f"The winner is {Winner} with a bid of ${Highest_Bid}!\n")
    input("(Press enter to close the program)")

while not Bidding_Finished:
    Name = input("What is your name?: ")
    Price = int(input("What is your bid?: $"))
    Bids[Name] = Price
    Should_Continue = input('Are there any other bidders? Type "y" or "n": ')
    if Should_Continue == "n":
        Bidding_Finished = True
        Find_Highest_Bidder(Bids)
    elif Should_Continue == "y":
        os.system('cls')
