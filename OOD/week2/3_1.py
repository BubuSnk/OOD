class Stack():
    def __init__(self):
        self.items = []
        
    def push(self,num):
        self.items.append(int(num))
        self.items.sort()
        self.size = len(self.items)
        return f'Add = {num} and Size = {self.size} '
    
    def pop(self):
        if self.items == []:
            print('-1')
            return -1
        else:
            self.size = len(self.items)
            print(f"Pop = {self.items[-1]} and Index = {self.size-1}")
            self.items.pop()
            
     
st = Stack()
S = input("Enter Input : ").split(',')
for i in range(len(S)):
    try:
        key, num = S[i].split()
        #print(key,num)
    except:
        key = S[i][0]
    if key == 'A':
        print(st.push(num))
    elif key == 'P':
        st.pop()

if st.items == []:
    print('Value in Stack = Empty')
else :
    print('Value in Stack =' ,*st.items)