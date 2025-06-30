N = int(input())
D = [[] for _ in range(N)]
for i in range(N-1):
    D[i] = [0] * (i+1) + list(map(int,input().split()))
D[N-1] = [0] * N

# for i in range(N):
#     print(D[i])

DP = [0 for _ in range(2**N)]
for i in range(2**N):
    for j in range(N-1):
        for k in range(j+1, N):
            if (i >> j) & 1 and (i >> k) & 1:
                # print(bin(i), j, k, D[j][k])
                t = i - (2**j) - (2**k)
                DP[i] = max(DP[i], DP[t] + D[j][k])

print(DP[2**N - 1])