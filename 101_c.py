import math

N, K = map(int,input().split())
A = list(map(int,input().split()))

N -= 1
K -= 1

ans = math.ceil(N / K)

print(ans)