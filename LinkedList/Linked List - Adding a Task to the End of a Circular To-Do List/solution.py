class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        nn=node(data)
        if self.head is None:
            nn.next=self.head
            self.head=nn
            return
        temp=self.head
        while temp.next is not None and temp.next!=self.head:
            temp=temp.next
        nn.next=self.head
        temp.next=nn
    def printll(self):
        temp=self.head
        if temp.next is None:
            print(temp.data,end=" ")
            return
        while temp and temp.next!=self.head:
            print(temp.data,end=" ")
            temp=temp.next
        print(temp.data,end=" ")
str=input()
ll1=ll()
nums=input().split(' ')
for n in nums:
    ll1.insert(int(n))
ll1.printll()
