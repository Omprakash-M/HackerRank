from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None

# Function to construct tree from level order input
def insert(arr):
    if not arr or arr[0] is None:
        return None
    root = Node(arr[0])
    q = deque([root])
    i = 1
    while i < len(arr):
        current = q.popleft()
        if i < len(arr) and arr[i] is not None:
            current.l = Node(arr[i])
            q.append(current.l)
        i += 1
        if i < len(arr) and arr[i] is not None:
            current.r = Node(arr[i])
            q.append(current.r)
        i += 1
    return root

# Function to sum all left leaves
def sum_of_left_leaves(root):
    if root is None:
        return 0
    total = 0
    if root.l and root.l.l is None and root.l.r is None:
        total += root.l.data
    total += sum_of_left_leaves(root.l)
    total += sum_of_left_leaves(root.r)
    return total

# Reading input
n = int(input())
arr = input().split()
arr1 = []
for x in arr:
    if x == "null":
        arr1.append(None)
    else:
        arr1.append(int(x))

# Build tree and compute result
root = insert(arr1)
print(sum_of_left_leaves(root))
