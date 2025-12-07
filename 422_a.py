S = str(input())
i = int(S[0])
j = int(S[2])

if j == 8:
    i += 1
    j = 1
else:
    j += 1

print(str(i) + "-" + str(j))