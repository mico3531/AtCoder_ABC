N = int(input())
S = ["" for _ in range(N)]
for i in range(N):
    S[i] = str(input())

str_set = set()
for i in range(N):
    for j in range(N):
        if i != j:
            str_set.add(S[i] + S[j])

print(len(str_set))