import random as rd

def make_line(p_1, p_2):
    x_1 = p_1[0]
    y_1 = p_1[1]
    x_2 = p_2[0]
    y_2 = p_2[1]

    a = y_1 - y_2
    b = x_2 - x_1
    c = x_1 * y_2 - x_2 * y_1
    return a, b, c

N = int(input())
point_ls = [[] for _ in range(N)]
for i in range(N):
    point_ls[i] = list(map(int, input().split()))

times = 100
for _ in range(times):
    p = rd.randint(0, N-1)
    q = p
    while q == p:
        q = rd.randint(0, N-1)
    a, b, c = make_line(point_ls[p], point_ls[q])

    count = 0
    for i in range(N):
        x, y = point_ls[i][0], point_ls[i][1]
        if a*x + b*y + c == 0:
            count += 1
    
    if 2*count > N:
        print("Yes")
        print(a, b, c)
        exit()

print("No")