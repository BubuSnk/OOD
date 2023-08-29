class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None :
            self.root = Node(data)
            return self.root
        temp = self.root
        while 1 :
            if data < temp.data :
                if temp.left is None :
                    temp.left = Node(data)
                    break
                else :
                    temp = temp.left
            else :
                if temp.right is None :
                    temp.right = Node(data)
                    break
                else :
                    temp = temp.right
        return self.root

    def searchBelow(self,data,node,found):
        if node != None :
            if node.data < data :
                found = True
                self.searchBelow(data,node.left,found) 
                print(node.data,end = " ")
                self.searchBelow(data,node.right,found)
            else :
                self.searchBelow(data,node.left,found) 
        if not found and node is None:
            print("Not have")

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split("|")
data = [int(i) for i in inp[0].split()]
for i in data:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
print("Below " + inp[1] + " : ",end="")
found = False 
T.searchBelow(int(inp[1]),root,found)