print(" *** Summation of each digit ***")
num = int(input("Enter a positive number : "))
sum = 0

while num > 0:
    digit = num % 10
    sum  += digit
    num //= 10

print(f"Summation of each digit =  {sum}")

