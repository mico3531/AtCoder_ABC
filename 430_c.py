import bisect

N, A, B = map(int, input().split())
S = str(input())

a_count = [0 for _ in range(N+1)]
b_count = [0 for _ in range(N+1)]

for i in range(1, N+1):
    a_count[i] = a_count[i-1]
    b_count[i] = b_count[i-1]
    if S[i-1] == "a":
        a_count[i] += 1
    else:
        b_count[i] += 1

# print(a_count)
# print(b_count)

ans = 0
for i in range(N):
    a_dat = bisect.bisect_left(a_count, a_count[i] + A)
    b_dat = bisect.bisect_left(b_count, b_count[i] + B)
    # print(i, a_dat, b_dat)
    if a_dat < b_dat:
        ans += b_dat - a_dat

print(ans)