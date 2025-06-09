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
    def insertat(self,data,k):
        temp=self.head
        i=1
        while temp and i<k-1:
            temp=temp.next
            i+=1
        if not temp:
            print("Position out of range")
            return
        nn=node(data)
        if k==1:
            nn.next=temp
            self.head=nn
            return
        nn.next=temp.next
        temp.next=nn
    def printll(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
str=input()
ll1=ll()
nums=input().split(' ')
pos=int(input())
num=int(input())
for n in nums:
    ll1.insert(int(n))
ll1.insertat(num,pos)
ll1.printll()
