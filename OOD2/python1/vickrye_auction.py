bid = input("Enter All Bid : ").split()
bidder = len(bid)

sorted_bid = sorted([int(b) for b in bid])

if bidder < 2:
    print("not enough bidder")
elif sorted_bid[bidder-1] == sorted_bid[bidder-2]:
    print("error : have more than one highest bid")
else:
    winner_bid = sorted_bid[bidder-1]
    second_highest_bid = sorted_bid[bidder-2]
    print(f"winner bid is {winner_bid} need to pay {second_highest_bid}")
