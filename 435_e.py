from sortedcontainers import SortedSet

N, Q = map(int, input().split())

Number_set = set()
L = [0 for _ in range(Q)]
R = [0 for _ in range(Q)]

for i in range(Q):
    L[i], R[i] = map(int, input().split())
    R[i] += 1
    Number_set.add(L[i])
    Number_set.add(R[i])

Number_ls = list(Number_set)
Number_ls.sort()
K = len(Number_ls)
# print(Number_ls)

ind_dict = dict()
for i in range(K):
    ind_dict[Number_ls[i]] = i

R_size = [Number_ls[i+1] - Number_ls[i] for i in range(K - 1)]
# print(R_size)

sum_size = 0

std = SortedSet(list(range(K - 1)))
# print("std is", std)

for i in range(Q):
    l_ind = ind_dict[L[i]]
    r_ind = ind_dict[R[i]]
    # print("l_ind:", l_ind, "r_ind:", r_ind)

    hit_array = list(std.irange(l_ind, r_ind-1))
    # print(hit_array)
    for x in hit_array:
        sum_size += R_size[x]
        std.discard(x)

    # print(sum_size)
    print(N - sum_size)