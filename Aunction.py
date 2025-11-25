bidder_data={}
end_of_bidding=false
def find_winner(bidder_details):
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(f"The winner is {winner} with a bid of ₹{highest_bid}")

        
while not end_of_bidding:
    name=input("enter the name :")
    price=int(input("enter the bid :"))
    bidder_data[name]=price
    more_bidders=input("Are there more bidders? Type 'Yes' or 'No' :").lower()
    if more_bidders == 'no':
        end_of_bidding=True
        find_winner(bidder_data)