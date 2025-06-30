import copy

N = int(input())
A = list(map(int,input().split()))
S = str(input())

L = [[0,0,0] for _ in range(N)]
for i in range(1, N):
    L[i] = copy.copy(L[i-1])
    if S[i-1] == "M":
        L[i][A[i-1]] += 1

R = [[0,0,0] for _ in range(N)]
for i in range(N-2, -1, -1):
    R[i] = copy.copy(R[i+1])
    if S[i+1] == "X":
        R[i][A[i+1]] += 1

ans = 0
for i in range(N):
    if S[i] == "E":
        x = A[i]
        for t in range(3):
            for u in range(3):
                num = 0
                while num in [x, t, u]:
                    num += 1
                ans += num * L[i][t] * R[i][u]

# print(L)
# print(R)
print(ans)