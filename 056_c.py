X = int(input())

X = abs(X)
ans = 0

while ans * (ans + 1) //2 < X:
    ans += 1

print(ans)