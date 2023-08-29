class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.next = None
        self.tail = None

    def __str__(self) -> str:
        if self.head == None:
            return "Empty"
        current = self.head.next
        out = str(self.head)
        while current is not None:
            out += "->" + (str(current))
            current = current.next
        return out

    def append(self,data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node

    def index(self,data):
        current = self.head
        for data in range(data):
            current = current.next
            if current.next == None:
                break
        return current

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def isEmpty(self):
        return self.head == None

L = SinglyLinkedList()
inp = input("Enter input : ").split(",")
check = False

for i in inp:
    i = i.split()

    if i[0] == "A":
        L.append(int(i[1]))
        print(L)

    if i[0] == "S":
        a = i[1].split(":")
        num0 = int(a[0])
        num1 = int(a[1])

        if L.isEmpty():
            print("Error! {list is empty}")

        elif num0 >= L.size() or num0 < 0:
            print("Error! {index not in length}:",num0)
            
        elif num1 >= L.size() or num1 < 0:
            print("index not in length, append :",num1)
            L.append(num1)

        else:
            b1 = L.index(num0)
            b2 = L.index(num1)
            b1.next = b2
            print(f"Set node.next complete!, index:value = {a[0]}:{b1.data} -> {a[1]}:{b2.data}")
            if num0 >= num1:
                check = True
if check:
    print("Found Loop")
else:
    print("No Loop")
    print(L)