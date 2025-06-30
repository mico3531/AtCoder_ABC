N = int(input())
S = [0 for _ in range(N)]

for i in range(N):
    S[i] = int(input())

if sum(S) % 10 != 0:
    print(sum(S))
else:
    min = 101
    for i in range(N):
        if S[i] < min and (sum(S) - S[i]) % 10 != 0:
            min = S[i]
    if min < 101:
        print(sum(S) - min)
    else:
        print(0)