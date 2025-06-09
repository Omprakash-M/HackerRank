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
    def swap(self,k,n):
        i=1
        temp=self.head
        temp1=0
        temp2=0
        while temp :
            if i==k:
                temp1=temp.data
            if i==n-k+1:
                temp2=temp.data
            temp=temp.next
            i+=1
        temp=self.head
        i=1
        while temp :
            if i==k:
                temp.data=temp2
            if i==n-k+1:
                temp.data=temp1
            temp=temp.next
            i+=1
            
    def printll(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
N=int(input())
ll1=ll()
data=input().split(" ")
for n in data:
    ll1.insert(n)
k=int(input())
ll1.swap(k,N)
ll1.printll()
