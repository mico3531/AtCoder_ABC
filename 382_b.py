N, D = map(int,input().split())
S = list((input()))

for i in range(N-1, -1, -1):
    if S[i] == "@" and D > 0:
        S[i] = "."
        D -= 1

print("".join(S))