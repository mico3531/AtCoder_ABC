import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

import math

N, Q = map(int,input().split())
A = list(map(int,input().split()))

dig = math.ceil(math.log2(N))
Dat = [[0, 0, -1, 0] for _ in range(2**dig - 1)]
Dat += [[A[i], 1, 0, 0] for i in range(N)] 
Dat += [[0, 0, -1, 0] for _ in range(2**dig - N)]
# {最大値: 最大値の個数, 2番目の値: 2番目の値の個数}

N = 2 ** dig

def make_new_ls(Ls_1, Ls_2):
    num_ls = list(set([Ls_1[0], Ls_1[2], Ls_2[0], Ls_2[2]]))
    num_ls.sort(reverse=True)
    f = num_ls[0]
    s = num_ls[1]
    c_f = 0
    c_s = 0

    if Ls_1[0] == f:
        c_f += Ls_1[1]
    if Ls_1[0] == s:
        c_s += Ls_1[1]
    if Ls_1[2] == f:
        c_f += Ls_1[3]
    if Ls_1[2] == s:
        c_s += Ls_1[3]
    
    if Ls_2[0] == f:
        c_f += Ls_2[1]
    if Ls_2[0] == s:
        c_s += Ls_2[1]
    if Ls_2[2] == f:
        c_f += Ls_2[3]
    if Ls_2[2] == s:
        c_s += Ls_2[3]
    
    return [f, c_f, s, c_s]

for k in range(N-2, -1, -1):
    Dat[k] = make_new_ls(Dat[2*k + 1], Dat[2*k + 2])

def update(i, x):
    i += N - 1
    Dat[i] = [x, 1, 0, 0]
    while i > 0:
        i = (i-1) // 2
        Dat[i] = make_new_ls(Dat[2*i + 1], Dat[2*i + 2])

def solve(a, b, k, l, r):
    # k: 今見ているノードのインデックス
    # [a, b): 最終的に求めたい範囲
    # [l, r): 今見ている範囲

    if (r <= a or b <= l):
        # print(l, r, {0:0, -1:0})
        return [0, 0, -1, 0]
    elif (a <= l and r <= b):
        # print(l, r, Dat_dict[k])
        return Dat[k]
    else:
        ls_left = solve(a, b, k*2 + 1, l, (l+r) // 2)
        ls_right = solve(a, b, k*2 + 2, (l+r) // 2, r)
        new_ls = make_new_ls(ls_left, ls_right)
        # print(l, r, new_dict)
        return new_ls

def print_dict():
    for t in range(dig + 1):
        l = 2**t -1
        r = 2**(t+1) - 1
        print(Dat[l: r])

# print_dict()

for _ in range(Q):
    Query = list(map(int,input().split()))
    if Query[0] == 1:
        p = Query[1] - 1
        x = Query[2]
        update(p, x)
        # print_dict()
    else:
        l = Query[1] - 1
        r = Query[2]
        ans_ls = solve(l, r, 0, 0, N)
        print(ans_ls[3])