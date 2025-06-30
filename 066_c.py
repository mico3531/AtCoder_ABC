N = int(input())
A = list(map(int,input().split()))

B = [0 for _ in range(N)]

k = N-1
i = 0
while k >= 0:
    B[i] = A[k]
    k -= 2
    i += 1

k = (N % 2)

while i < N:
    B[i] = A[k]
    k += 2
    i += 1

print(*B)