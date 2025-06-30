N = int(input())

A = 1
B = N
while B-A > 1:
    M = (A+B) // 2
    print("?", A, M, 1, N)
    width = M-A+1
    x = int(input())
    if width == x:
        A = M+1
    else:
        B = M
if A == B:
    ans_1 = A
else:
    print("?", A, A, 1, N)
    x = int(input())
    if x == 0:
        ans_1 = A
    else:
        ans_1 = B

C = 1
D = N
while D-C > 1:
    M = (C+D) // 2
    print("?", 1, N, C, M)
    width = M-C+1
    x = int(input())
    if x == width:
        C = M+1
    else:
        D = M
if C == D:
    ans_2 = C
else:
    print("?", 1, N, C, C)
    x = int(input())
    if x == 0:
        ans_2 = C
    else:
        ans_2 = D

print("!", ans_1, ans_2)