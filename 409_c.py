N, L = map(int, input().split())
D = list(map(int, input().split()))

P = [0 for _ in range(N)]
for i in range(1, N):
    P[i] = P[i-1] + D[i-1]
    P[i] %= L
# print(P)

Count = [0 for _ in range(L)]
for p in P:
    Count[p] += 1
# print(Count)

ans = 0
if L % 3 == 0:
    tri_len = L // 3
    for i in range(tri_len):
        j = i + tri_len
        k = i + 2 * tri_len
        ans += Count[i] * Count[j] * Count[k]
print(ans)