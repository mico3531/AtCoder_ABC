S = str(input())
ls = [0, 0, 0]

for i in range(len(S)):
    if S[i] == "a":
        ls[0] += 1
    elif S[i] == "b":
        ls[1] += 1
    else:
        ls[2] += 1

if abs(ls[0]-ls[1]) >= 2 or abs(ls[1]-ls[2]) >= 2 or abs(ls[2]-ls[0]) >= 2:
    print("NO")
else:
    print("YES")
