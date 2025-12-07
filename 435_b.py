N = int(input())
A = list(map(int, input().split()))

ans = 0
for l in range(N):
    for r in range(l+1, N+1):
        total_num = 0
        for i in range(l, r):
            total_num += A[i]
        check = True
        for i in range(l, r):
            if total_num % A[i] == 0:
                check = False
        if check:
            ans += 1

print(ans)