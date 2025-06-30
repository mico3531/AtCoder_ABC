S = str(input())
N = len(S)
Ls = list(S)
# print(Ls)
for i in range(N-2, -1, -1):
    if Ls[i] == "W" and Ls[i+1] == "A":
        Ls[i] = "A"
        Ls[i+1] = "C"

print("".join(Ls))