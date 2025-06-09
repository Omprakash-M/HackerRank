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
    def dlteat(self,k):
        temp=self.head
        i=1
        if k==1:
            self.head=self.head.next
            return
        while temp and i<k-1:
            temp=temp.next
            i+=1
        temp.next=temp.next.next

    def printll(self):
        temp=self.head
        if temp is None:
            print("List is empty")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
N=int(input())
ll1=ll()
if N!=0:
    nums=input().split(' ')
    x=int(input())
    if x>N:
        print("Position out of range")
    else:
        for n in nums:
            ll1.insert(int(n))
        ll1.dlteat(x)
        ll1.printll()
else:
    print("List is empty")

