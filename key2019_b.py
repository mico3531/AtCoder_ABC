S = str(input())

left = 0
for i in range(7):
    if S[i] == "keyence"[i]:
        left += 1
    else:
        break

right = 0
for i in range(1, 8):
    if S[-i] == "keyence"[-i]:
        right += 1
    else:
        break

if left + right >= 7:
    print("YES")
else:
    print("NO")
