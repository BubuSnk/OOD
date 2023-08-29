class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data}'

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        if self.head == None:
            return ''
        current = self.head.next
        out = str(self.head)
        while current is not None:
            out += ' <- ' + (str(current))
            current = current.next
        return out

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def moveHead(self):
        if self.head.data == 0:
            return

        current = self.head
        while current.next.data != 0:
            current = current.next

        self.tail.next = self.head
        self.tail = self.head
        self.head = current.next
        self.tail = current
        current.next = None

print(' *** Locomotive ***')
n = input("Enter Input : ").split()
link = LinkedList()
for i in n:
    link.append(int(i))

print(f"Before : {link}")
link.moveHead()
print(f"After : {link}")

