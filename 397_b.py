S = str(input())

count = 0
for i in range(len(S)):
    if count % 2 == 0:
        if i % 2 == 0:
            if S[i] == "o":
                count += 1
        else:
            if S[i] == "i":
                count += 1
    else:
        if i % 2 == 0:
            if S[i] == "i":
                count += 1
        else:
            if S[i] == "o":
                count += 1

if len(S) % 2 != count % 2:
    count += 1

print(count)