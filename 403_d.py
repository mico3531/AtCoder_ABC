import bisect

N, D = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
Used = [False for _ in range(N)]
# print(A)

def DP(array):
    L = len(array)
    DP = [[0,0] for _ in range(L)]
    DP[0][1] = array[0]
    for t in range(1, L):
        DP[t][0] = max(DP[t-1])
        DP[t][1] = DP[t-1][0] + array[t]
    # print(DP)
    return sum(array) - max(DP[-1])

if D == 0:
    num_set = set(A)
    ans = N - len(set(A))
else:
    ans = 0
    for i in range(N):
        if Used[i] == False:
            num = A[i]
            Ls = []
            while True:
                l = bisect.bisect_left(A, num)
                r = bisect.bisect_right(A, num)
                if l == r:
                    break
                Ls.append(r-l)
                for j in range(l, r):
                    Used[j] = True
                num += D
            ans += DP(Ls)

print(ans)