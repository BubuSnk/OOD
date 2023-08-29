class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
   
    def enQueue(self,i):
        self.items.append(i)
  
    def deQueue(self):
        return self.items.pop(0)
  
    def isEmpty(self):
        return self.items == []
  
    def size(self):
        return len(self.items)
    
q1 = Queue()
q2 = Queue()  
code,hint = input('Enter code,hint : ').split(',')
for i in code:
    q1.enQueue(i)
    
x = ord(hint)-ord(q1.items[0])
if x < 0:
    x = x*(-1)
for j in q1.items:
    if ord(hint) > ord(q1.items[0]):
        q2.enQueue(chr(ord(j)+x))
    else:
        q2.enQueue(chr(ord(j)-x))
    print(q2.items)