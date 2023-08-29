class stack:
    def __init__(self):
        self.items = []

    def __str__(self) -> str:
        return " ".join(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def bottom(self):
        return self.items[0]


def postFixCalc(inp: str):
    s = stack()
    for ele in inp:
        if ele not in "+-*/":
            s.push(int(ele))
        else:
            b = s.pop()
            a = s.pop()
            if ele == "+":
                s.push(a+b)
            elif ele == "-":
                s.push(a-b)
            elif ele == "*":
                s.push(a*b)
            elif ele == "/":
                s.push(a/b)
    return s.bottom()

print(" ***Postfix expression calculation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ", '{:.2f}'.format(postFixCalc(token)))