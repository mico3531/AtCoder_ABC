T = int(input())

for _ in range(T):
    N = int(input())
    S = str(input())
    
    L = -1
    R = N-1
    for i in range(N-1):
        if S[i] > S[i+1]:
            L = i
            for j in range(L+1, N):
                if S[j] > S[L]:
                    R = j-1
                    break
            break
    # print(L, R)
    
    if L == -1:
        print(S)
    else:
        ans_1 = S[:L]
        ans_2 = S[L+1:R+1]
        ans_3 = S[L]
        ans_4 = S[R+1:]
        print(ans_1 + ans_2 + ans_3 + ans_4)