def find_min(lst):
    # base case: if the list is empty, return None
    if not lst:
        return None
    # base case: if the list has only one element, return that element
    if len(lst) == 1:
        return lst[0]
    # recursive case: divide the list in two halves and find the minimum of each half
    # then return the minimum of the two
    else:
        mid = len(lst) // 2
        left_min = find_min(lst[:mid])
        right_min = find_min(lst[mid:])
        return left_min if left_min < right_min else right_min

my_list = list(map(int, input("Enter Input : ").split()))
print("Min :", find_min(my_list))