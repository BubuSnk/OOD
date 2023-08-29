class queue:
    def __init__(self,list = None):
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
    
q1 = queue()
q2 = queue()
qMain = queue()
count = 0
people = input("Enter people : ")

for i in people:
    qMain.enQueue(i)

while not qMain.isEmpty():
    count += 1
    if count % 3 == 1 and count >= 3:
        q1.deQueue()
    if count % 2 == 0 and q2.size() > 1:
        q2.deQueue()
    if q1.size() < 5:
        q1.enQueue(qMain.deQueue())
    elif q2.size() < 5:
        q2.enQueue(qMain.deQueue())
    print(f'{count} {qMain.items} {q1.items} {q2.items}')