str=input()
stack=[]
for i in str:
    if i in "({[":
        stack.append(i)
    elif i in ")}]":
        if not stack:
            stack.append(i)
            break
        if i==")" and stack[-1]=="(":
            stack.pop()
        elif i=="}" and stack[-1]=="{":
            stack.pop()
        elif i=="]" and stack[-1]=="[":
            stack.pop()
        else:
            stack.append(i)
if len(stack)==0:
    #print(stack)
    print("true")
else:
    #print(stack)
    print("false")
