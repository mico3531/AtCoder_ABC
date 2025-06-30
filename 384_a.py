N, c_1, c_2 = map(str,input().split())
S = list(str(input()))
N = int(N)
# print(c_1, c_2)
# print(S)

for i in range(N):
    if S[i] != c_1:
        S[i] = c_2

print("".join(S))