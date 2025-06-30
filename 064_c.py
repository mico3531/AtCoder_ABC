N = int(input())
A = list(map(int,input().split()))

ls = [0 for _ in range(9)]

for i in range(N):
    if A[i] < 3200:
        ls[A[i] // 400] += 1
    else:
        ls[-1] += 1

ans = 0
for i in range(8):
    if ls[i] != 0:
        ans += 1

if ans == 0:
    print(1, ls[-1])
else:
    print(ans, ans + ls[-1])
