class Stack:
    def __init__(self):
        self.items = []

    def push(self,num):
        self.items.append(int(num))

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items != []:
            return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []
    
    def __str__(self):
        return "Value in Stack =" + str(self.items)

S = Stack()
inp = input("Enter Input : ").split(",")
for i in range(len(inp)):
    try:
        key, num = inp[i].split()
    except:
        key = inp[i][0]
    if key == "A":
        if S.isEmpty():
            S.push(num)
        else:
            for j in range(S.size()):
                if int(num) >= int(S.peek()):
                    S.pop()
            S.push(num)

    elif key == "B":
        print(S.size())