def rev(list,reverse) :
    if len(list)==0 :
        return reverse
    else :
        reverse.append(max(list))
        maxindex = list.index(max(list))
        list.pop(maxindex)
        return rev(list,reverse)

inp = input("Enter your List : ").split(",")
for i in range(len(inp)) :
    inp[i] = int(inp[i])
inpre = []
print(f"List after Sorted : {rev(inp,inpre)}")