print("*** multiplication or sum ***")
a,b = input("Enter num1 num2 : ").split()
result1 = int(a)+int(b)
result2 = int(a)*int(b)

if result2>1000:
    print("The result is",result1)
else: print("The result is",result2)

