L, R = map(int,input().split())

def f(x):
    S = str(x)
    dig = len(S)
    Ls = [int(S[i]) for i in range(dig)]

    count = 0

    check_1 = True
    for i in range(1, dig):
        if Ls[0] <= Ls[i]:
            check_1 = False
    if check_1:
        count += 1
    # print("1", count)
    
    for k in range(dig-1):
        check_2 = True
        for i in range(1, k+1):
            if Ls[0] <= Ls[i]:
                check_2 = False
        if check_2:
            count += min(Ls[0], Ls[k+1]) * (Ls[0] ** (dig - k - 2))
    # print("2", count)

    for i in range(Ls[0]):
        count += i ** (dig - 1)
    # print("3", count)
    
    for k in range(1, dig):
        for i in range(1, 10):
            count += i ** (k - 1)
    
    return count

print(f(R) - f(L-1))