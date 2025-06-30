N, Q = map(int, input().split())
A = list(map(int, input().split()))

Ls = [0 for _ in range(N+2)]
count = 0
for i in range(Q):
    x = A[i]
    if Ls[x] == 0:
        Ls[x] = 1
        if Ls[x-1] + Ls[x+1] == 2:
            count -= 1
        elif Ls[x-1] + Ls[x+1] == 0:
            count += 1
    elif Ls[x] == 1:
        Ls[x] = 0
        if Ls[x-1] + Ls[x+1] == 2:
            count += 1
        elif Ls[x-1] + Ls[x+1] == 0:
            count -= 1
    print(count)