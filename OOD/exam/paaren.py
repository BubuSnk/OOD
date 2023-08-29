class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if self.size() > 0 else -1

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return 
        

op = "([{"
cl = ")]}"
s = Stack()    
inp = input("Enter expresion : ")
for i in inp:
    if i in op:
        s.push(i)
    elif i in cl:
        if s.isEmpty():
            print(" close paren excess")
            break
        elif op.index(s.peek()) != cl.index(i):
            print(" Unmatch open-close")
            break
        else:
            s.pop()

if not s.isEmpty():
    print(" open paren excess   {0} : ".format(s.size()), end= "")
    t = ""
    while not s.isEmpty():
        t += s.pop()
    print(t[::-1])
