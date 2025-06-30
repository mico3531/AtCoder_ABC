import math

N = int(input())
A = list(map(int,input().split()))

ans = math.gcd(A[0], A[1])

for i in range(N):
    ans = math.gcd(ans, A[i])

print(ans)