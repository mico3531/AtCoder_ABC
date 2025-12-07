N = int(input())

S = ["" for _ in range(N)]
for i in range(N):
    S[i] = str(input())

ls = list(map(str, input().split()))
X = int(ls[0])
Y = str(ls[1])

if S[X-1] == Y:
    print("Yes")
else:
    print("No")