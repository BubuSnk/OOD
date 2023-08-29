class Stack:
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

s = Stack()
inp = input("Enter Color : ")
combo = 0
for ele in inp:
    s.push(ele)
    if s.size() >= 3:
        c1 = s.pop()
        c2 = s.pop()
        c3 = s.pop()
        if c1 == c2 == c3:
            combo += 1
        else:
            s.push(c3)
            s.push(c2)
            s.push(c1)
print("Color left : " + str(s.items))
print("Combo : " + str(combo))