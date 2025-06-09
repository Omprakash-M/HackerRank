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
    def reverse(self):
        prev=None
        temp=self.head
        while temp:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head=prev
    def printll(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
N=int(input())
ll1=ll()
data=[]
for i in range(N):
    data.append(input())
for n in data:
    ll1.insert(n)
ll1.reverse()
ll1.printll()
