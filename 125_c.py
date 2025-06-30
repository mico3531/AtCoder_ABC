import math

N = int(input())

A = list(map(int,input().split()))

if N > 2:
    L_gcd = [A[0] for _ in range(N)] #i以前のgcd
    for i in range(1, N):
        L_gcd[i] = math.gcd(L_gcd[i-1], A[i])

    R_gcd = [A[N-1] for _ in range(N)] #i以降のgcd
    for i in range(N-2, -1, -1):
        R_gcd[i] = math.gcd(R_gcd[i+1], A[i])
    
    Ls_g = [0 for _ in range(N)]
    Ls_g[0] = R_gcd[1]
    Ls_g[N-1] = L_gcd[N-2]
    for i in range(1, N-1):
        Ls_g[i] = math.gcd(L_gcd[i-1], R_gcd[i+1])
    ans = max(Ls_g)
else:
    ans = max(A[0], A[1])

print(ans)