R_t, C_t, R_a, C_a = map(int, input().split())
N, M, L = map(int, input().split())

num_set = set()
num_set.add(0)

count = 0
S_ls = [[] for _ in range(M)]
for i in range(M):
    line = list(map(str, input().split()))
    pre_S = str(line[0])
    pre_A = int(line[1])
    S_ls[i] = [pre_S, pre_A]
    count += pre_A
    num_set.add(count)

count = 0
T_ls = [[] for _ in range(L)]
for j in range(L):
    line = list(map(str, input().split()))
    pre_T = str(line[0])
    pre_B = int(line[1])
    T_ls[j] = [pre_T, pre_B]
    count += pre_B
    num_set.add(count)

num_ls = list(num_set)
num_ls.sort()
diff_ls = [num_ls[i+1] - num_ls[i] for i in range(len(num_ls) - 1)]
# print(diff_ls)

new_S = []
i = 0
t = 0
while i < M:
    data = S_ls[i]
    direct = data[0]
    num = data[1]
    while num > 0:
        new_S.append([direct, diff_ls[t]])
        num -= diff_ls[t]
        t += 1
    i += 1

new_T = []
j = 0
t = 0
while j < L:
    data = T_ls[j]
    direct = data[0]
    num = data[1]
    while num > 0:
        new_T.append([direct, diff_ls[t]])
        num -= diff_ls[t]
        t += 1
    j += 1

# print(new_S)
# print(new_T)

ans = 0

for k in range(len(new_S)):
    data_S = new_S[k]
    direct_S = data_S[0]
    num = data_S[1]

    if direct_S == "L":
        new_R_t = R_t
        new_C_t = C_t - num
    elif direct_S == "R":
        new_R_t = R_t
        new_C_t = C_t + num
    elif direct_S == "U":
        new_R_t = R_t - num
        new_C_t = C_t
    else:
        new_R_t = R_t + num
        new_C_t = C_t

    data_T = new_T[k]
    direct_T = data_T[0]

    if direct_T == "L":
        new_R_a = R_a
        new_C_a = C_a - num
    elif direct_T == "R":
        new_R_a = R_a
        new_C_a = C_a + num
    elif direct_T == "U":
        new_R_a = R_a - num
        new_C_a = C_a
    else:
        new_R_a = R_a + num
        new_C_a = C_a
        
    # print(R_t, C_t, R_a, C_a)
    # print(direct_S, direct_T)

    if R_t == R_a:
        if C_t == C_a:
            if direct_S == direct_T:
                ans += num
        elif C_t < C_a:
            if (C_a - C_t) % 2 == 0 and num >= (C_a - C_t) // 2:
                if direct_S == "R" and direct_T == "L":
                    ans += 1
        else:
            if (C_t - C_a) % 2 == 0 and num >= (C_t - C_a) // 2:
                if direct_S == "L" and direct_T == "R":
                    ans += 1
    
    elif C_t == C_a:
        if R_t < R_a:
            if (R_a - R_t) % 2 == 0 and num >= (R_a - R_t) // 2:
                if direct_S == "D" and direct_T == "U":
                    ans += 1
        else:
            if (R_t - R_a) % 2 == 0 and num >= (R_t - R_a) // 2:
                if direct_S == "U" and direct_T == "D":
                    ans += 1
    
    elif R_a - R_t == C_a - C_t:
        if R_a > R_t:
            if direct_S == "R" and direct_T == "U" and R_a - R_t <= num:
                ans += 1
            elif direct_S == "D" and direct_T == "L" and R_a - R_t <= num:
                ans += 1
        else:
            if direct_T == "R" and direct_S == "U" and R_t - R_a <= num:
                ans += 1
            elif direct_T == "D" and direct_S == "L" and R_t - R_a <= num:
                ans += 1
    
    elif R_a - R_t == C_t - C_a:
        if R_a > R_t:
            if direct_S == "L" and direct_T == "U" and R_a - R_t <= num:
                ans += 1
            elif direct_S == "D" and direct_T == "R" and R_a - R_t <= num:
                ans += 1
        else:
            if direct_T == "L" and direct_S == "U" and R_t - R_a <= num:
                ans += 1
            elif direct_T == "D" and direct_S == "R" and R_t - R_a <= num:
                ans += 1

    R_t = new_R_t
    C_t = new_C_t
    R_a = new_R_a
    C_a = new_C_a
    # print(ans)
print(ans)