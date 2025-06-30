N = int(input())
A = list(map(int,input().split()))

ans = 0
if N == 2:
    if A[0] == A[1]:
        ans = 2
elif N >= 3:
    Ls1 = [-1 for _ in range(N // 2)]
    for i in range(N // 2):
        k = i*2
        if A[k] == A[k+1]:
            Ls1[i] = A[k]
    # print(Ls1)

    K = len(Ls1)
    y = 0
    Kind = set()
    for x in range(K):
        if Ls1[x] == -1:
            Kind = set()
        else:
            if y <= x:
                y = x
                Kind = set([Ls1[x]])
            else:
                Kind.remove(Ls1[x-1])
            while y+1 < K:
                if Ls1[y+1] != -1 and Ls1[y+1] not in Kind:
                    Kind.add(Ls1[y+1])
                    y += 1
                else:
                    break
            ans = max(ans, 2*(y-x+1))

    Ls2 = [-1 for _ in range((N-1) // 2)]
    for i in range((N-1) // 2):
        k = 1 + i*2
        if A[k] == A[k+1]:
            Ls2[i] = A[k]
    # print(Ls2)

    K = len(Ls2)
    y = 0
    Kind = set()
    for x in range(K):
        if Ls2[x] == -1:
            Kind = set()
        else:
            if y <= x:
                y = x
                Kind = set([Ls2[x]])
            else:
                Kind.remove(Ls2[x-1])
            while y+1 < K:
                if Ls2[y+1] != -1 and Ls2[y+1] not in Kind:
                    Kind.add(Ls2[y+1])
                    y += 1
                else:
                    break
            ans = max(ans, 2*(y-x+1))

print(ans)