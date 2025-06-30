N, S = map(int, input().split())
T = [0] + list(map(int, input().split()))

ans = "Yes"
for i in range(1, N+1):
    if T[i] - T[i-1] > S:
        ans = "No"

print(ans)