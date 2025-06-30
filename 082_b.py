S = sorted(input())
T = sorted(input())
T.reverse()

s = "".join(S)
t = "".join(T)

if s < t:
    print("Yes")
else:
    print("No")
