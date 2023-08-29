class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    head = None
    for i in LL:
        newNode = Node(i)
        if(head == None):
            head = newNode
        else:
            now = head
            while now.next:
                now = now.next
            now.next = newNode
    return head

def printLL(head):
    sr = ""
    now = head
    while now:
        sr += str(now.value) + " "
        now = now.next
    return sr

def SIZE(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def nodeAt(head: Node, size):
    cur = head
    for _ in range(size):
        cur = cur.next
    return cur

def splitL(head: Node, numCut):
    before = nodeAt(head, numCut - 1)
    after = before.next
    before.next = None
    return after

def appendNode(head: Node, data: Node):
    if head is None:
        return data
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = data
    return head    

def bottomUp(head: Node, numCut, size):  
    if numCut == 0 or numCut == size:
        return head
    tail = nodeAt(head, size - 1)
    new_node = splitL(head, numCut)
    tail.next = head       
    return new_node

def riffle(head: Node, numCut):
    node2 = splitL(head, numCut)   
    new_node = None
    while head is not None or node2 is not None:
        if head is not None:
            temp = splitL(head, 1)
            head, temp = temp, head
            new_node = appendNode(new_node, temp)
        if node2 is not None:
            temp = splitL(node2, 1)
            node2, temp = temp, node2
            new_node = appendNode(new_node, temp)
    return new_node
    
def deRiffle(head: Node, collect, size):
    node1 = node2 = None
    while head is not None:
        if SIZE(node1) < collect:
            temp = splitL(head, 1)
            head, temp = temp, head
            node1 = appendNode(node1, temp)
        if SIZE(node2) < size - collect:
            temp = splitL(head, 1)
            head, temp = temp, head
            node2 = appendNode(node2, temp)
    nodeAt(node1, collect - 1).next = node2
    return node1

def scarmble(head, b, r, size):
    bottom_num = int(size * b / 100)
    rif_num = int(size * r / 100)

    head = bottomUp(head, bottom_num, size)
    print(f"BottomUp {b:.3f} % : {printLL(head)}")

    head = riffle(head, rif_num)
    print(f"Riffle {r:.3f} % : {printLL(head)}")

    head = deRiffle(head, rif_num, size)
    print(f"Deriffle {r:.3f} % : {printLL(head)}")

    head = bottomUp(head, size - bottom_num, size)
    print(f"Debottomup {b:.3f} % : {printLL(head)}")

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)