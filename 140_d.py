N, K = map(int,input().split())
S = str(input())

alp = "A"
count = 0
for i in range(N):
    if S[i] != alp:
        count += 1
        alp = S[i]

# print(count)
ans = N-count
ans += min(2*K, count-1)
print(ans)