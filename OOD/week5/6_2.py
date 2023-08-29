def isPalindrome(n):
    x = n.upper()
    y = x.isalpha()
    return y == y[::-1]

input = input("Enter Input : ")
if(isPalindrome(input)):
    print(f'\'{input}\' is palindrome')
else:
    print(f'\'{input}\' is not palindrome')