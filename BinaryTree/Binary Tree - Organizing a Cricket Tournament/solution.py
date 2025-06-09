from collections import deque
class node:
    def __init__(self,data):
        self.data=data
        self.r=None
        self.l=None
n=int(input())
arr=list(map(int,input().split()))
#print(arr)
root=node(arr[0])
i=1
q=deque()
q.append(root)
while q:
    curr = q.popleft()
    #print(curr)
    if i<len(arr):
        curr.l = node(arr[i])
        q.append(curr.l)
    i+=1
    if i<len(arr):
        curr.r=node(arr[i])
        q.append(curr.r)
    i+=1
def bfs(root):
    if root is None:
        return
    q=deque([root])
    i=1
    while q:
        curr=q.popleft()
        print(curr.data,end=" ")
        if curr.l:
            q.append(curr.l)
        if curr.r:
            q.append(curr.r)
bfs(root)
