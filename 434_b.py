N, M = map(int, input().split())

ls_sum = [0 for _ in range(M)]
count = [0 for _ in range(M)]

for _ in range(N):
    A, B = map(int, input().split())
    ls_sum[A-1] += B
    count[A-1] += 1

for i in range(M):
    print(ls_sum[i] / count[i])