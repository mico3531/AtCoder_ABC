N, Q = map(int,input().split())

ans = 0
Lhand = 1
Rhand = 2
for i in range(Q):
    H, S = map(str,input().split())
    T = int(S)

    if H == "L":
        m = min(T, Lhand)
        M = max(T, Lhand)
        if m < Rhand and Rhand < M:
            ans += (m - M + N)
        else:
            ans += (M - m)
        Lhand = T
    else:
        m = min(T, Rhand)
        M = max(T, Rhand)
        if m < Lhand and Lhand < M:
            ans += (m - M + N)
        else:
            ans += (M - m)
        Rhand = T

print(ans)