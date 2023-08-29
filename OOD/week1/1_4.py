def odd_list(al):    
    ood = []
    for als in al:
        if als %2 == 1:
            ood.append(als)
    return ood

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]

opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
