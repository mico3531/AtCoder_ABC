N = int(input())

ans = 0
for b in range(2, N):
    t = (N-b+1) // b
    k = b*t + 2*b - N - 1
    print(t, k)

print(ans)