N = int(input())
A = list(map(int, input().split()))

ans = -10 ** 5
for i in range(N):
    ao_max_score = - 10 ** 5
    ta_max_score = - 10 ** 5
    
    for j in range(N):
        if j != i:
            x = min(i, j)
            y = max(i, j)
            B = A[x:y+1]
            ta_score = 0
            ao_score = 0

            for k in range(len(B)):
                if k % 2 == 0:
                    ta_score += B[k]
                else:
                    ao_score += B[k]

            if ao_score > ao_max_score:
                ta_max_score = ta_score
                ao_max_score = ao_score

    ans = max(ans, ta_max_score)

print(ans)