def solve(N, A):
    posi_A = []
    nega_A = []
    for x in A:
        if x > 0:
            posi_A.append(x)
        else:
            nega_A.append(x)
    posi_A.sort()
    nega_A.sort(reverse=True)
    
    ans = "Yes"
    if len(posi_A) == 0:
        B = nega_A
    elif len(nega_A) == 0:
        B = posi_A
    elif len(posi_A) == len(nega_A) + 1:
        B = []
        for i in range(len(nega_A)):
            B.append(posi_A[i])
            B.append(nega_A[i])
        B.append(posi_A[-1])
    elif len(nega_A) == len(posi_A) + 1:
        B = []
        for i in range(len(posi_A)):
            B.append(nega_A[i])
            B.append(posi_A[i])
        B.append(nega_A[-1])
    elif len(nega_A) == len(posi_A):
        B = []
        if abs(nega_A[0]) <= abs(posi_A[0]):
            for i in range(len(posi_A)):
                B.append(nega_A[i])
                B.append(posi_A[i])
        else:
            for i in range(len(posi_A)):
                B.append(posi_A[i])
                B.append(nega_A[i])
    else:
        ans = "No"
        B = []
    
    # print(B)
    if ans == "Yes":
        for i in range(N-1):
            if B[1]*B[i] != B[0]*B[i+1]:
                ans = "No"
    
    print(ans)

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)