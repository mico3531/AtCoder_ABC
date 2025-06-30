S = str(input())
count = 0
for i in range(len(S)):
    if S[i] == "2":
        count += 1

print("2"*count)