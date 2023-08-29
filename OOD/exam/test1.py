class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,num):
        self.items.append(num)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return " ".join(self.items)

s = Stack()
combo = 0
inp = input("Enter color :")
for e in inp:
    s.push(e)
    if s.size >= 3:
        c1 = s.pop()
        c2 = s.pop()
        c3 = s.pop()
        if c1 == c2 == c3:
            combo += 1
        else:
            s.push(c3)
            s.push(c2)
            s.push(c1)

for i in range(len(s)):
    try:
        key,num = s[i].split()
    except:
        key = s[i][0]

def postfixcal(int):
    