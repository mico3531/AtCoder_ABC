R, G, B, N = map(int,input().split())

ans = 0

for i in range(1 + (N // R)):
    M = N - i * R
    for j in range(1 + (M // G)):
        L = M - j * G
        if L % B == 0:
            ans += 1

print(ans)