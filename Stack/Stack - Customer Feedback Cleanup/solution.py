s = input()
stack = list(s)

def find(stack):
    i = 0
    changed = False
    while i < len(stack) - 1:
        if stack[i] == stack[i + 1]:
            # Remove the adjacent duplicates
            del stack[i]
            del stack[i]  # same index since list shifts left
            changed = True
            # Step back one index to check for new adjacent duplicates
            if i > 0:
                i -= 1
        else:
            i += 1
    return changed

# Keep removing adjacent duplicates until no change occurs
while find(stack):
    pass
if "".join(stack):
    print("".join(stack))
else:
    print("Empty String")
