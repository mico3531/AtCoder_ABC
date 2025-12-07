N = int(input())

P = [0 for _ in range(N)]
A = [0 for _ in range(N)]
B = [0 for _ in range(N)]

for i in range(N):
    P[i], A[i], B[i] = list(map(int, input().split()))

Q = int(input())