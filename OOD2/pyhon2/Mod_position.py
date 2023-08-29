def mod_position(arr, s):
    result = []
    for i in range(len(arr)):
        if (i+1) % s == 0:
            result.append(arr[i])
    return result

print("*** Mod Position ***")
arr,s = input("Enter Input : ").split(",")
s = int(s)
result = mod_position(arr, s)
print(result)

