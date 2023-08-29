class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def push(self,i):
        self.items.append(i)
        
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else: return '-1'
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
inp = input('Enter Input : ').split()
S = Stack()
count = 0
for n in range(len(inp)):
    if S.size() < 2:
        S.push(inp[n])
    elif inp[n] == S.peek() and S.peek() == S.items[-2]:
        S.pop()
        S.pop()
        count += 1
    else:
        S.push(inp[n])
print(S.size())
if not S.isEmpty():
    while not S.isEmpty():
        print(S.pop(),end='')
    print()
else: print('Empty')
if count > 1:
    print(f'Combo : {count} ! ! !')
