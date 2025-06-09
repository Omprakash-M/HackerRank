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
            self.head=nn
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=nn
    def printll(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
str=input()
ll1=ll()
nums=input().split(' ')
for n in nums:
    ll1.insert(int(n))
ll1.printll()
