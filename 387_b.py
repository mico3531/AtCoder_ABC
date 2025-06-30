X = int(input())

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        if X != i*j:
            ans += i*j

print(ans)