N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

D.sort()
T.sort()

i = 0
j = 0
while i < N and j < M:
    if D[i] == T[j]:
        j += 1
    i += 1

if j == M:
    print("YES")
else:
    print("NO")