def solve():
    N, H = map(int, input().split())
    
    T = [0 for _ in range(N)]
    L = [0 for _ in range(N)]
    U = [0 for _ in range(N)]
    for i in range(N):
        T[i], L[i], U[i] = list(map(int, input().split()))
    
    time = 0
    lower = H
    upper = H
    for i in range(N):
        last_time = T[i] - time
        lower -= last_time
        upper += last_time
        if max(lower, L[i]) <= min(upper, U[i]):
            lower = max(lower, L[i])
            upper = min(upper, U[i])
            time = T[i]
        else:
            print("No")
            return 0
    
    print("Yes")
    return 0

T = int(input())
for _ in range(T):
    solve()