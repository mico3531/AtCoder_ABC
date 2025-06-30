N, K = map(int,input().split())
R, S, P = map(int,input().split())
T = str(input())

Result = [0 for _ in range(N)]
Point = {"r":P, "s":R, "p":S}
ans = 0
for i in range(N):
    hand = T[i]
    if i < K:
        ans += Point[hand]
        Result[i] = 1
    else:
        if T[i-K] == hand and Result[i-K] == 1:
            Result[i] = -1
        else:
            ans += Point[hand]
            Result[i] = 1

print(ans)