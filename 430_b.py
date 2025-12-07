N, M = map(int, input().split())

S = ["" for _ in range(N)]
for i in range(N):
    S[i] = str(input())

pat = set()

for i in range(N-M+1):
    for j in range(N-M+1):
        str_data = ""
        for t in range(M):
            str_data += S[i+t][j:j+M]
        pat.add(str_data)

# print(pat)
print(len(pat))