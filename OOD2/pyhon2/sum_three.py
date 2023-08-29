def find_sum_of_three(arr):
    n = len(arr)
    if n < 3:
        return "Array Input Length Must More Than 2"
    result = set()
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 5:
                    result.add(tuple(sorted([arr[i], arr[j], arr[k]])))
    return [list(x) for x in result]

arr = input("Enter Your List : ").split()
arr = [int(x) for x in arr]
result = find_sum_of_three(arr)
print(result)