N = int(input())
H = list(map(int,input().split()))

ans = 1
for d in range(1, N):
    for L in range(d):
        x = L
        count = 1
        while x+d < N:
            if H[x] == H[x+d]:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
            x += d

print(ans)