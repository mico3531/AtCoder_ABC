N = int(input())
A = list(map(int, input().split()))

Ans = [-1 for _ in range(N)]

if N >= 2:
    for i in range(1, N):
        for j in range(i):
            if A[i] < A[j]:
                Ans[i] = j + 1

for i in range(N):
    print(Ans[i])