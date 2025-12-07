N, A, B = map(int, input().split())
S = str(input())

S_1 = S[A:]
if B == 0:
    S_2 = S_1
else:
    S_2 = S_1[:-B]
print(S_2)