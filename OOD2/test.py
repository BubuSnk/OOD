def find_min(lst):
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        mid = len(lst)//2
        left_min = find_min(lst[:mid])
        right_min = find_min(lst[mid:])
        return left_min if left_min < right_min else right_min
    
inp = list(map(int,input("Enter Input : ").split()))
print(f"Min : {find_min(inp)}")