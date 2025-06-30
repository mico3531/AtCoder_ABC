N, M, K = map(int,input().split())

ans = "No"
for x in range(N+1):
    for y in range(M+1):
        count = x*M + y*N - x*y*2
        if count == K:
            ans = "Yes"

print(ans)