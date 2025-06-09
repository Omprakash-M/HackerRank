from collections import deque
class node:
    def __init__(self,data):
        self.data=data
        self.r=None
        self.l=None
n=int(input())
arr=input().split()
arr1=[]
for x in arr:
    if int(x)==-1:
        arr1.append(None)
    if x.isdigit():
        arr1.append(int(x))
    
def insert(arr):
    if not arr or arr[0] is None:
        return
    root=node(arr[0])
    i=1
    q=deque()
    q.append(root)
    while q:
        curr = q.popleft()
        if i<len(arr) and arr[i] is not None:
            curr.l = node(arr[i])
            q.append(curr.l)
        i+=1
        if i<len(arr) and arr[i] is not None:
            curr.r=node(arr[i])
            q.append(curr.r)
        i+=1
    return root
root=insert(arr1)
def bfs(root):
    if root is None:
        return
    q=deque([root])
    while q:
        curr=q.popleft()
        print(curr.data,end=" ")
        if curr.l:
            q.append(curr.l)
        if curr.r:
            q.append(curr.r)
def inorder(root):
    if root is None:
        return
    inorder(root.l)
    print(root.data ,end=" ")
    inorder(root.r)
def preorder(root):
    if root is None:
        return 0
    return 1 + preorder(root.l) + preorder(root.r)

c = preorder(root)
print(c)
