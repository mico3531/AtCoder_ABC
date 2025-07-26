S = list(str(input()))

T = ["" for _ in range(len(S))]

check = True
for i in range(len(S)):
    if S[i] == "#":
        T[i] = "#"
        check = True
    else:
        if check:
            T[i] = "o"
            check = False
        else:
            T[i] = "."

print("".join(T))