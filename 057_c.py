import math

N = int(input())
K = math.ceil(math.sqrt(N))+3

def F(A, B):
    x = math.floor(math.log(A, 10)) + 1
    y = math.floor(math.log(B, 10)) + 1
    return max(x, y)

ans = 100
for i in range(1, K):
    if N % i == 0:
        A = i
        B = N // i
        ans = min(ans, F(A, B))

print(ans)