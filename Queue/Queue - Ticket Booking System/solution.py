q=[]
x=int(input())
def enq(data):
    if len(q)>=x:
        print(f"Queue is full. Cannot add ({data})")
        return
    q.append(data)
def dq():
    if len(q)==0:
        print("Served Customer: Queue is empty. No customer to serve.")
        return
    print("Served Customer:", q.pop(0))
def disp():
    if len(q)==0:
        print("Queue is empty.")
        return
    print("Current Queue: ",end="")
    
    for x in q:
        print(x,end=" ")
    print()

y=int(input())
for _ in range(y):
    str=input()
    if " " in str:
        data=str.split()
        enq(data[1])
    elif "DIS" in str:
        disp()
    elif "DE" in str:
        dq()
