class Stack:
    def __init__(self,list=None):
        if list == None:
            self.item = []
        else :
            self.item = list
       
    def push(self,i):
        self.item.append(i)

    def pop(self):
        return self.item.pop()

    def isEmpty(self):
        return self.item == []

    def size(self):
        return int(len(self.item))

    def peek(self):
        return str(self.item[-1])


priority = {'+':1, '-':1, '*':2, '/':2,'^':3,'(':4} 


inp = input('Enter Infix : ')
S = []
print('Postfix : ', end='')

for i in range (len(inp)):
    if inp[i] in "()+-*/^":
        if inp[i] == '(':
            S.append(inp[i])
        elif inp[i] == ')':
            while S[-1] != '(':
                print(S.pop(),end="")
            S.pop()
        else :
            while (not S == [] and priority[inp[i]] <= priority[S[-1]]) and (S[-1] != '('):
                print(S.pop(),end="")
            S.append(inp[i])
    else:
        print(inp[i] , end='')

for i in range (len(S)) :
    print(S.pop(),end="")