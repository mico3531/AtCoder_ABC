N, M = map(int,input().split())
P = list(map(int,input().split()))

def check(x):
    cost = 0
    count = 0
    for p in P:
        k = ((x/p) + 1) // 2
        cost += (k ** 2) * p
        count += k
    return [cost, count]

L = 0
R = 10 ** 15
while R - L >= 2:
    mid = (L+R) // 2
    if check(mid)[0] <= M:
        L = mid
    else:
        R = mid

cost, ans = check(L)
M -= cost
for p in P:
    if M < R:
        break
    if (p-R) % (2*p) == 0:
        ans += 1
        M -= R

print(int(ans))