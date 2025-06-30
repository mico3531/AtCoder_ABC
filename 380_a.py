N = str(input())

Ls = [0,0,0]
for i in range(6):
    if N[i] == "1":
        Ls[0] += 1
    elif N[i] == "2":
        Ls[1] += 1
    elif N[i] == "3":
        Ls[2] += 1

if Ls == [1, 2, 3]:
    print("Yes")
else:
    print("No")