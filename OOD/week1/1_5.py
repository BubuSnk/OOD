Bid = [int(e) for e in input("Enter All Bid : ").split()]
Bid.sort(reverse=True)
x = len(Bid)
if x<2:
    print("not enough bidder")
elif Bid[0] == Bid[1]:
    print("error : have more than one highest bid")
else:
    print("winner bid is",Bid[0],"need to pay",Bid[1])
