import bisect

A, B, Q = map(int,input().split())

Shrine = [int(input()) for _ in range(A)]
Temple = [int(input()) for _ in range(B)]

# print(Shrine)
# print(Temple)

for _ in range(Q):
    x = int(input())
    ans = float("INF")

    s_ind = bisect.bisect_left(Shrine, x)
    Ls_s = [s_ind, s_ind - 1]
    
    for s in Ls_s:
        if 0 <= s and s < A:
            t_ind = bisect.bisect_left(Temple, Shrine[s])
            Ls_t = [t_ind, t_ind - 1]
            for t in Ls_t:
                if 0 <= t and t < B:
                    dist = abs(x - Shrine[s]) + abs(Shrine[s] - Temple[t])
                    ans = min(ans, dist)
    
    t_ind = bisect.bisect_left(Temple, x)
    Ls_t = [t_ind, t_ind - 1]

    for t in Ls_t:
        if 0 <= t and t < B:
            s_ind = bisect.bisect_left(Shrine, Temple[t])
            Ls_s = [s_ind, s_ind - 1]
            for s in Ls_s:
                if 0 <= s and s < A:
                    dist = abs(x - Temple[t]) + abs(Temple[t] - Shrine[s])
                    ans = min(ans, dist)
    
    print(ans)