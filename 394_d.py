from collections import deque

S = str(input())
N = len(S)

Stack = deque([])
check = True
for i in range(N):
    if S[i] in ["(", "[", "<"]:
        Stack.append(S[i])
    elif S[i] == ")":
        if len(Stack) > 0:
            x = Stack.pop()
            if x != "(":
                check = False
        else:
            check = False
    elif S[i] == "]":
        if len(Stack) > 0:
            x = Stack.pop()
            if x != "[":
                check = False
        else:
            check = False
    else:
        if len(Stack) > 0:
            x = Stack.pop()
            if x != "<":
                check = False
        else:
            check = False
    
    # print(Stack)

    if not check:
        break

if check and len(Stack) == 0:
    print("Yes")
else:
    print("No")