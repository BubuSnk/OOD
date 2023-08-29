class Queue:
    def __init__(self):
        self.items=[]
   
    def enQueue(self,num):
        for val in self.items[-1::-1]:
            if num[0] == val[0]:
                if self.items.index(val) == self.size() - 1:
                    break
                self.items.insert(self.items.index(val) + 1, num)
                return
        self.items.append(num)
   
    def deQueue(self):
        return self.items.pop(0)
   
    def size(self):
        return len(self.items)
   
    def isEmpty(self):
        if len(self.items)!=0:
            return False
        else:
            return True

id,op = input('Enter Input : ').split('/')
lst = dict()
for i in id.split(','):
    i = i.split()
    lst[i[1]] = i[0]
queue = Queue()
for d in op.split(','):
    d = d.split()
    if d[0] == 'D':
        if queue.isEmpty():
            print("Empty")
        else:
            print(int(queue.deQueue()[1]))
    elif d[0] == 'E':
        d[0] = lst[d[1]]
        queue.enQueue(d)