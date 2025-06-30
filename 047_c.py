S = str(input())
N = len(S)

alp = S[0]

k = 1
for i in range(N):
    if S[i] != alp:
        k += 1
        alp = S[i]

print(k-1)