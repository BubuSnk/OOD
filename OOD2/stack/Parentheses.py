def parentheses(inp):
    stack = []
    par = {"(":")","[":"]"}

    for char in inp:
        if char in par:
            stack.append(char)
        elif char in par.values():
            if stack == []:
                return False
            if par[stack[-1]] == char:
                stack.pop()
            else:
                return False

    return len(stack) == 0

inp = input("Enter Input : ")
if parentheses(inp):
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")