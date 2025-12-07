N = int(input())
S = str(input())

ans_1 = 0 # ABAB
ans_2 = 0 # BABA
B_count = 0

for i in range(2*N):
    if S[i] == "B":
        ans_1 += abs(2*B_count + 1 - i)
        ans_2 += abs(2*B_count - i)
        B_count += 1

print(min(ans_1, ans_2))