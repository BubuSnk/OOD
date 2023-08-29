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
qMain = Queue()
people,minute = input('Enter people and time : ').split()

count = 0

for i in people:
    qMain.enQueue(i)

for min in range(1,int(minute)+1):
    if min % 3 == 1 and min >=3:
        q1.deQueue()
    if count % 2 == 0 and q2.size() > 1:
        q2.deQueue()  
    if not q1.size() >= 5:
        if not qMain.isEmpty():
            q1.enQueue(qMain.deQueue())
    elif not q2.size() >= 5:
        if not qMain.isEmpty():
            q2.enQueue(qMain.deQueue())
    if not q2.isEmpty():
        count +=1
    else:
        count = 0 
    print(min,end=(' '))
    print(f'{qMain.items} {q1.items} {q2.items}')