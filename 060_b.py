A, B, C = map(int,input().split())

A %= B
ans = "NO"
for i in range(1, B+1):
    if (A * i) % B == C:
        ans = "YES"

print(ans)