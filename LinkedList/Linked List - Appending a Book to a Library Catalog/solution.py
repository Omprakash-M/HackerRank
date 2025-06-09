class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
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
        nn.prev=temp
        temp.next=nn
    def printdll(self):
        temp=self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
N=int(input())
nums=input().split(" ")
dll1=DLL()
for n in nums:
    dll1.insert(int(n))
dll1.printdll()
