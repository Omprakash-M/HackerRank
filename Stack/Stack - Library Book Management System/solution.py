class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        nn=node(data)
        if self.head is None:
            self.head=nn
            return
        nn.next=self.head
        self.head=nn
    def printll(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
    def delfrombeg(self,k):
        i=1
        while i<=k and self.head:
            temp=self.head
            self.head=temp.next
            i+=1
    def top(self):
        print(self.head.data)
    def size(self):
        x=0
        temp=self.head
        while temp:
            x+=1
            temp=temp.next
        print(x)
    def isEmpty(self):
        if self.head== None:
            print("true")
        else:
            print("false")
n=int(input())
if n>100:
    pass
else:
    ll1=ll()
    for i in range(n):
        str=input()
        if "Push" in str:
            data=str.split()
            ll1.insertatbeg(data[1])
        elif "Pop" in str:
            ll1.delfrombeg(1)
        elif "Top" in str:
            ll1.top()
        elif "Is" in str:
            ll1.isEmpty()
        elif "Size" in str:
            ll1.size()
