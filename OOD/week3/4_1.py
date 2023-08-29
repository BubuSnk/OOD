class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def enQueue(self,i):
        self.items.append(i)
   
    def deQueue(self):
        self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
   
    def size(self):
        return len(self.items)

q = Queue()    
inp = input('Enter Input : ').split(',')
for i in range(len(inp)):
    try:
        key, num = inp[i].split()
    except:
        key = inp[i][0]
    if key == 'E':
        q.enQueue(num)
        print(q.size())
    elif key == 'D':
        if not q.isEmpty():
            
            print(q.items[0] + " 0")
            q.deQueue()
        else:
            print('-1')
if not q.isEmpty():
    for i in q.items:
        print(i,end=' ')
else:
    print('Empty')