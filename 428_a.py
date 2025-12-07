S, A, B, X = map(int, input().split())

ans = S * (X // (A+B)) * A
ans += S * min(X % (A+B), A)

print(ans)